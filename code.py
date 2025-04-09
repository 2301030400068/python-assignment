# Environmental Data Analysis Mini Project

# 📦 Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 🗂️ Load the air quality dataset
# Replace 'air_quality.csv' with your actual dataset path
df = pd.read_csv("air_quality.csv")  # Ensure your CSV has columns: date, city, pm2.5, pm10, no2, so2, co, o3

# 📅 Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# 🧹 Basic Data Cleaning
df = df.fillna(method='ffill')  # Forward fill missing values

# 📊 Statistical Summary
print("Summary Statistics:\n", df.describe())

# 🔗 Correlation Matrix
corr_matrix = df.corr()
print("\nCorrelation Matrix:\n", corr_matrix)

# 📈 Matplotlib Line Plot - PM2.5 Over Time (Delhi Example)
city = "Delhi"
df_city = df[df['city'] == city]

plt.figure(figsize=(10, 5))
plt.plot(df_city['date'], df_city['pm2.5'], label='PM2.5', color='blue')
plt.title(f"{city} - PM2.5 Over Time")
plt.xlabel("Date")
plt.ylabel("PM2.5 (µg/m³)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 🌡️ Seaborn Heatmap - Correlation Between Pollutants
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Pollutant Correlation Heatmap")
plt.show()

# 📦 Seaborn Boxplot - PM2.5 by City
plt.figure(figsize=(10, 6))
sns.boxplot(x='city', y='pm2.5', data=df)
plt.title("PM2.5 Levels Across Cities")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 📊 Plotly Interactive Line Chart - PM2.5 Trend
fig = px.line(df[df['city'] == 'Delhi'], x='date', y='pm2.5',
              title='Interactive PM2.5 Trend in Delhi',
              labels={'date': 'Date', 'pm2.5': 'PM2.5 (µg/m³)'})
fig.show()

# 🔍 Plotly Scatter Matrix - Pollutants Relationship
fig = px.scatter_matrix(df,
                        dimensions=['pm2.5', 'pm10', 'no2', 'so2', 'co', 'o3'],
                        color='city',
                        title="Scatter Matrix of Pollutants by City")
fig.show()
