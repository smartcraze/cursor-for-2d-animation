from manim import *
import numpy as np

class GrowingSineWave(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-2 * PI, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=9,
            y_length=3,
            axis_config={"include_numbers": True}
        )

        # Optional axis labels
        labels = ax.get_axis_labels(x_label="x", y_label="y")

        func = lambda x: np.sin(x)
        tracker = ValueTracker(-2 * PI)

        growing_graph = always_redraw(
            lambda: ax.plot(func, color=BLUE, x_range=[-2 * PI, tracker.get_value()])
        )

        sin_text = Text("sin(x)", font_size=24).next_to(ax, UP)

        self.play(Create(ax), Write(sin_text), Write(labels))
        self.add(growing_graph)
        self.play(tracker.animate.set_value(2 * PI), run_time=4, rate_func=linear)
        self.wait()
