import numpy as np
import math
from manim import Scene, Square, Circle, Triangle, Dot, Group, Text, UP, DOWN, LEFT, RIGHT, RED, GREEN, BLUE, WHITE, YELLOW, ORANGE, PURPLE, GOLD, GRAY, Transform, Create, FadeIn, FadeOut, MoveAlongPath, Line, Arc, Write, Rotate, PI, ValueTracker, always_redraw, Axes

class AnimatedShapes(Scene):
    def construct(self):
        # Create a square
        square = Square(side_length=2, color=BLUE)
        square_label = Text("Square", font_size=24)
        square_label.next_to(square, UP)

        # Create a circle
        circle = Circle(radius=1, color=GREEN)
        circle_label = Text("Circle", font_size=24)
        circle_label.next_to(circle, DOWN)

        # Create a triangle
        triangle = Triangle(color=RED)
        triangle_label = Text("Triangle", font_size=24)
        triangle_label.next_to(triangle, UP)

        # Position the shapes
        square.to_edge(LEFT)
        circle.to_edge(RIGHT)
        triangle.to_edge(UP)

        # Animations
        self.play(Create(square), Write(square_label))
        self.play(Create(circle), Write(circle_label))
        self.play(Create(triangle), Write(triangle_label))
        self.wait(1)

        # Transformation: Square to Circle
        self.play(Transform(square, circle.copy().move_to(square.get_center())))
        self.play(FadeOut(square_label), FadeIn(circle_label.copy().move_to(square_label.get_center())))
        self.wait(1)

        # Rotation
        self.play(Rotate(triangle, angle=PI, about_point=triangle.get_center()))
        self.wait(1)

        # Fading out
        self.play(FadeOut(square), FadeOut(circle), FadeOut(triangle), FadeOut(circle_label), FadeOut(triangle_label))
        self.wait(1)

        # Dynamic number line
        number_line = Axes(
            x_range=[-5, 5, 1],
            y_range=[-1, 1, 0.5],
            axis_config={"include_numbers": True},
        )
        number_line_labels = number_line.get_axis_labels()

        dot = Dot(color=YELLOW)
        dot.move_to(number_line.coords_to_point(2, 0))

        tracker = ValueTracker(2)

        dot.add_updater(lambda d: d.move_to(number_line.coords_to_point(tracker.get_value(), 0)))

        self.play(Create(number_line), Write(number_line_labels))
        self.play(Create(dot))
        self.play(tracker.animate.set_value(-3), run_time=5)
        self.wait(1)

        self.play(FadeOut(number_line), FadeOut(dot), FadeOut(number_line_labels))
        self.wait(1)