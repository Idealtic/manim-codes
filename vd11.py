import os
from pathlib import Path
from manim import *
class vd11(Scene):
    def construct(self):
        # Set global LaTeX preamble for Vietnamese support
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"""
            \usepackage[utf8]{vietnam}
            \usepackage[left=3cm,right=3cm,top=2cm,bottom=2cm]{geometry}
        """)
        Tex.set_default(tex_template=tex_template, font_size=30, tex_environment="flushleft")
        MathTex.set_default(tex_template=tex_template, font_size=30)

        question = Tex(r"Ví dụ 11: Diện tích hình phẳng giới hạn bởi đồ thị \((C)\) của hàm số \(y=\dfrac{1}{2}(x^2-4x+3)\) và 2 tiếp tuyến của \((C)\) xuất phát từ \(M(3;-2)\) là:").to_corner(UL, buff=0.3)
    
        ax = Axes(
            x_range=[-2,7,1],
            x_length = 9,
            y_range=[-2,8,1],
            y_length = 10,
            axis_config={"tip_shape": StealthTip,
                         "font_size": 16,
                         "tip_width": 0.15,
                         "tip_height": 0.15,
                         "include_ticks": False,
                         }            
        ).scale(0.5).to_edge(RIGHT).shift(DOWN *0.5)
        labelx = MathTex(r"x").next_to(ax.x_axis.get_end(), DOWN, buff=0.1)
        labely = MathTex(r"y").next_to(ax.y_axis.get_end(), LEFT, buff=0.1)
        labelO = MathTex(r"O").next_to(ax.c2p(0, 0), DL, buff=0.1)
        parabol = ax.plot(lambda x: (x**2)/2-2*x+3/2, x_range=[-2,6])
        line1 = ax.plot(lambda x: 1-x, x_range=[-2,3.5])
        labelline1 = MathTex(r"\Delta_1").next_to(line1.get_start(), LEFT *0.5)
        line2 = ax.plot(lambda x: 3*x-11, x_range=[17/6,6])
        labelline2 = MathTex(r"\Delta_2").next_to(line2.get_end(), RIGHT *0.5)
        pointm = Dot(ax.c2p(3,-2))
        labelm = MathTex("M(3;-2)").next_to(pointm, RIGHT*0.5)
        linemid = Line(ax.c2p(3,4),ax.c2p(3,-2.5))
        tangent1 = Dot(ax.c2p(1,0))
        tangent2 = Dot(ax.c2p(5,4))
        labeltangent1 = MathTex("1").next_to(tangent1, DOWN)
        labeltangent2 = MathTex("5").next_to(ax.c2p(5,0), DOWN)
        tangent2x = DashedLine(ax.c2p(5,4),ax.c2p(5,0))
        area1 = ax.get_area(graph = parabol, bounded_graph = line1, x_range=[1,3], color=RED)
        area2 = ax.get_area(graph = parabol, bounded_graph = line2, x_range=[3,5], color=BLUE)
        t1 = MathTex(r"f(x)=\frac{1}{2}(x^2-4x+3) \Rightarrow f'(x)=x-2").next_to(question, DOWN).to_edge(LEFT, buff=0.3)
        t2 = Tex(r"Tiếp tuyến tại \((C)\) tại điểm \(A(x_0,f(x_0))\) có phương trình dạng:").next_to(t1, DOWN, aligned_edge=LEFT, buff=0.1)
        t3 = MathTex(r"\begin{split} \Delta: y&=f'(x-x_0)(x-x_0)+f(x_0)\\ &=(x_0-2)(x-x_0)+\frac{1}{2}(x_0^2-4x_0+3) \end{split}").next_to(t2, DOWN, aligned_edge=LEFT, buff=0.1)
        t4 = Tex(r"Tiếp tuyến xuất phát từ \(M(3;-2)\) nên:").next_to(t3, DOWN, aligned_edge=LEFT, buff=0.1)
        t5 = MathTex(r"-2=(x_0-2)(3-x_0)+\frac{1}{2}(x_0^2-4x_0+3)").next_to(t4, DOWN, aligned_edge=LEFT, buff=0.1)
        t6 = MathTex(r"\Leftrightarrow -\frac{1}{2}x_0^2+3x_0-\frac{5}{2}=0 \Leftrightarrow \begin{cases} x_{01}=1 \\ x_{02}=5 \end{cases} \Rightarrow \begin{cases} \Delta_1: y=-x+1 \\ \Delta_2: y=3x-11 \end{cases}").next_to(t5, DOWN, aligned_edge=LEFT, buff=0.1)
        t7 = Tex(r"Dựa vào đồ thị, diện tích hình phẳng cần tính là:").next_to(t6, DOWN, aligned_edge=LEFT, buff=0.1)
        t8 = MathTex(r"\begin{split} S&=S_1+S_2 \\ &=\int\limits_{1}^{3}\left[\left(\frac{1}{2}x^2-2x+\frac{3}{2}\right)-(-x+1)\right]\,\mathrm{d}x+\int\limits_{3}^{5}\left[\left(\frac{1}{2}x^2-2x+\frac{3}{2}\right)-(3x-11)\right]\,\mathrm{d}x=\frac{8}{3} \end{split}").next_to(t7, DOWN, aligned_edge=LEFT, buff=0.1)
        t8[0][2:4].set_color(RED)
        t8[0][5:7].set_color(BLUE)

        self.add(question,ax,labelx,labely,labelO,parabol,line1,line2,pointm,labelm,linemid,tangent1,tangent2,labeltangent1,labeltangent2,tangent2x,area1,area2,labelline1,labelline2,t1,t2,t3,t4,t5,t6,t7,t8)
FLAGS = f"-pqm"
SCENE = "vd11"

if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
