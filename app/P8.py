import altair as alt 
import pandas as pd 


df_V8_normalized = pd.read_csv('datasetsVisualizations/df_V8_normalized.csv')

chart_V8 = alt.Chart(df_V8_normalized).mark_bar().encode(
    x = alt.X('NORMALIZED AFFECTED:Q', title = "Proportion of severity"),
    y = alt.X('TIME OF DAY:N',  sort = ['Night', 'Morning', 'Afternoon', 'Evening'], title = "Period of day"), 
    color = alt.value('#ffb55a')
).properties(
    title = ("Severity of accidents in function of the period of the day")
)