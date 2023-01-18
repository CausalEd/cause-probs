import streamlit as st

st.header("Bounds on Probabilities of Causation")
st.subheader('Experimental Probabilities')
pyx = st.slider('$P(y_x)$', 0., 1.)
pyxp = st.slider('$P(y_{x\'})$', 0., 1., 0.05)
st.subheader('Observational Probabilities')
px = st.slider('$P(x)$', 0., 1., 0.005)
pycx = st.slider('$P(y|x)$', 0., 1., 0.05)
pycxp = st.slider('$P(y|{x\'})$', 0., 1., 0.05)

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
st.subheader('Bounds')
st.write(f'${pypxp - lb:.2f} \\leqslant P(\\text{{doomed}}) \\leqslant {pypxp - ub:.2f}$')
st.write(f'${lb:.2f} \\leqslant P(\\text{{benefit}}) \\leqslant {ub:.2f}$')
st.write(f'${lb - ate:.2f} \\leqslant P(\\text{{harm}}) \\leqslant {ub - ate:.2f}$')
st.write(f'${pyx - lb:.2f} \\leqslant P(\\text{{immune}}) \\leqslant {pyx - ub:.2f}$')
