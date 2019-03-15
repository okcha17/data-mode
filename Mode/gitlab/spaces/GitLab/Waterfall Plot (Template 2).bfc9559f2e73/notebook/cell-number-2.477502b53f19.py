from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
import plotly.graph_objs as go
import plotly
plotly.offline.init_notebook_mode()
import plotly.graph_objs as go

df = datasets[0]

x_data = df.category
y_data = [df.value[0]-30, df.value[0]-30 + df.value[1], df.value[0]-30 + df.value[1], 
df.value[0]-30 + df.value[1], df.value[0]-30 + df.value[1] + df.value[3], df.value[0]-30 + df.value[1], df.value[6]-30]
text = df.text

# Base
trace0 = go.Bar(
    x=x_data,
    y=[0, df.value[0], 0, df.value[2] + df.value[3], df.value[2] + df.value[3] + df.value[4], df.value[2] + df.value[3] + df.value[4], 0],
    marker=dict(
        color='rgba(1,1,1, 0.0)',
    )
)
# Revenue
trace1 = go.Bar(
    x=x_data,
    y=df.revenue_y,
    marker=dict(
        color='#008000',
        line=dict(
            color='#008000',
            width=2,
        )
    )
)
# Costs
trace2 = go.Bar(
    x=x_data,
    y=df.cost_y,
    marker=dict(
        color='#800000',
        line=dict(
            color='#800000',
            width=2,
        )
    )
)
# Profit
trace3 = go.Bar(
    x=x_data,
    y=df.total_y,
    marker=dict(
        color='#008000',
        line=dict(
            color='#008000',
            width=2,
        )
    )
)
data = [trace0, trace1, trace2, trace3]
layout = go.Layout(
    width=1200,
    height=480,
    barmode='stack',
    paper_bgcolor='rgba(245, 246, 249, 1)',
    plot_bgcolor='rgba(245, 246, 249, 1)',
    showlegend=False
)

annotations = []

for i in range(0, 7):
    annotations.append(dict(x=x_data[i], y=y_data[i], text=text[i],
                                  font=dict(family='Arial', size=14,
                                  color='rgba(245, 246, 249, 1)'),
                                  showarrow=False,))
    layout['annotations'] = annotations

fig = go.Figure(data=data, layout=layout)
iplot(fig)