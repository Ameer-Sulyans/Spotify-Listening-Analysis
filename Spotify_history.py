#!/usr/bin/env python
# coding: utf-8

# # Importing libraries

# In[ ]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:





# # Load

# In[ ]:


Spotify_data = pd.read_csv(r"C:\Users\meers\Downloads\Spotify Data\spotify_history.csv")


# In[ ]:


Spotify_data


# In[ ]:





# # Check Structure

# In[ ]:


Spotify_data.info()


# In[ ]:





# In[ ]:


Spotify_data.describe()


# In[ ]:





# In[ ]:


Spotify_data.head()


# In[ ]:





# # Cleaning Data
# 
# Handle missing values.
# 
# Convert timestamps to datetime.
# 
# Create new time-based features (year, month, day, hour).
# 
# Convert ms_played to minutes/seconds.
# 
# Remove extremely short plays less than 15 seconds to filter out accidental clicks.

# In[ ]:





# In[ ]:


#Convert timestep to Datetime

Spotify_data['ts'] = pd.to_datetime(Spotify_data['ts'])

Spotify_data['ts_year'] = Spotify_data['ts'].dt.year
Spotify_data['ts_month'] = Spotify_data['ts'].dt.month_name()
Spotify_data['ts_day'] = Spotify_data['ts'].dt.day
Spotify_data['ts_hour'] = Spotify_data['ts'].dt.hour



# In[ ]:


# Filter, convert to seconds, and format in one go
Spotify_data = (
    Spotify_data.assign(duration_seconds=Spotify_data['ms_played'] / 1000)
                .loc[lambda df: df['duration_seconds'] >= 15]
                .assign(minute_and_seconds=lambda df: df['duration_seconds'].apply(
                    lambda x: f"{int(x // 60)}:{int(x % 60):02d}"
                ))
)


Spotify_data


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#Removing uncessary columns

Spotify_data = Spotify_data.drop(columns=['ts', 'ms_played'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


Spotify_data


# In[ ]:





# # Exploratory Data Analysis
# 
# Questions to answer:
# 
# 1. Top artists & tracks by total minutes played.
# 
# 2. Listening habits by time (hour, day, month).
# 
# 3. Platform usage (web player, mobile, etc.).
# 
# 4. Skips behavior – which songs or artists are skipped most.
# 
# 5. Album listening trends.
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Data Visualization in Python
# 
# Bar chart: Top 10 Artists.
# 
# Heatmap: Listening by day of week & hour.
# 
# Pie chart: Platform usage.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




