import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('Interactive Wodgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('aaa')
expander.write('bbb')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'あなたのコンディション： ', condition


text = st.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味： ', text

option = st.selectbox(
    'あなたが好きな数字を教えて下さい',
    list(range(1, 11))
)

'あなたが好きな数字は、', option, 'です。'

