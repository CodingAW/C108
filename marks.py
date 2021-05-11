import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data5.csv")
fig = ff.create_distplot([df["Math_score"].tolist()], ["Math_score"], show_hist=False)
fig.show()