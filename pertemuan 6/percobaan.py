import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))

st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)
 
st.title('Ini adalah contoh penggunaan title atau judul pada streamlit')

st.header('Ini adalah contoh penggunaan header pada streamlit')

st.subheader('Ini adalah contoh penggunaan subheader pada streamlit')

st.caption('Ini adalah contoh penggunaan caption pada streamlit')

code = """def hello():
    print("Ini adalah contoh penggunaan function code pada streamlit")"""
st.code(code, language='python')

st.text('Ini adalah contoh penggunaan text pada streamlit')

st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
 
st.dataframe(data=df, width=500, height=150)

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df)

st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)

number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)

if st.button('Say hello'):
    st.write('Hello there')

agree = st.checkbox('I agree')
 
if agree:
    st.write('Welcome to MyApp')

genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)

values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)


with st.sidebar:
    
    st.text('Ini merupakan sidebar')
    
    values = st.slider(
        label='Select a range of values',
        min_value=10, max_value=100, value=(0, 100)
    )
    st.write('Values:', values)

col1, col2, col3 = st.columns(3)
 
with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
 
with tab1:
    st.header("Tab 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with tab2:
    st.header("Tab 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with st.container():
    st.write("Inside the container")
    
    x = np.random.normal(15, 5, 250)
 
    fig, ax = plt.subplots()
    ax.hist(x=x, bins=15)
    st.pyplot(fig) 
 
st.write("Outside the container")


x = np.random.normal(15, 5, 250)
 
 
with st.expander("Ini judul expandernya"):
    st.write(
        """Ini text expandernya"""
    )