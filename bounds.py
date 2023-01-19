import math
import streamlit as st

def less_equal(x, y):
    return x < y or math.isclose(x, y)
def greater(x, y):
    return x > y and not math.isclose(x, y)

st.set_page_config(layout = 'wide')

st.header("Bounds on Probabilities of Causation")
col1, col2 = st.columns(2)

with col1:
    # pyx = P(yₓ), pyxp = P(yₓ')
    st.subheader('Experimental Probabilities')
    pyx = st.slider('$P(y_x)$', 0., 1., 0.5, step=0.01)
    pyxp = st.slider('$P(y_{x\'})$', 0., 1., 0.5, step=0.01)
with col2:
    # px = P(x), pycx = P(y|x), pycxp = P(y|x')
    st.subheader('Observational Probabilities')
    px = st.slider('$P(x)$', 0., 1., 0.5, step=0.01)
    pycx = st.slider('$P(y|x)$', 0., 1., 0.5, step=0.01)
    pycxp = st.slider('$P(y|{x\'})$', 0., 1., 0.5, step=0.01)

ate = pyx - pyxp

pypxp = 1 - pyxp
pxp = 1 - px
pypcx = 1 - pycx
pypcxp = 1 - pycxp

pxy = pycx * px
pxyp = pypcx * px
pxpy = pycxp * pxp
pxpyp = pypcxp * pxp
py = pxy + pxpy

incompatible = greater(pxy, pyx) or greater(pyx, pxy + pxp) or greater(pxpy, pyxp) or greater(pyxp, pxpy + px)
if incompatible:
    st.image('red-alert-icon.png', width = 100)
    st.header(':fire: Danger: Experimental & Observational Probabilities Incompatible! :fire:')

# lb and ub are lower and upper bounds of P(benefit)
lb = max(0, pyx - pyxp, py - pyxp, pyx - py)
ub = min(pyx, pypxp, pxy + pxpyp, pyx - pyxp + pxyp + pxpy)
lb_doomed = pypxp - ub
ub_doomed = pypxp - lb
lb_harm = lb - ate
ub_harm = ub - ate
lb_immune = pyx - ub
ub_immune = pyx - lb

st.subheader('Bounds')
st.markdown(f'${lb_doomed:.2f} \\leqslant P(\\text{{doomed}}) \\leqslant {ub_doomed:.2f}$  \n'
f'${lb:.2f} \\leqslant P(\\text{{benefit}}) \\leqslant {ub:.2f}$  \n'
f'${lb_doomed:.2f} \\leqslant P(\\text{{harm}}) \\leqslant {ub_doomed:.2f}$  \n'
f'${lb_immune:.2f} \\leqslant P(\\text{{immune}}) \\leqslant {ub_immune:.2f}$')
if incompatible:
    st.warning('Experimental and observational data incompatible', icon = '🚨')
