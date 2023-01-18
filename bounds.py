import streamlit as st

st.header("Bounds on Probabilities of Causation")
st.subheader('Experimental Probabilities')
pyx = st.slider('$P(y_x)$', 0., 1., 0.5, step=0.01)
pyxp = st.slider('$P(y_{x\'})$', 0., 1., 0.5, step=0.01)
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

lb = max(0, pyx - pyxp, py - pyxp, pyx - py)
ub = min(pyx, pypxp, pxy + pxpyp, pyx - pyxp + pxyp + pxpy)
lb_doomed = pypxp - ub
ub_doomed = pypxp - lb
lb_harm = lb - ate
ub_harm = ub - ate
lb_immune = pyx - ub
ub_immune = pyx - lb
st.subheader('Bounds')
st.write(f'${lb_doomed:.2f} \\leqslant P(\\text{{doomed}}) \\leqslant {ub_doomed:.2f}$')
st.write(f'${lb:.2f} \\leqslant P(\\text{{benefit}}) \\leqslant {ub:.2f}$')
st.write(f'${lb_doomed:.2f} \\leqslant P(\\text{{harm}}) \\leqslant {ub_doomed:.2f}$')
st.write(f'${lb_immune:.2f} \\leqslant P(\\text{{immune}}) \\leqslant {ub_immune:.2f}$')
if pxy > pyx or pxy + pxp < pyx or pxpy > pyxp or pxpy + px < pyxp:
    st.warning('Experimental and observational data incompatible')
