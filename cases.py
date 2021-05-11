import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data4.csv")
fig = ff.create_distplot([df["cases"].tolist()], ["cases"], show_hist=False)
fig.show()