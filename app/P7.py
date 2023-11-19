import altair as alt  
import pandas as pd 


df_V7_accidents = pd.read_csv('../datasetsVisualizations/df_V7_accidents.csv')
df_V7_people = pd.read_csv('../datasetsVisualizations/df_V7_people.csv')
df_V7_comb = pd.read_csv('../datasetsVisualizations/df_V7_comb.csv')
df_V7_background = pd.read_csv('../datasetsVisualizations/df_V7_background.csv')


chart_V1_accidents = alt.Chart(df_V7_accidents).mark_bar().encode(
    alt.X('COMBINATION:N', axis = None, sort = alt.EncodingSortField(field = 'ACCIDENTS', order = 'descending')),
    alt.Y('ACCIDENTS:Q', axis = alt.Axis(title = 'Accidents')),
    color = alt.value('#ffb55a')
).properties(height = 80)

chart_V1_comb = alt.Chart(df_V7_comb).mark_line(point = True, size = 2).encode(
    alt.Y('CATEGORY:N', sort = ['Pedestrians Injured', 'Pedestrians Killed', 'Motorists Injured', 'Motorists Killed'], axis = alt.Axis(title = None)),
    alt.X('COMBINATION:N', axis = None, sort = ['0011', '0110', '0010', '1100', '1000', ]),
    detail = 'COMBINATION:N',
    color = alt.value('#ffb55a')
)

chart_V1_background = alt.Chart(df_V7_background).mark_point(filled = True, point = True, size = 40, color = 'grey').encode(
    alt.Y('CATEGORY:N', sort = ['Pedestrians Injured', 'Pedestrians Killed', 'Motorists Injured', 'Motorists Killed']),
    alt.X('COMBINATION:N', axis = None, sort = ['0011', '0110', '0010', '1100', '1000', '1001'])
)

chart_V1_people = alt.Chart(df_V7_people).mark_bar().encode(
    alt.X('PEOPLE:Q', axis = alt.Axis(title = 'People')),
    alt.Y('CATEGORY', sort = ['Pedestrians Injured', 'Pedestrians Killed', 'Motorists Injured', 'Motorists Killed'], axis = None),
    color = alt.value('#ffb55a')
).properties(width = 204)

chart_V7 = (chart_V1_accidents & ((chart_V1_background + chart_V1_comb) | chart_V1_people)).properties(title = 'Accidents and People Distribution in NYC by injure fatality and type of person')


