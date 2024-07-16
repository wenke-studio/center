import reflex as rx


class Line(rx.Base):
    data_key: str
    stroke: str


def line(data: rx.Var | list[dict], data_key: str, lines: list[Line], height: int = 300) -> rx.Component:
    return rx.recharts.line_chart(
        *[rx.recharts.line(data_key=line.data_key, stroke=line.stroke) for line in lines],
        rx.recharts.x_axis(data_key=data_key),
        rx.recharts.y_axis(),
        data=data,
        height=height,
    )
