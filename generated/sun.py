import numpy as np
from manim import Scene, Square, Circle, Triangle, Text, Group, ValueTracker, always_redraw, Line, WHITE, RED, BLUE, GREEN, Create, Transform, Write, MoveAlongPath, Dot, Axes

class AnimatedShapes(Scene):
    def construct(self):
        square = Square(side_length=2, color=BLUE)
        circle = Circle(radius=1, color=RED)
        triangle = Triangle(color=GREEN)

        square_label = Text("Square", font_size=24).next_to(square, DOWN)
        circle_label = Text("Circle", font_size=24).next_to(circle, DOWN)
        triangle_label = Text("Triangle", font_size=24).next_to(triangle, DOWN)

        self.play(Create(square), Write(square_label))
        self.play(Create(circle), Write(circle_label))
        self.play(Create(triangle), Write(triangle_label))

        group = Group(square, circle, triangle, square_label, circle_label, triangle_label).scale(0.7)
        self.play(Transform(group, group.copy().move_to(ORIGIN)))

        tracker = ValueTracker(0)
        line = always_redraw(lambda: Line(start=group.get_center(), end=group.get_center() + [3*np.cos(tracker.get_value()), 3*np.sin(tracker.get_value()), 0], color=WHITE))
        dot = always_redraw(lambda: Dot(group.get_center() + [3*np.cos(tracker.get_value()), 3*np.sin(tracker.get_value()), 0], color=WHITE))

        self.play(Create(line), Create(dot))
        self.play(tracker.animate.set_value(2 * np.pi), run_time=5)

        self.wait(1)

        axes = Axes(x_range=[-5, 5, 1], y_range=[-5, 5, 1], axis_config={"color": WHITE})
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        self.play(Transform(group, axes), Uncreate(line), Uncreate(dot))
        self.play(Transform(square_label, labels[0]), Transform(circle_label, labels[1]))
        self.play(Uncreate(triangle), Uncreate(triangle_label))

        graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        self.play(Create(graph))

        self.wait(2)