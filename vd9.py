import os
from pathlib import Path
from manim import *
class vd9(Scene):
    def construct(self):
        # Set global LaTeX preamble for Vietnamese support
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"""
            \usepackage[utf8]{vietnam}
            \usepackage[left=3cm,right=3cm,top=2cm,bottom=2cm]{geometry}
        """)
        Tex.set_default(tex_template=tex_template, font_size=30, tex_environment="flushleft")
        MathTex.set_default(tex_template=tex_template, font_size=30)

        question = Tex(r"Ví dụ 9: Cho Parabol \((P)\) và đường tròn \((C)\) có tâm \(A(0,3)\), bán kính bằng \(\sqrt{5}\) như hình vẽ. Diện tích phần được tô màu (làm tròn đến chữ số hàng phần trăm) là: ").to_corner(UL, buff=0.3)
    
        ax = Axes(
            x_range=[-4,4,1],
            x_length = 8,
            y_range=[0,6,1],
            y_length = 6,
            axis_config={"tip_shape": StealthTip,
                         "font_size": 16,
                         "tip_width": 0.15,
                         "tip_height": 0.15,
                         "include_ticks": False,
                         }            
        ).scale(0.7).to_edge(RIGHT).shift(DOWN)
        labelx = MathTex(r"x").next_to(ax.x_axis.get_end(), DOWN, buff=0.1)
        labely = MathTex(r"y").next_to(ax.y_axis.get_end(), LEFT, buff=0.1)
        labelO = MathTex(r"O").next_to(ax.c2p(0, 0), DL, buff=0.1)       
        parabol = ax.plot(lambda x: x**2, x_range=[-2.5,2.5])
        circleup = ax.plot(lambda x: 3+np.sqrt(max(5-x**2,0)), x_range=[-np.sqrt(5),np.sqrt(5),0.01])
        circledown = ax.plot(lambda x: 3-np.sqrt(max(5-x**2,0)), x_range=[-np.sqrt(5),np.sqrt(5),0.01])
        line1 = Line(ax.c2p(-3,3),ax.c2p(3,3))
        line2 = DashedLine(ax.c2p(-2,4),ax.c2p(-2,0))
        line3 = DashedLine(ax.c2p(-1,1),ax.c2p(-1,0))
        line4 = DashedLine(ax.c2p(1,1),ax.c2p(1,0))
        line5 = DashedLine(ax.c2p(2,4),ax.c2p(2,0))
        line6 = DashedLine(ax.c2p(-2,4),ax.c2p(2,4))
        labelneg2 = MathTex("-2").next_to(ax.c2p(-2,0), DOWN)
        labelneg1 = MathTex("-1").next_to(ax.c2p(-1,0), DOWN)
        label1 = MathTex("1").next_to(ax.c2p(1,0), DOWN)
        label2 = MathTex("2").next_to(ax.c2p(2,0), DOWN)
        labelliney = MathTex("y=3").next_to(line1)
        label3y = MathTex("3").next_to(ax.c2p(0,3), DL, buff=0.1)
        label4y = MathTex("4").next_to(ax.c2p(0,4), DL, buff=0.1)
        center = Dot(ax.c2p(0,3))
        labelcenter = MathTex("A").next_to(center, UR, buff=0.1)
        s11 = ax.get_area(graph = parabol, bounded_graph = circledown, x_range=[1,2], color=RED)
        s12 = ax.get_area(graph = circleup, bounded_graph = circledown, x_range=[2,np.sqrt(5)], color=RED)
        s2 = ax.get_area(graph = circledown, bounded_graph = parabol, x_range=[-1,1], color=BLUE)
        s31 = ax.get_area(graph = parabol, bounded_graph = circledown, x_range=[-2,-1], color = YELLOW)
        s32 = ax.get_area(graph = circleup, bounded_graph = circledown, x_range=[-np.sqrt(5),-2], color=YELLOW)  
        t1 = MathTex(r"x^2+(y-3)^2=5 \Rightarrow y-3=-\sqrt{5-x^2}\,(y<3)").next_to(question, DOWN).to_edge(LEFT, buff=0.3)
        t2 = MathTex(r"\Leftrightarrow y=3-\sqrt{5-x^2}=g(x)").next_to(t1, DOWN, aligned_edge=LEFT, buff=0.1)
        t3 = MathTex(r"S_2=\int\limits_{-1}^{1}(3-\sqrt{5-x^2})\,\mathrm{d}x \approx 1,015").next_to(t2, DOWN, aligned_edge=LEFT, buff=0.1)
        t3[0][0:2].set_color(BLUE)
        t4 = Tex(r"Tiếp theo xét \(S_1\) do \(S_1=S_3\)").next_to(t3, DOWN, aligned_edge=LEFT, buff=0.1)
        VGroup(t4[0][11:13],t4[0][15:17]).set_color(RED)
        t4[0][18:20].set_color(YELLOW)
        t5 = MathTex(r"y=x^2 \Rightarrow x=\sqrt{y}").next_to(t4, DOWN, aligned_edge=LEFT, buff=0.1)
        t6 = MathTex(r"x^2+(y-3)^2=5 \Rightarrow x=\sqrt{5-(y-3)^2}").next_to(t5, DOWN, aligned_edge=LEFT, buff=0.1)
        t7 = MathTex(r"S_1=\int\limits_{1}^{4}(\sqrt{5-(y-3)^2}-\sqrt{y})\,\mathrm{d}y \approx 1,26").next_to(t6, DOWN, aligned_edge=LEFT, buff=0.1)
        t7[0][0:2].set_color(RED)
        t8 = MathTex(r"\Rightarrow S=S_1+S_2+S_3=S_2+2S_1=3,54").next_to(t7, DOWN, aligned_edge=LEFT, buff=0.1)
        VGroup(t8[0][3:5],t8[0][16:18]).set_color(RED)
        VGroup(t8[0][6:8],t8[0][12:14]).set_color(BLUE)
        t8[0][9:11].set_color(YELLOW)

        self.add(question,ax,labelx,labely,labelO,parabol,circleup,circledown,line1,line2,line3,line4,line5,line6,labelneg2,labelneg1,label1,label2,labelliney,label3y,label4y,center,labelcenter,s11,s2,s12,s31,s32,t1,t2,t3,t4,t5,t6,t7,t8)
FLAGS = f"-pqm"
SCENE = "vd9"

if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
