import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize-matplotlib

# Load the dataset
data_path = '/mnt/data/202406_202406_연령별인구현황_월간.csv'
df = pd.read_csv(data_path, encoding='cp949')

# Assuming the data contains columns 'Region', 'Age Group', and 'Population'
# Adjust the column names and preprocessing as per the actual structure of your dataset

# Example column names and preprocessing
# df.columns = ['Region', 'Age Group', 'Population']
# df['Population'] = df['Population'].str.replace(',', '').astype(int)

# Streamlit App
st.title("Middle School Population Ratio by Region")

# User input for region
regions = df['Region'].unique()
selected_region = st.selectbox("Select a Region", regions)

# Filter data for the selected region
region_data = df[df['Region'] == selected_region]

# Define middle school age groups (13-15 years)
# Adjust the age groups as per your dataset
middle_school_ages = ['13세', '14세', '15세']
middle_school_data = region_data[region_data['Age Group'].isin(middle_school_ages)]

# Calculate the total population and middle school population
total_population = region_data['Population'].sum()
middle_school_population = middle_school_data['Population'].sum()

# Calculate the ratio
middle_school_ratio = middle_school_population / total_population * 100
other_population_ratio = 100 - middle_school_ratio

# Prepare data for pie chart
labels = ['Middle School Age (13-15)', 'Other Ages']
sizes = [middle_school_ratio, other_population_ratio]
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)  # explode 1st slice

# Plot pie chart
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
