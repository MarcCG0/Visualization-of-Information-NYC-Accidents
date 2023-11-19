import altair as alt
import pandas as pd 
from colors import categorical_palette


df_V1 = pd.read_csv('../datasetsVisualizations/df_V1.csv')

weekday_bars = alt.Chart(df_V1).mark_bar().encode(
    x = alt.X('ACCIDENTS:Q', axis = None),
    y = alt.Y('WEEKDAY:O', axis = alt.Axis(title = None), sort = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']),
    color = alt.Color('DAY TYPE:N', legend = None, scale=alt.Scale(range=categorical_palette[2:4]))
).transform_filter(
    (alt.datum.WEEKDAY != 'Saturday') & (alt.datum.WEEKDAY != 'Sunday') & (alt.datum.YEAR == 2018)
)

weekday_rule = alt.Chart(df_V1).mark_rule(color = "red").encode(
    x = alt.X('mean(ACCIDENTS):Q', axis = alt.Axis(title = "Average Accident Count")),
).transform_filter(
    (alt.datum.WEEKDAY != 'Saturday') & (alt.datum.WEEKDAY != 'Sunday') & (alt.datum.YEAR == 2018)
)

weekend_bars = alt.Chart(df_V1).mark_bar().encode(
    x = alt.X('ACCIDENTS:Q', axis = alt.Axis(title = 'Accident Count and Average')),
    y = alt.Y('WEEKDAY:O', axis = alt.Axis(title = None), sort = ['Saturday', 'Sunday']),
    color = alt.Color('DAY TYPE:N', legend = None, scale=alt.Scale(range=categorical_palette[2:4]))
).transform_filter(
    ((alt.datum.WEEKDAY == 'Saturday') | (alt.datum.WEEKDAY == 'Sunday')) & (alt.datum.YEAR == 2018)
)

weekend_rule = alt.Chart(df_V1).mark_rule(color = "red").encode(
    x = alt.X('mean(ACCIDENTS):Q', axis = alt.Axis(title = ""))
).transform_filter(
    ((alt.datum.WEEKDAY == 'Saturday') | (alt.datum.WEEKDAY == 'Sunday')) & (alt.datum.YEAR == 2018)
)

accidents_nyc_before_covid = alt.vconcat(
    (weekday_bars + weekday_rule),
    (weekend_bars + weekend_rule)
).resolve_scale(
    x = 'shared'
).properties(
    title=alt.TitleParams(text = 'Accidents in NYC Before COVID-19 by Day', anchor = 'middle')
)

weekday_bars = alt.Chart(df_V1).mark_bar().encode(
    x = alt.X('ACCIDENTS:Q', axis = None),
    y = alt.Y('WEEKDAY:O', axis = alt.Axis(title = None), sort = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']),
    color = alt.Color('DAY TYPE:N', legend = None, scale=alt.Scale(range=categorical_palette[2:4]))
).transform_filter(
    (alt.datum.WEEKDAY != 'Saturday') & (alt.datum.WEEKDAY != 'Sunday') & (alt.datum.YEAR == 2020)
)

weekday_rule = alt.Chart(df_V1).mark_rule(color = "red").encode(
    x = alt.X('mean(ACCIDENTS):Q', axis = alt.Axis(title = "Average Accident Count")),
).transform_filter(
    (alt.datum.WEEKDAY != 'Saturday') & (alt.datum.WEEKDAY != 'Sunday') & (alt.datum.YEAR == 2020)
)

weekend_bars = alt.Chart(df_V1).mark_bar().encode(
    x = alt.X('ACCIDENTS:Q', axis = alt.Axis(title = 'Accident Count and Average')),
    y = alt.Y('WEEKDAY:O', axis = alt.Axis(title = None), sort = ['Saturday', 'Sunday']),
    color = alt.Color('DAY TYPE:N', legend = None, scale=alt.Scale(range=categorical_palette[2:4]))
).transform_filter(
    ((alt.datum.WEEKDAY == 'Saturday') | (alt.datum.WEEKDAY == 'Sunday')) & (alt.datum.YEAR == 2020)
)

weekend_rule = alt.Chart(df_V1).mark_rule(color = "red").encode(
    x = alt.X('mean(ACCIDENTS):Q', axis = alt.Axis(title = ""))
).transform_filter(
    ((alt.datum.WEEKDAY == 'Saturday') | (alt.datum.WEEKDAY == 'Sunday')) & (alt.datum.YEAR == 2020)
)

accidents_nyc_after_covid = alt.vconcat(
    (weekday_bars + weekday_rule),
    (weekend_bars + weekend_rule)
).resolve_scale(
    x = 'shared'
).properties(
    title=alt.TitleParams(text = 'Accidents in NYC After COVID-19 by Day', anchor = 'middle')
)

# Vertically concatenate the two charts
chart_V1 = alt.vconcat(
    accidents_nyc_before_covid,
    accidents_nyc_after_covid
).resolve_scale(
    color='independent',
    x = 'shared'
)
