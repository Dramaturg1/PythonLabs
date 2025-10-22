import math

class Shape:
    def __init__(self, shape_id: str, points: list[tuple[float, float]]):
        self.id = shape_id
        if not points or len(points) < 3:
            raise ValueError("Фигура должна иметь как минимум 3 точки.")
        self.points = points

    def move(self, dx: float, dy: float):
        self.points = [(x + dx, y + dy) for x, y in self.points]

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, points={self.points})"


class Triangle(Shape):
    def __init__(self, shape_id: str, points: list[tuple[float, float]]):
        if len(points) != 3:
            raise ValueError("Треугольник должен иметь ровно 3 вершины.")
        super().__init__(shape_id, points)


class Pentagon(Shape):
    def __init__(self, shape_id: str, points: list[tuple[float, float]]):
        if len(points) != 5:
            raise ValueError("Пятиугольник должен иметь ровно 5 вершин.")
        super().__init__(shape_id, points)


def is_intersect(fig1: Shape, fig2: Shape) -> bool:
    if not isinstance(fig1, Shape) or not isinstance(fig2, Shape):
        raise TypeError("Обе фигуры должны быть экземплярами класса Shape.")

    def bbox(points):
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        return min(xs), max(xs), min(ys), max(ys)

    x1_min, x1_max, y1_min, y1_max = bbox(fig1.points)
    x2_min, x2_max, y2_min, y2_max = bbox(fig2.points)

    return not (x1_max < x2_min or x2_max < x1_min or y1_max < y2_min or y2_max < y1_min)


if __name__ == "__main__":
    try:
        t1 = Triangle("T1", [(0, 0), (2, 0), (1, 2)])
        p1 = Pentagon("P1", [(1, 1), (3, 1), (4, 2), (3, 3), (1, 3)])

        print("Исходные фигуры:")
        print(t1)
        print(p1)

        print("\nПеремещаем треугольник на (1, 1):")
        t1.move(1, 1)
        print(t1)

        print("\nПересекаются ли фигуры?")
        print("Да" if is_intersect(t1, p1) else "Нет")

    except Exception as e:
        print(f"Ошибка: {e}")