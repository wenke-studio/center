from datetime import datetime, timedelta, timezone

import bcrypt
import reflex as rx
from sqlmodel import Column, DateTime, Field, func

SALT = b"$2b$12$LD76ivI5jIJPYQpTTPXh7."  # created by bcrypt.gensalt()


class User(rx.Model, table=True):
    email: str
    password: str

    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hashpw(
            password=password.encode("utf-8"),
            salt=SALT,
        ).decode("utf-8")

    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(
            password=password.encode("utf-8"),
            hashed_password=self.password.encode("utf-8"),
        )

    @classmethod
    def create(cls, email: str, password: str) -> "User":
        with rx.session() as session:
            user = cls(
                email=email,
                password=cls.hash_password(password),
            )
            session.add(user)
            session.commit()
            session.refresh(user)
            return user


class Token(rx.Model, table=True):
    user_id: int = Field(nullable=False)
    client_token: str = Field(unique=True, nullable=False)
    expired_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )

    @classmethod
    def create(cls, user_id: int, client_token: str) -> "Token":
        with rx.session() as session:
            token = cls(
                user_id=user_id,
                client_token=client_token,
                expired_at=datetime.now(timezone.utc) + timedelta(hours=1),
            )
            session.add(token)
            session.commit()
            session.refresh(token)
            return token
