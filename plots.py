import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = np.random.randn(20,3)
d = pd.DataFrame(data, columns = ["l1","l2","l3"])

st.header("1 - CHARTS WITH RANDOM NUMBERS")
st.subheader("1.1 - LINE CHART")
st.line_chart(d)

st.subheader("1.2 - AREA CHART")
st.area_chart(d)

st.subheader("1.3 - BAR CHART")
st.bar_chart(d)

st.header("2 - DATA VISUALIZATION WITH MATPLOTLIB AND SEABORN")
st.subheader("2.1 - Loading the DataFrame")
df = pd.read_csv(r"C:\Users\Chary Mattela\Desktop\Python\STREAMLIT\iris.csv")
st.dataframe(df)

st.subheader("2.2 -  BarGraph with Matplotlib")
fig = plt.figure(figsize = (15,8))
df["species"].value_counts().plot(kind = "bar")
st.pyplot(fig)

st.subheader("2.3 -  Distribution Plot with Seaborn")
fig = plt.figure(figsize = (15,8))
sns.distplot(df["sepal_length"])
st.pyplot(fig)

st.header("3 - Multiple Graphs in columns")
col1, col2 = st.columns(2)

with col1:
    col1.header = "KDE = FALSE"
    fig = plt.figure(figsize = (5,5))
    sns.distplot(df["sepal_length"], kde = True)
    st.pyplot(fig)
    
with col2:
    col1.header = "HIST = FALSE"
    fig = plt.figure(figsize = (5,5))
    sns.distplot(df["sepal_length"], hist = False)
    st.pyplot(fig)

st.header("4 -  DIFFERENT STYLES OF PLOTS")
col1, col2 = st.columns(2)

with col1:
    fig = plt.figure(figsize = (5,5))
    sns.set_style("darkgrid")
    sns.set_context("notebook")
    sns.distplot(df["petal_length"], hist = False)
    st.pyplot(fig)
    
with col2:
    fig = plt.figure(figsize = (5,5))
    sns.set_theme(context = "poster", style = "darkgrid")
    sns.distplot(df["petal_length"], hist = False)
    st.pyplot(fig)

st.header("5 - EXPLORING DIFFERENT GRAPHS")
st.subheader("5.1 - Scatter Plot")
fig,ax = plt.subplots(figsize = (15,8))
ax.scatter(*np.random.random(size = (2,100)))
st.pyplot(fig)           

st.subheader("5.2 - Count-Plot")
fig = plt.figure()
sns.countplot(data = df, x = "species")
st.pyplot(fig)

st.subheader("5.3 - Box-Plot")
fig = plt.figure()
sns.boxplot(data = df, x = "species", y = "petal_length")
st.pyplot(fig)

st.subheader("5.4 - Violin-Plot")
fig = plt.figure()
sns.violinplot(data = df, x = "species", y = "petal_length")
st.pyplot(fig)










































    
    
