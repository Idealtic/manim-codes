import os
from pathlib import Path
from manim import *
class vd7 (Scene):
    def construct(self):
        # Set global LaTeX preamble for Vietnamese support
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"""
            \usepackage[utf8]{vietnam}
            \usepackage[left=3cm,right=3cm,top=2cm,bottom=2cm]{geometry}
        """)
        Tex.set_default(tex_template=tex_template, font_size=30, tex_environment="flushleft")
        MathTex.set_default(tex_template=tex_template, font_size=30)

        question = Tex(r"Tính diện tích của phần hình phẳng tô màu trong hình vẽ sau:").to_edge(UP)
        ax = Axes(
            x_range=[-0.5,6,1],
            y_range=[-0.5,3,1],
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
        curve = ax.plot(lambda x: np.sqrt(x), x_range=[0,5,0.01])
        line = ax.plot(lambda x: x-2, x_range=[1,5,1])
        areabig = ax.get_area(curve, [0,4])
        areasmall = ax.get_area(line, [2,4])
        area = Exclusion(areabig,areasmall, color=RED, fill_opacity=0.3)
        point1label = MathTex("2").next_to(ax.c2p(2,0), DOWN)
        point2label = MathTex("4").next_to(ax.c2p(4,0), DOWN)
        point2labely = MathTex("2").next_to(ax.c2p(0,2), LEFT)
        firstline = Line(ax.c2p(2,np.sqrt(2)),ax.c2p(2,0))
        secondline = Line(ax.c2p(4,2),ax.c2p(4,0))
        secondliney = DashedLine(ax.c2p(4,2),ax.c2p(0,2))
        labelh1 = MathTex(r"(H_1)").move_to(area).shift(LEFT *0.75, DOWN *0.5)
        labelh2 = MathTex(r"(H_2)").move_to(area).shift(RIGHT *0.5)
        labelN = MathTex("N").next_to(ax.c2p(4,2), UP, buff=0.1)
        labelK = MathTex("K").next_to(ax.c2p(2,0), UL, buff=0.1)
        labelM = MathTex("M").next_to(ax.c2p(4,0), UR, buff=0.1)
        t1 = Tex(r"Cách 1: \(S=S_1+S_2\)").next_to(question, DOWN).shift(LEFT *2)
        h1 = MathTex(r"(H_1):\begin{cases} y=\sqrt{x} \\ y=0 \\ x=0 \\ x=2 \end{cases}").next_to(t1, DOWN)
        t2 = MathTex(r"S(H_1)=\int\limits_{0}^{2}\sqrt{x}\,\mathrm{d}x=1,885...\to A").next_to(h1, DOWN)
        t3 = MathTex(r"\begin{cases} x\geqslant 2 \\ \sqrt{x}=x-2 \end{cases}").next_to(t2, DOWN)
        t4 = MathTex(r"S(H_2)=\int\limits_{2}^{4}[\sqrt{x}-(x-2)]\,\mathrm{d}x=1,4477...\to B").next_to(t3, DOWN)
        t5 = MathTex(r"\Rightarrow S=S(H_1)+S(H_2)=A+B=\frac{10}{3}").next_to(t4, DOWN)
        t6 = Tex(r"Cách 2:").next_to(question, DOWN).shift(RIGHT *3)
        t7 = MathTex(r"\begin{split} S&=S_{\mathit{OMN}}-S_{\triangle{KMN}} \\ &=\int\limits_{0}^{4}\sqrt{x}\,\mathrm{d}x-\frac{1}{2}\cdot 2 \cdot 2 = \frac{10}{3} \end{split}").next_to(t6, DOWN) 

        self.add(question,ax,curve,line,labelx,labely,labelO,area,point1label,point2label,firstline,secondline,secondliney,point2labely,labelh1,labelh2,labelN,labelK,labelM,t1,h1,t2,t3,t4,t5,t6,t7)

FLAGS = f"-pqm"
SCENE = "vd7"

if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f'manim "{script_name}" {SCENE} {FLAGS}')
