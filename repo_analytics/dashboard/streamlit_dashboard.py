import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 示例数据
data = {
    'Category': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'Value': [10, 20, 15, 25, 30, 35, 40, 45, 50]
}
df = pd.DataFrame(data)

# 标题
st.title('数据过滤和可视化应用')

# 过滤器
selected_category = st.selectbox('选择分类', df['Category'].unique())
filtered_df = df[df['Category'] == selected_category]

# 展示过滤后的数据
st.write('过滤后的数据', filtered_df)

# 绘制直方图
st.subheader('直方图')
fig, ax = plt.subplots()
sns.histplot(filtered_df['Value'], bins=10, kde=True, ax=ax)
st.pyplot(fig)

# 绘制折线图
st.subheader('折线图')
fig, ax = plt.subplots()
sns.lineplot(data=filtered_df, x='Category', y='Value', ax=ax)
st.pyplot(fig)

# 绘制条形图
st.subheader('条形图')
fig, ax = plt.subplots()
sns.barplot(data=filtered_df, x='Category', y='Value', ax=ax)
st.pyplot(fig)

# 绘制散点图
st.subheader('散点图')
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_df, x='Category', y='Value', ax=ax)
st.pyplot(fig)
