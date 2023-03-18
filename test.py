import plotly.express as px
import pandas as pd

# Define the data
country = ['Brazil', 'US', 'IT']
rates = [13, 45, 67]

# Create a dataframe with the data
data = {'Country': country, 'Rate': rates}
df = pd.DataFrame(data)

# Load the country codes dataset
country_codes = px.data.gapminder().query("year == 2007")[["country", "iso_alpha"]]

# Merge the data with the country codes dataset
merged_df = pd.merge(df, country_codes, left_on="Country", right_on="iso_alpha")

# Create a choropleth map
fig = px.choropleth(merged_df, locations="Country", color="Rate", hover_name="Country",
                    projection="natural earth")

# Show the map
fig.show()
