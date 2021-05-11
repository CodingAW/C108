import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

df = pd.read_csv("data6.csv")
# fig = ff.create_distplot([df["quant_saved"].tolist()], ["quant_saved"], show_hist=False)
# fig = px.scatter(df, x="quant_saved", y="female")
fig = px.bar(df, x="female", y="quant_saved")
fig.show()
