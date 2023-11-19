import geopandas as gpd 
import altair as alt 
import pandas as pd 


df_V4 = pd.read_csv('datasetsVisualizations/df_V4.csv')
url_geojson = "https://raw.githubusercontent.com/fedhere/PUI2015_EC/master/mam1612_EC/nyc-zip-code-tabulation-areas-polygons.geojson"
data_url_geojson = alt.Data(url=url_geojson, format=alt.DataFormat(property="features"))

tooltip_names = {'properties.postalCode': 'Zip Code', 'properties.borough': 'Borough', 'ACCIDENTS': 'Accidents'}

chart_V4 = alt.Chart(data_url_geojson).mark_geoshape().encode(
    color=alt.Color('ACCIDENTS:Q', scale=alt.Scale(scheme='oranges'), legend = alt.Legend(title = 'Accidents')),
    tooltip = [alt.Tooltip(field=name, title = tooltip_names[name]) for name in ['properties.postalCode', 'properties.borough', 'ACCIDENTS']]
).transform_lookup(
    lookup='properties.postalCode',
    from_=alt.LookupData(df_V4, 'ZIP CODE', ['ACCIDENTS']) # join amb 'name' i 'borough' i agafem valor d'accidents.
).properties(
    width=500, height=300
).properties(title = 'Accidents in NYC by Zip Code Area')

