from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
import plotly.graph_objs as go
import plotly
plotly.offline.init_notebook_mode()
import plotly.graph_objs as go

df = datasets[0]

x_data = df["pipeline_change.category"]

trace0 = go.Bar(
    x=x_data,
    y=[0, df["pipeline_change.acv_metric"][0], df["pipeline_change.acv_metric"][0] + df["pipeline_change.acv_metric"][1], df["pipeline_change.acv_metric"][0] + df["pipeline_change.acv_metric"][1] + df["pipeline_change.acv_metric"][2], df["pipeline_change.acv_metric"][0] + df["pipeline_change.acv_metric"][1] + df["pipeline_change.acv_metric"][2] + df["pipeline_change.acv_metric"][3], df["pipeline_change.acv_metric"][0] + df["pipeline_change.acv_metric"][1] + df["pipeline_change.acv_metric"][2] + df["pipeline_change.acv_metric"][3] + df["pipeline_change.acv_metric"][4], 0],
    marker=dict(
        color='rgba(1,1,1, 0.0)',
    )
)

trace1 = go.Bar(
    x=x_data,
    y=df["pipeline_change.acv_metric"],
    marker=dict(
        color='#008000',
        line=dict(
            color='#008000',
            width=2,
        )
    )
)


data =[trace0, trace1]
layout = go.Layout(
    width=1200,
    height=480,
    barmode='stack',
    paper_bgcolor='rgba(245, 246, 249, 1)',
    plot_bgcolor='rgba(245, 246, 249, 1)',
    showlegend=False
)


fig = go.Figure(data=data, layout=layout)
iplot(fig)