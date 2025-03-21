import os
from pathlib import Path
from manim import *
class vd10(Scene):
    def construct(self):
        # Set global LaTeX preamble for Vietnamese support
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"""
            \usepackage[utf8]{vietnam}
            \usepackage[left=3cm,right=3cm,top=2cm,bottom=2cm]{geometry}
        """)
        Tex.set_default(tex_template=tex_template, font_size=30, tex_environment="flushleft")
        MathTex.set_default(tex_template=tex_template, font_size=30)

        question = Tex(r"Ví dụ 10: Diện tích \(S\) của hình phẳng giới hạn bởi đồ thị hàm số \(y=x^2-4x+5 (C)\) và hai tiếp tuyến của \((C)\) tại các tiếp điểm \(A(1;2),B(4;5)\) là:").to_corner(UL, buff=0.3)
    
        ax = Axes(
            x_range=[-1,5,1],
            x_length = 6,
            y_range=[-2,8,1],
            y_length = 10,
            axis_config={"tip_shape": StealthTip,
                         "font_size": 16,
                         "tip_width": 0.15,
                         "tip_height": 0.15,
                         "include_ticks": False,
                         }            
        ).scale(0.5).shift(RIGHT *5.5).shift(DOWN *0.5)
        labelx = MathTex(r"x").next_to(ax.x_axis.get_end(), DOWN, buff=0.1)
        labely = MathTex(r"y").next_to(ax.y_axis.get_end(), LEFT, buff=0.1)
        labelO = MathTex(r"O").next_to(ax.c2p(0, 0), DL, buff=0.1)   
        parabol = ax.plot(lambda x: x**2-4*x+5, x_range=[-0.5,4.5,0.01])
        pointa = Dot(ax.c2p(1,2))
        pointb = Dot(ax.c2p(4,5))
        labela = MathTex("A").next_to(pointa, LEFT *0.5)
        labelb = MathTex("B").next_to(pointb, RIGHT *0.5)
        line1 = ax.plot(lambda x: -2*x+4, x_range=[-0.5,3,0.01])
        line2 = ax.plot(lambda x: 4*x-11, x_range=[2.25,4.5,0.01])
        midline = Line(ax.c2p(2.5,6),ax.c2p(2.5,-2))
        linea = DashedLine(pointa,ax.c2p(1,0))
        labelx1 = MathTex("1").next_to(ax.c2p(1,0), DOWN)
        lineb = DashedLine(pointb,ax.c2p(4,0))
        labelx2 = MathTex("4").next_to(ax.c2p(4,0), DOWN)
        labelmid = MathTex(r"\frac{5}{2}",font_size=15).next_to(ax.c2p(2.5,0), UL, buff=0.1)
        area1 = ax.get_area(graph=parabol, bounded_graph=line1, x_range=[1,2.5], color=RED)
        area2 = ax.get_area(graph=parabol, bounded_graph=line2, x_range=[2.5,4], color=BLUE)
        t1 = MathTex(r"y=x^2-4x+5 \Rightarrow y'=2x-4 \Rightarrow \begin{cases} f'(1)=-2 \\ f'(4)=4 \end{cases}").next_to(question, DOWN).to_edge(LEFT, buff=0.3)
        t2 = Tex(r"Phương trình tiếp tuyến với \(C\) tại điểm \(A(1;2)\) là:").next_to(t1, DOWN, aligned_edge=LEFT, buff=0.1)
        t3 = MathTex(r"y-y_A=f'(x_A)(x-x_A) \Leftrightarrow y=-2(x-1)+2 \Leftrightarrow y=-2x+4 \, (d)").next_to(t2, DOWN, aligned_edge=LEFT, buff=0.1)
        t4 = Tex(r"Phương trình tiếp tuyến với \(C\) tại điểm \(B(4;5)\) là:").next_to(t3, DOWN, aligned_edge=LEFT, buff=0.1)
        t5 = MathTex(r"y-y_B=f'(x_B)(x-x_B) \Leftrightarrow y=4(x-4)+5 \Leftrightarrow y=4x-11 \, (d')").next_to(t4, DOWN, aligned_edge=LEFT, buff=0.1)
        t6 = Tex(r"Phương trình hoành độ giao điểm của 2 tiếp tuyến là:").next_to(t5, DOWN, aligned_edge=LEFT, buff=0.1)
        t7 = MathTex(r"-2x+4=4x-11 \Leftrightarrow x=\frac{5}{2}").next_to(t6, DOWN, aligned_edge=LEFT, buff=0.1)
        t8 = Tex(r"Diện tích \(S\) cần tìm là: ").next_to(t7, DOWN, aligned_edge=LEFT, buff=0.1)
        t9 = MathTex(r"\begin{split} S&=S_1+S_2 \\ &=\int\limits_{1}^{\frac{5}{2}}|(x^2-4x+5)-(-2x+4)|\,\mathrm{d}x+\int\limits_{\frac{5}{2}}^{4}|(x^2-4x+5)-(4x-11)|\,\mathrm{d}x=\frac{9}{4} \end{split}").next_to(t8, DOWN, aligned_edge=LEFT, buff=0.1)
        t9[0][2:4].set_color(RED)
        t9[0][5:7].set_color(BLUE)
        
        self.add(question,ax,labelx,labely,labelO,parabol,pointa,pointb,labela,labelb,line1,line2,midline,linea,labelx1,lineb,labelx2,labelmid,area1,area2,t1,t2,t3,t4,t5,t6,t7,t8,t9)
FLAGS = f"-pqm"
SCENE = "vd10"

if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
