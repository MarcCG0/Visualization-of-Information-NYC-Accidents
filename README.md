# Visualization of Information: NYC Accidents

## Introduction
This project aims to create a static visualization of collision data in New York City, specifically during the summers of 2018 and 2020. The goal is to analyze various aspects of these accidents, such as their frequency, involved vehicle types, timing, geographical distribution, and any correlation with weather conditions.

## Data
The project utilizes a collisions dataset for the specified period, alongside additional data such as weather conditions and a map of New York City. Data sources include:

- Collisions dataset (June-September 2018 and 2020)
- Weather dataset
- NYC map

## Data Processing
Data cleaning and processing were conducted using OpenRefine and Pandas in Python. The process involved filtering, cleaning, and deriving necessary data to answer the project's questions. Detailed steps and code are available in the associated Google Colab document.

## Design and Implementation
The visualization design process, tested and refined through multiple iterations, is documented in the Google Colab file. The final multi-view visualization is built using Altair and integrated into a Streamlit application. Various types of charts, like bar charts, heat maps, and choropleth maps,... were employed to present the data effectively.

## How to Run
To run the Streamlit application:

1. Ensure you have Python, Streamlit, Pandas and Altair installed.
2. Clone this repository.
3. Navigate to the app directory.
4. Run `streamlit run app.py`.

## Authors
- Ignacio Gris Martín
- Marc Camps Garreta
