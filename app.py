import streamlit as st
import pandas as pd
import numpy as np

st.title('Hello App!')
name = st.text_input('Enter your name:')
st.write('You entered: ', name)

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

df = pd.DataFrame({'Name': ['abc', 'xyz', 'pqr'], 'City': ['mumbai', 'delhi', 'pune']})
st.table(df)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)