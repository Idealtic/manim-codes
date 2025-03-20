import os
from pathlib import Path
from manim import *
class vd8(Scene):
    def construct(self):
        # Set global LaTeX preamble for Vietnamese support
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"""
            \usepackage[utf8]{vietnam}
            \usepackage[left=3cm,right=3cm,top=2cm,bottom=2cm]{geometry}
        """)
        Tex.set_default(tex_template=tex_template, font_size=30, tex_environment="flushleft")
        MathTex.set_default(tex_template=tex_template, font_size=30)

        question = Tex(r"Ví dụ 8: Tính diện tích hình phẳng giới hạn bởi các đồ thị hàm số \(y=x^2,\,\, y=\dfrac{x^2}{8},\,\, y=\dfrac{27}{x}\)").to_corner(UL, buff=0.3)
        ax = Axes(
            x_range=[-0.5,8,1],
            y_range=[-0.5,12,1],
            axis_config={"tip_shape": StealthTip,
                         "font_size": 16,
                         "tip_width": 0.15,
                         "tip_height": 0.15,
                         "include_ticks": False,
                         }            
        ).scale(0.5).to_edge(RIGHT).shift(DOWN)
        labelx = MathTex(r"x").next_to(ax.x_axis.get_end(), DOWN, buff=0.1)
        labely = MathTex(r"y").next_to(ax.y_axis.get_end(), LEFT, buff=0.1)
        labelO = MathTex(r"O").next_to(ax.c2p(0, 0), DL, buff=0.1)
        graph1 = ax.plot(lambda x: x**2, x_range=[0,3.5,0.01],color=RED)
        graph1label = MathTex(r"y=x^2", color=RED).next_to(graph1).shift(UP *1.75)
        graph2 = ax.plot(lambda x: (x**2)/8, x_range=[0,7,0.01],color=BLUE)
        graph3label = MathTex(r"y=\frac{27}{x}", color=YELLOW).next_to(graph2)
        graph3 = ax.plot(lambda x: 27/x, x_range=[2.7,7,0.01],color=YELLOW)
        graph2label = MathTex(r"y=\frac{x^2}{8}", color=BLUE).next_to(graph3)
        line1 = Line(ax.c2p(3,9),ax.c2p(3,0))
        line1label = MathTex("3").next_to(ax.c2p(3,0), DOWN)
        line2 = Line(ax.c2p(6,4.5),ax.c2p(6,0))
        line2label = MathTex("6").next_to(ax.c2p(6,0), DOWN)
        area1 = ax.get_area(graph=graph1, bounded_graph=graph2, x_range=[0,3], color=GREEN, fill_opacity=0.3)
        area1label = MathTex(r"S_1").move_to(area1).shift(RIGHT *0.75)
        area2 = ax.get_area(graph=graph3, bounded_graph=graph2, x_range=[3,6], color=GREEN, fill_opacity=0.3)
        area2label = MathTex(r"S_2").move_to(area2).shift(LEFT *0.5)
        t1 = Tex(r"Xét phương trình hoành độ giao điểm:").next_to(question, DOWN).to_edge(LEFT, buff=0.3)
        t2 = MathTex(r"x^2=\frac{x^2}{8} \Leftrightarrow x=0").next_to(t1, DOWN, aligned_edge=LEFT, buff=0.1)
        t3 = MathTex(r"x^2=\frac{27}{x} \Leftrightarrow x=3").next_to(t2, DOWN, aligned_edge=LEFT, buff=0.1)
        t4 = MathTex(r"\frac{x^2}{8}=\frac{27}{x} \Leftrightarrow x=6").next_to(t3, DOWN, aligned_edge=LEFT, buff=0.1)
        t5 = MathTex(r"S=S_1+S_2=\int\limits_{0}^{3}\left|x^2-\frac{x^2}{8}\right|\,\mathrm{d}x+\int\limits_{3}^{6}\left|\frac{27}{x}-\frac{x^2}{8}\right|\,\mathrm{d}x \approx 18,7").next_to(t4, DOWN, aligned_edge=LEFT, buff=0.1)

        self.add(question,ax,labelx,labely,labelO,graph1,graph2,graph3,line1,line2,line1label,line2label,area1,area2,area1label,area2label,t1,t2,t3,t4,t5,graph1label,graph2label,graph3label)
FLAGS = f"-pqm"
SCENE = "vd8"

if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f'manim "{script_name}" {SCENE} {FLAGS}')
