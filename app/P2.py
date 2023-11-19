import altair as alt 
import pandas as pd
from colors import categorical_palette

df_V2 = pd.read_csv('datasetsVisualizations/df_V2.csv')

chart_V2 = alt.Chart(df_V2).mark_bar().encode(
    alt.X('ACCIDENTS:Q', axis = alt.Axis(title = 'Accidents')),
    alt.Y('VEHICLE TYPE:N', sort = alt.EncodingSortField(field = 'ACCIDENTS', order = 'descending'), axis = alt.Axis(title = 'Vehicle Type')),
    color = alt.Color('YEAR:N', scale=alt.Scale(range=categorical_palette), legend = alt.Legend(title = 'Year'))
).properties(title = 'Accidents in NYC by Vehicle Type')

