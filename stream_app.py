'''
@Author: Ayur Ninawe
@Date: 08-09-2021
@Last Modified by: Ayur Ninawe
@Last Modified time: 08-09-2021
@Title : Program to plot static graph of predicted values using streamlit.
'''

from matplotlib.pyplot import colorbar, colormaps, fill, text, title
from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegressionModel
import streamlit as st
spark= SparkSession.builder.appName('Stock Data processing').getOrCreate()

model = LinearRegressionModel.load("stockModel")
data = spark.read.parquet("test_data")
prediction = model.transform(data)
output = prediction.toPandas()

import plotly.graph_objects as go
  
st.title("Stock Data Prediction Dashboard")
st.markdown("The dashboard is used for visualizing predicted stock data values")
st.sidebar.title("Select Visual Charts")
st.sidebar.markdown("For Now Only Line Chart is Available")
  
  
chart_visual = st.sidebar.selectbox('Select Charts/Plot type', 
                                    ('Line Chart', 'Bar Chart', 'Bubble Chart'))
  
st.sidebar.checkbox("Show Analysis by Smoking Status", True, key = 1)
selected_status = st.sidebar.selectbox('Select line chart',
                                       options = ['Line_Chart'])

fig = go.Figure()
  
if chart_visual == 'Line Chart':
    if selected_status == 'Line_Chart':
        fig.add_trace(go.Scatter(x = output.date, y = output.prediction,
                                 mode = 'lines',
                                 name = 'Predicted Data',
                                 line=dict(color='green')
                                 ))
        fig.add_trace(go.Scatter(x = output.date, y = output.Close,
                                 mode = 'lines',
                                 name = 'Actual Data',
                                 line=dict(color='royalblue')
                                 ))

fig.update_layout(title='Stock Price Prediction',
                font_family="sans-serif",
                title_font_family="Times New Roman",
                title_font_color="darkslategray",
                title_font_size=30,
                legend_title_font_color="green",
                  title_x=0.4,
                   xaxis_title='Date',
                   yaxis_title='Stock Price (closing)')
  
st.plotly_chart(fig, use_container_width=True)