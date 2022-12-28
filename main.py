
import streamlit as st
import time

st.title('Streamlit超入門')

st.write('show progress bar')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!'

# left_column, right_column = st.columns(2)

# if left_column.checkbox('show image'):
#     st.write('Display image')
#     img = Image.open('sample.png')
#     left_column.image(img, caption='this is a screen shot', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[10, 10]+[35.69, 139.79],
#     columns=['lat', 'lon']
# )
# st.map(df)

# option = right_column.selectbox(
#     'tell me your favorite number. ',
#     list(range(1, 11))
# )

# 'あなたが好きな数字は', option, 'です'

# expander = st.expander('query')
# expander.write('問い合わせ1')
# expander = st.expander('query')
# expander.write('問い合わせ2')
# expander = st.expander('query')
# expander.write('問い合わせ3')

# st.write('interactive widget')
# text = st.sidebar.text_input('tell me your hobby,')
# 'your favorite pastime is ', text, '.'

# condition = st.sidebar.slider('how is your energy level?', 0, 100, 50)
# 'your condition ', condition


# st.dataframe(df.style.highlight_max(axis=0))
# st.line_chart(df)
# st.area_chart(df)
# 静的フレームを作成する
# st.table(df)


"""
```python
import streamlit as st
import numpy as np
import pandas as pd
```
# this is a
## mark down
### system


"""
