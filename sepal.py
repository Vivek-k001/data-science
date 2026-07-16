import plotly.express as px

# Load the Iris dataset
df = px.data.iris()

# Create the scatter plot
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    hover_data=["petal_width"],
    title="Sepal Width vs Length"
)

# Display the plot
fig.show()
