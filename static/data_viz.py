import plotly.express as px

# load weather data
df = pd.read_csv('weather_data.csv')

# Create a line plot for temperature trends
fig = px.line(df, x='Date', y='Temperature', title='Temperature Trends')
fig.show()

# Create a bar plot for rainfall
fig=px.bar(df, x='Date', y='Rainfall', title='Rainfall')
fig.show()