"""


13:17 - 15-01-2023
"""

def render_mathplot():
    import matplotlib.pyplot as plt
    a = '\\frac{a}{b}'  #notice escaped slash
    plt.plot()
    plt.text(0.5, 0.5,'$%s$'%a)
    plt.show()

def render_latex():
    from IPython.display import display, Latex
    for i in range(3):
        display(Latex(f'$x_{i}$'))

render_latex()

# https://problemsolvingwithpython.com/99-Appendix/99.06-LaTeX-Math/
# https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html

def render_sympy():
    from sympy.interactive import printing
    from IPython.display import display, Math
    printing.init_printing(use_latex=True)
    import sympy as sp
    func = sp.Function('func')
    x = sp.Symbol('x')

    func = sp.sin(x)
    inte = sp.Integral(func, x)
    display(inte)

render_sympy()


import sympy as sym
from IPython.display import display

x, a, b = sym.symbols('x a b')
func = (a*x**b)/(a+b)

display(func)
'''
$
\begin{align}
\lim_{x\to0} \frac{\sin{x}}{x} = 1
\end{align}
$
'''