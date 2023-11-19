import altair as alt 
import pandas as pd

df_V5 = pd.read_csv('datasetsVisualizations/df_V5.csv')

degree_order = ['LOW', 'MEDIUM', 'HIGH']

chart_V5 = alt.Chart(df_V5).mark_rect().encode(
    x=alt.X('Degree:N', title='Degree', sort = degree_order),
    y=alt.Y('Measure:N', title='Weather condition'),
    color=alt.Color('Count proportion',scale=alt.Scale(scheme='oranges')),
    tooltip = ['Count proportion', 'Degree', 'Measure']
).properties(
    width=400,
    height=300
).properties(
    title='Weather conditions relevance on quantity of accidents'
)

