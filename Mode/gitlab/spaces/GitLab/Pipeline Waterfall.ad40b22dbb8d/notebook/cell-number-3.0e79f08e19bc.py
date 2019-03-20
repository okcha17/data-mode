from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
import plotly.graph_objs as go
import plotly
plotly.offline.init_notebook_mode()
import plotly.graph_objs as go
import pandas as pd

df = datasets[1]

x_data = df["pipeline_change.category"]

total_y = [df["pipeline_change.acv_metric"][0],0,0,0,0,0,df["pipeline_change.acv_metric"][6]]
positive_y = [0,df["pipeline_change.acv_metric"][1],df["pipeline_change.acv_metric"][2],df["pipeline_change.acv_metric"][3],0,0,0]
negative_y = [0,0,0,0,df["pipeline_change.acv_metric"][4],df["pipeline_change.acv_metric"][5],0]
trace0 = go.Bar(
    x=x_data,
    y=[0, df["pipeline_change.acv_metric"][0], df["pipeline_change.acv_metric"][0] + df["pipeline_change.acv_metric"][1], df["pipeline_change.acv_metric"][0] + df["pipeline_change.acv_metric"][1] + df["pipeline_change.acv_metric"][2], df["pipeline_change.acv_metric"][0] + df["pipeline_change.acv_metric"][1] + df["pipeline_change.acv_metric"][2] + df["pipeline_change.acv_metric"][3], df["pipeline_change.acv_metric"][0] + df["pipeline_change.acv_metric"][1] + df["pipeline_change.acv_metric"][2] + df["pipeline_change.acv_metric"][3] + df["pipeline_change.acv_metric"][4], 0],
    marker=dict(
        color='rgba(1,1,1, 0.0)',
    )
)

Total = go.Bar(
    x=x_data,
    y=total_y,
    marker=dict(
        color='#3390FF',
        line=dict(
            color='#3390FF',
            width=2,
        )
    )
)

Positive = go.Bar(
    x=x_data,
    y=positive_y,
    marker=dict(
        color='#008000',
        line=dict(
            color='#008000',
            width=2,
        )
    )
)

Negative = go.Bar(
    x=x_data,
    y=negative_y,
    marker=dict(
        color='#FF4F33',
        line=dict(
            color='#FF4F33',
            width=2,
        )
    )
)

data =[trace0, Total,Positive, Negative]
layout = go.Layout(
    width=1200,
    height=480,
    barmode='stack',
    paper_bgcolor='rgba(245, 246, 249, 1)',
    plot_bgcolor='rgba(245, 246, 249, 1)',
    showlegend=False
)

y_data1 = [df["pipeline_change.acv_metric"][0]/2, df["pipeline_change.acv_metric"][0]/2 + df["pipeline_change.acv_metric"][1]/2, df["pipeline_change.acv_metric"][0]/2 + df["pipeline_change.acv_metric"][1]/2, 
df["pipeline_change.acv_metric"][0]/2 + df["pipeline_change.acv_metric"][1]/2, df["pipeline_change.acv_metric"][0]/2 + df["pipeline_change.acv_metric"][1]/2 + df["pipeline_change.acv_metric"][3]/2, df["pipeline_change.acv_metric"][0]/2 + df["pipeline_change.acv_metric"][1]/2, df["pipeline_change.acv_metric"][6]/2]    
y_data = [df["pipeline_change.acv_metric"][0]-30, df["pipeline_change.acv_metric"][0]-30 + df["pipeline_change.acv_metric"][1], df["pipeline_change.acv_metric"][0]-30 + df["pipeline_change.acv_metric"][1], 
df["pipeline_change.acv_metric"][0]-30 + df["pipeline_change.acv_metric"][1], df["pipeline_change.acv_metric"][0]-30 + df["pipeline_change.acv_metric"][1] + df["pipeline_change.acv_metric"][3], df["pipeline_change.acv_metric"][0]-30 + df["pipeline_change.acv_metric"][1], df["pipeline_change.acv_metric"][6]-30]
text =  '$' + df["pipeline_change.acv_metric"].astype(str)

annotations = []

for i in range(0, 7):
    annotations.append(dict(x=x_data[i], y=y_data1[i], text=text[i],
                                  font=dict(family='Arial', size=14,
                                  color='rgba(245, 246, 249, 1)'),
                                  showarrow=False,))
    layout['annotations'] = annotations

fig = go.Figure(data=data, layout=layout)
iplot(fig)