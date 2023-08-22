# TRENDSCAPE

## Google Trends Analysis

This document outlines a Python script designed to analyze Google Trends data. The script employs various libraries to offer insights into the trends and popularity of user-specified keywords within a defined time frame. Here's a breakdown of the script's functionality:

## Table of Contents
- [Libraries](#libraries)
- [Google Trends Setup](#google-trends-setup)
- [User Input](#user-input)
- [Fetching Data](#fetching-data)
- [Plotting Trends](#plotting-trends)
- [Percentage Changes](#percentage-changes)
- [Results](#results)

## Libraries <a name="libraries"></a>
The script starts by importing essential libraries: `TrendReq` from `pytrends.request`, `matplotlib.pyplot`, `pandas`, and `plotly.graph_objects`.

## Google Trends Setup <a name="google-trends-setup"></a>
The Google Trends API is initialized with parameters like language (`hl`), time zone (`tz`), and other settings.

## User Input <a name="user-input"></a>
The script prompts users to input the number of keywords they want to analyze (up to 25) and collects these keywords in a list.

## Fetching Data <a name="fetching-data"></a>
Using the provided keywords, the script builds a payload and retrieves Google Trends data for the last 5 years (`timeframe='today 5-y'`) without geographical or property filters.

## Plotting Trends <a name="plotting-trends"></a>
The `plot_interest_over_time` function utilizes `plotly.graph_objects` to create a line chart. This chart visualizes the interest levels of each keyword over time.

## Percentage Changes <a name="percentage-changes"></a>
The script calculates the percentage change in interest for each keyword over various time intervals (`1w`, `1m`, `3m`, `6m`, `12m`). It compares initial and final interest levels within each interval.

## Results <a name="results"></a>
The script displays the percentage change DataFrame, illustrating interest level fluctuations across selected time intervals. Additionally, it identifies the keyword with the highest interest.

To run the script, ensure the required libraries are installed. Upon execution, input desired keywords when prompted to gain insights into Google Trends data and keyword popularity trends.
