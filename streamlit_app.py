
import streamlit as st
import pandas as pd
import numpy as np

import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly import tools



"""
# Welcome to Streamlit Example Covid cases worldmap!

The code is deployed via Streamlit Cloud
Explaining of the world map graphic can be found in the
Udemy lecture: https://bit.ly/3sM0cYR
"""

# GET DATA
url="https://covid.ourworldindata.org/data/owid-covid-data.csv"
df_country_info=pd.read_csv(url,sep=',')


# cut out the last day with data
df_country_info_day=df_country_info[df_country_info['date']==max(df_country_info['date'])]

## Visualize something
#visualize_col='total_vaccinations_per_hundred'
visualize_col='total_cases in %'

my_z=df_country_info_day['total_cases_per_million']/10000

fig = go.Figure(go.Choropleth(
                    locations = df_country_info_day['iso_code'],
                    z = my_z, # norm to percent
                    text = df_country_info_day['location'],
                    colorscale = 'Blues',
                    autocolorscale=False,
                    reversescale=False,
                    marker_line_color='darkgray',
                    marker_line_width=0.5,
                    colorbar_title = visualize_col,
                    ))

# Beatify the graph_objects

fig.update_layout(
    #width=1200, height=900,
    title_text='COVID-19 Total cases in %',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Data Source: <a href="https://github.com/owid/covid-19-data/tree/master/public/data/">\
            Our World in Data</a>',
        showarrow = False
    )]
)



# Plot!
st.plotly_chart(fig, use_container_width=True)
