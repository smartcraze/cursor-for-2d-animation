from manim import *

class ComputerScienceTimeline(Scene):
    def construct(self):
        timeline_color = BLUE
        era_color = GREEN
        text_color = WHITE
        number_color = YELLOW

        timeline = Line(LEFT * 6, RIGHT * 6, color=timeline_color)
        self.play(Create(timeline))

        # Define eras and positions
        eras = [
            {"name": "Early Computing (Pre-1940)", "position": -5, "year": 1940},
            {"name": "Mainframe Era (1940-1970)", "position": -3, "year": 1970},
            {"name": "Personal Computing (1970-1990)", "position": -1, "year": 1990},
            {"name": "Internet Era (1990-2010)", "position": 1, "year": 2010},
            {"name": "Mobile/Cloud (2010-Present)", "position": 3, "year": 2024},
        ]

        era_markers = VGroup()
        era_labels = VGroup()
        year_labels = VGroup()

        for era in eras:
            position = era["position"]
            name = era["name"]
            year = era["year"]

            marker = Dot(color=era_color).move_to(timeline.point_from_proportion((position + 6) / 12))
            era_markers.add(marker)

            label = Text(name, color=text_color, font_size=18).next_to(marker, UP)
            era_labels.add(label)

            year_label = Text(str(year), color=number_color, font_size=16).next_to(marker, DOWN)
            year_labels.add(year_label)

        self.play(Create(era_markers, run_time=2))
        self.play(Write(era_labels, run_time=3))
        self.play(Write(year_labels, run_time=3))

        self.wait(2)

        title = Text("Computer Science History", color=text_color, font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(3)

        self.play(FadeOut(VGroup(timeline, era_markers, era_labels, year_labels, title)))
        self.wait(1)