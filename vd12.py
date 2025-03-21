import os
from pathlib import Path
from manim import *
class vd12(Scene):
    def construct(self):
        # Set global LaTeX preamble for Vietnamese support
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"""
            \usepackage[utf8]{vietnam}
            \usepackage[left=3cm,right=3cm,top=2cm,bottom=2cm]{geometry}
        """)
        Tex.set_default(tex_template=tex_template, font_size=30, tex_environment="flushleft")
        MathTex.set_default(tex_template=tex_template, font_size=30)

        question = Tex(r"Ví dụ 12: Cho đường tròn \((C):(x-1)^2+(y+1)^2=4\). Từ \(A(1;3)\) kẻ được 2 tiếp tuyến \((d_1),(d_2)\) tới đường tròn. Diện tích hình phẳng được giới hạn bởi đường tròn và 2 tiếp tuyến là (kết quả làm tròn đến chữ số hàng phần chục):").to_corner(UL, buff=0.3)
    
        ax = Axes(
            x_range=[-3,5,1],
            x_length = 8,
            y_range=[-5,5,1],
            y_length = 10,
            axis_config={"tip_shape": StealthTip,
                         "font_size": 16,
                         "tip_width": 0.15,
                         "tip_height": 0.15,
                         "include_ticks": False,
                         }            
        ).scale(0.5).to_edge(RIGHT).shift(DOWN *0.5)
        labelx = MathTex(r"x").next_to(ax.x_axis.get_end(), DOWN, buff=0.1)
        labely = MathTex(r"y").next_to(ax.y_axis.get_end(), RIGHT, buff=0.1)
        labelO = MathTex(r"O").next_to(ax.c2p(0, 0), DL, buff=0.1)
        circleup = ax.plot(lambda x: -1+np.sqrt(4-(x-1)**2), x_range=[-1,3,0.01])
        circledown = ax.plot(lambda x: -1-np.sqrt(4-(x-1)**2), x_range=[-1,3,0.01])
        center = Dot(ax.c2p(1,-1)).scale(0.5)
        centerlabel = MathTex(r"I(1;-1)", font_size=20).next_to(center, DR, buff=0.1)
        line1 = ax.plot(lambda x: np.sqrt(3)*x+3-np.sqrt(3), x_range=[-3,3,0.01])
        line2 = ax.plot(lambda x: -np.sqrt(3)*x+3+np.sqrt(3), x_range=[-1,5,0.01])
        pointc = Dot(ax.c2p(1+np.sqrt(3),0)).scale(0.5)
        pointd = Dot(ax.c2p(1-np.sqrt(3),0)).scale(0.5)
        labelc = MathTex("C").next_to(pointc, UR, buff=0.1)
        labeld = MathTex("D").next_to(pointd, UL, buff=0.1)
        pointa = Dot(ax.c2p(1,3)).scale(0.5)
        labela = MathTex(r"A(1;3)").next_to(pointa, RIGHT *0.5)
        labelline1 = MathTex(r"(d_1)").next_to(line1.get_start(), RIGHT *0.5)
        labelline2 = MathTex(r"(d_2)").next_to(line2.get_end(), LEFT *0.5)
        linemid = Line(ax.c2p(1,3),ax.c2p(1,-3))
        area1 = ax.get_area(graph=line1, bounded_graph=circleup, x_range=[1-np.sqrt(3),1], color=RED)
        area2 = ax.get_area(graph=line2, bounded_graph=circleup, x_range=[1,1+np.sqrt(3)], color=RED)
        t1 = Tex(r"Phương trình tiếp tuyến của đường tròn đi qua điểm \(A(1;3)\) có dạng:").next_to(question, DOWN).to_edge(LEFT, buff=0.3)
        t2 = MathTex(r"a(x-1)+b(y-3)=0 \, (d)").next_to(t1, DOWN, aligned_edge=LEFT, buff=0.1)
        t3 = MathTex(r"d(I;d)=R=2 \Leftrightarrow \frac{|-4b|}{\sqrt{a^2+b^2}}=2 \Leftrightarrow a=\pm\sqrt{3}b").next_to(t2, DOWN, aligned_edge=LEFT, buff=0.1)
        t4 = Tex(r"Hai tiếp tuyến có phương trình là:").next_to(t3, DOWN, aligned_edge=LEFT, buff=0.1)
        t5 = MathTex(r"\begin{cases} -\sqrt{3}(x-1)+1(y-3)=0 \, (d_1) \\ \sqrt{3}(x-1)+1(y-3)=0 \, (d_2) \end{cases}\Leftrightarrow \begin{cases} y=\sqrt{3}x+3-\sqrt{3} \, (d_1) \\ y=-\sqrt{3}(x-1)+3+\sqrt{3} \, (d_2) \end{cases}").next_to(t4, DOWN, aligned_edge=LEFT, buff=0.1)
        t6 = Tex(r"Gọi \(S\) là diện tích cần tìm, \(S_1\) là diện tích hình phẳng giới hạn bởi \((d_1)\), cung nhỏ \(\mathit{CD}\) và đường thẳng \(x=1\)").next_to(t5, DOWN, aligned_edge=LEFT, buff=0.1)
        t7 = MathTex(r"(x-1)^2+(y+1)^2=4 \Leftrightarrow y+1=\pm\sqrt{4-(x-1)^2}").next_to(t6, DOWN, aligned_edge=LEFT, buff=0.1)
        t8 = Tex(r"\(\Rightarrow y=-1+\sqrt{4-(x-1)^2}\) là phương trình của cung nhỏ \(\mathit{CD}\) (do cung nằm trên đường thẳng \(y=-1\))").next_to(t7, DOWN, aligned_edge=LEFT, buff=0.1)
        t9 = Tex(r"Xét hệ phương trình:").next_to(t8, DOWN, aligned_edge=LEFT, buff=0.1)
        t10 = MathTex(r"\begin{cases} y=-1+\sqrt{4-(x-1)^2} \\ y=\sqrt{3}x+3-\sqrt{3} \end{cases} \Leftrightarrow \begin{cases} x=1-\sqrt{3} \\ y=0 \end{cases} \Rightarrow D(1-\sqrt{3};0)").next_to(t9, DOWN, aligned_edge=LEFT, buff=0.1)
        t11 = MathTex(r"\Rightarrow S=2S_1=2\int\limits_{1-\sqrt{3}}^{1}[\sqrt{3}x+3-\sqrt{3}-(-1+\sqrt{4-(x-1)^2})\,\mathrm{d}x \approx 2,74").next_to(t10, DOWN, aligned_edge=LEFT, buff=0.1)

        self.add(question,ax,labelx,labely,labelO,circleup,circledown,center,centerlabel,line1,line2,pointc,pointd,labelc,labeld,pointa,labela,labelline1,labelline2,linemid,area1,area2,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11)
FLAGS = f"-pqm"
SCENE = "vd12"

if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
