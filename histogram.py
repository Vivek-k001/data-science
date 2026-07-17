import plotly.express as px
df=px.data.tips()
fig=px.histogram(df,x="total_bill",color="sex",nbins=30,marginal="rug",
title="distribution of total bils by gender")
fig.show()
