import altair as alt 
import pandas as pd 


df_V3 = pd.read_csv('../datasetsVisualizations/df_V3.csv')


# HORIZON PLOT FOR ACCIDENTS PER HOUR IN 2018

base_18 = alt.Chart(df_V3).mark_area(
    clip = True,
    interpolate = 'monotone'
).encode(
    alt.X('CRASH TIME:O').title('Hour').axis(labelAngle = 0),
    alt.Y('ACCIDENTS:Q').scale(domain = [0, 2000]).title('Accidents'),
    opacity = alt.value(0.5),
    color = alt.Color('Thousands:O', scale = alt.Scale(scheme = 'oranges'))
).transform_filter(
    alt.datum.YEAR == 2018
).transform_calculate(
    Thousands = '2'
).properties(
    width = 500,
    height = 100
)

base_18_2 = base_18.encode(
    alt.Y('ACCIDENTS2:Q').scale(domain = [0, 2000])
).transform_calculate(
    'ACCIDENTS2', alt.datum.ACCIDENTS - 2000,
    Thousands = '4'
)

base_18_3 = base_18.encode(
    alt.Y('ACCIDENTS3:Q').scale(domain = [0, 2000]),
).transform_calculate(
    'ACCIDENTS3', alt.datum.ACCIDENTS - 4000,
    Thousands = '6'
)

# HORIZON PLOT FOR ACCIDENTS PER HOUR IN 2020

base_20 = alt.Chart(df_V3).mark_area(
    clip = True,
    interpolate = 'monotone'
).encode(
    alt.X('CRASH TIME:O').title('Hour').axis(labelAngle = 0),
    alt.Y('ACCIDENTS:Q').scale(domain = [0, 2000]).title('Accidents'),
    opacity = alt.value(0.5),
    color = alt.Color('Thousands:O', scale = alt.Scale(scheme = 'oranges'))
).transform_filter(
    alt.datum.YEAR == 2020
).transform_calculate(
    Thousands = '2'
).properties(
    width = 500,
    height = 100
)

base_20_2 = base_20.encode(
    alt.Y('ACCIDENTS2:Q').scale(domain = [0, 2000])
).transform_calculate(
    'ACCIDENTS2', alt.datum.ACCIDENTS - 2000,
    Thousands = '4'
)

# HORIZON PLOT FOR ACCIDENTS PER HOUR IN 2020

base_20 = alt.Chart(df_V3).mark_area(
    clip = True,
    interpolate = 'monotone'
).encode(
    alt.X('CRASH TIME:O').title('Hour').axis(labelAngle = 0),
    alt.Y('ACCIDENTS:Q').scale(domain = [0, 2000]).title('Accidents'),
    opacity = alt.value(0.5),
    color = alt.Color('Thousands:O', scale = alt.Scale(scheme = 'oranges'))
).transform_filter(
    alt.datum.YEAR == 2020
).transform_calculate(
    Thousands = '2'
).properties(
    width = 500,
    height = 100
)

base_20_2 = base_20.encode(
    alt.Y('ACCIDENTS2:Q').scale(domain = [0, 2000])
).transform_calculate(
    'ACCIDENTS2', alt.datum.ACCIDENTS - 2000,
    Thousands = '4'
)


# First supperposed chart
hour_distribution_2018 = (
    base_18 +
    base_18_2 +
    base_18_3
).resolve_scale(
    x = 'shared'
).properties(
    title=alt.TitleParams(text = 'Accidents in NYC After COVID-19 by Hour', anchor = 'middle')
)

# Second supperposed chart
hour_distribution_2020 = (
    base_20 +
    base_20_2
).resolve_scale(
    x = 'shared'
).properties(
    title=alt.TitleParams(text = 'Accidents in NYC After COVID-19 by Hour', anchor = 'middle')
)

# Vertically concatenate the two charts
chart_V3 = alt.vconcat(
    hour_distribution_2018,
    hour_distribution_2020
).resolve_scale(
    color='independent',
    x = 'shared'
)

