import streamlit as st
import altair as alt
import pandas as pd  # Assuming you have data in a Pandas DataFrame
import geopandas as gpd

# Load dataframes
import altair as alt
import pandas as pd
from P1 import chart_V1
from P2 import chart_V2
from P3 import chart_V3
from P4 import chart_V4
from P5 import chart_V5
from P6 import chart_V6
from P7 import chart_V7
from P8 import chart_V8

col1 = alt.vconcat(chart_V1, chart_V7).resolve_scale(color='independent', size='independent').resolve_legend(color='independent', size='independent')
col2 = alt.vconcat(chart_V3, chart_V4, chart_V5).resolve_scale(color='independent', size='independent').resolve_legend(color='independent', size='independent')
col3 = alt.vconcat(chart_V2, chart_V6, chart_V8).resolve_scale(color='independent', size='independent').resolve_legend(color='independent', size='independent')

final = alt.hconcat(col1, col2, col3).resolve_scale(color='independent', size='independent').resolve_legend(color='independent', size='independent')

st.altair_chart(final, use_container_width=True)
