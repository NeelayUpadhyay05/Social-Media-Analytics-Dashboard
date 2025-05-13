# Social Media Analytics - Exploratory Data Analysis
# DataSculpt Hackathon 2025

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set styles
plt.style.use('fivethirtyeight')
sns.set(style="whitegrid")
pd.set_option('display.max_columns', None)

# Load the dataset
df = pd.read_csv('Time-Wasters on Social Media.csv')

# Display basic information
print("Dataset Shape:", df.shape)
print("\nFirst few rows:")
df.head()

# Check data types and missing values
print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# Basic statistics
print("\nBasic Statistics:")
df.describe()

# ------ DATA CLEANING ------

# Check for duplicates
duplicate_rows = df[df.duplicated()]
print(f"\nNumber of duplicate rows: {len(duplicate_rows)}")

# Convert data types as needed
# Convert 'Debt' and 'Owns Property' to boolean if they're not already
df['Debt'] = df['Debt'].astype(bool)
df['Owns Property'] = df['Owns Property'].astype(bool)

# Clean any inconsistent entries in categorical variables
# Check for unique values in categorical columns
categorical_cols = ['Gender', 'Location', 'Profession', 'Demographics', 'Platform', 
                   'Video Category', 'Frequency', 'Watch Reason', 'DeviceType', 'OS', 
                   'CurrentActivity', 'ConnectionType']

for col in categorical_cols:
    print(f"\nUnique values in {col}:")
    print(df[col].value_counts())

# ------ EXPLORATORY ANALYSIS ------

# 1. Platform Usage Distribution
plt.figure(figsize=(12, 6))
platform_counts = df['Platform'].value_counts()
sns.barplot(x=platform_counts.index, y=platform_counts.values)
plt.title('Social Media Platform Usage')
plt.xlabel('Platform')
plt.ylabel('Number of Users')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Age Distribution by Platform
plt.figure(figsize=(14, 7))
sns.boxplot(x='Platform', y='Age', data=df)
plt.title('Age Distribution by Platform')
plt.xlabel('Platform')
plt.ylabel('Age')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Time Spent Analysis by Platform
plt.figure(figsize=(14, 7))
sns.barplot(x='Platform', y='Total Time Spent', data=df)
plt.title('Average Time Spent by Platform')
plt.xlabel('Platform')
plt.ylabel('Total Time Spent (minutes)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Video Category Popularity
plt.figure(figsize=(14, 8))
category_counts = df['Video Category'].value_counts()
sns.barplot(x=category_counts.index, y=category_counts.values)
plt.title('Popularity of Video Categories')
plt.xlabel('Video Category')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# 5. Watch Reason Analysis
plt.figure(figsize=(14, 7))
reason_counts = df['Watch Reason'].value_counts()
sns.barplot(x=reason_counts.index, y=reason_counts.values)
plt.title('Reasons for Watching Social Media Content')
plt.xlabel('Watch Reason')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Productivity Loss by Platform
plt.figure(figsize=(14, 7))
sns.boxplot(x='Platform', y='ProductivityLoss', data=df)
plt.title('Productivity Loss by Platform')
plt.xlabel('Platform')
plt.ylabel('Productivity Loss (Scale 1-10)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 7. Addiction Level Analysis
plt.figure(figsize=(14, 7))
sns.boxplot(x='Platform', y='Addiction Level', data=df)
plt.title('Addiction Level by Platform')
plt.xlabel('Platform')
plt.ylabel('Addiction Level (Scale 0-10)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 8. Device Usage Analysis
plt.figure(figsize=(12, 6))
device_counts = df['DeviceType'].value_counts()
plt.pie(device_counts, labels=device_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Device Type Distribution')
plt.axis('equal')
plt.tight_layout()
plt.show()

# 9. Engagement by Video Category
plt.figure(figsize=(14, 8))
sns.boxplot(x='Video Category', y='Engagement', data=df)
plt.title('Engagement by Video Category')
plt.xlabel('Video Category')
plt.ylabel('Engagement')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# 10. Watch Time Distribution
plt.figure(figsize=(14, 7))
watch_time_counts = df['Watch Time'].value_counts()
sns.barplot(x=watch_time_counts.index, y=watch_time_counts.values)
plt.title('Watch Time Distribution')
plt.xlabel('Time of Day')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 11. Satisfaction Analysis
plt.figure(figsize=(14, 7))
sns.boxplot(x='Platform', y='Satisfaction', data=df)
plt.title('User Satisfaction by Platform')
plt.xlabel('Platform')
plt.ylabel('Satisfaction (Scale 1-10)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 12. Self Control vs Addiction Level
plt.figure(figsize=(10, 8))
sns.scatterplot(x='Self Control', y='Addiction Level', data=df, hue='Platform')
plt.title('Self Control vs Addiction Level')
plt.xlabel('Self Control (Scale 1-10)')
plt.ylabel('Addiction Level (Scale 0-10)')
plt.tight_layout()
plt.show()

# 13. Demographic Analysis
plt.figure(figsize=(12, 6))
demo_platform = pd.crosstab(df['Demographics'], df['Platform'])
demo_platform.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Platform Usage by Demographics')
plt.xlabel('Demographics')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 14. Location Analysis
plt.figure(figsize=(14, 8))
location_counts = df['Location'].value_counts().head(10)  # Top 10 locations
sns.barplot(x=location_counts.index, y=location_counts.values)
plt.title('Top 10 Locations by User Count')
plt.xlabel('Location')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------ CORRELATION ANALYSIS ------

# Select numerical columns for correlation analysis
numerical_cols = ['Age', 'Income', 'Total Time Spent', 'Number of Sessions', 
                  'Video Length', 'Engagement', 'Importance Score', 
                  'Time Spent On Video', 'Number of Videos Watched', 'Scroll Rate',
                  'ProductivityLoss', 'Satisfaction', 'Self Control', 'Addiction Level']

# Calculate correlation matrix
corr_matrix = df[numerical_cols].corr()

# Plot correlation heatmap
plt.figure(figsize=(14, 12))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix of Numerical Variables')
plt.tight_layout()
plt.show()

# ------ KEY INSIGHTS FOR STAKEHOLDERS ------

# 1. Insights for Operation Team (Supply Chain)
# Analyze device usage, connection types, and OS preferences
print("\n--- INSIGHTS FOR OPERATION TEAM ---")

# Platform usage by device type
platform_device = pd.crosstab(df['Platform'], df['DeviceType'])
print("\nPlatform usage by device type:")
print(platform_device)

# Connection type distribution
connection_counts = df['ConnectionType'].value_counts()
print("\nConnection Type Distribution:")
print(connection_counts)

# OS distribution
os_counts = df['OS'].value_counts()
print("\nOS Distribution:")
print(os_counts)

# 2. Insights for Sales Team (Vendor Collaboration)
print("\n--- INSIGHTS FOR SALES TEAM ---")

# Popular video categories by platform
platform_category = pd.crosstab(df['Platform'], df['Video Category'])
print("\nPopular video categories by platform:")
print(platform_category)

# Engagement by platform and category
platform_engagement = df.groupby(['Platform', 'Video Category'])['Engagement'].mean().reset_index()
print("\nAverage engagement by platform and video category:")
print(platform_engagement.sort_values('Engagement', ascending=False).head(10))

# 3. Insights for Marketing Team (Customized Launch)
print("\n--- INSIGHTS FOR MARKETING TEAM ---")

# User demographics by platform
platform_demographics = pd.crosstab([df['Age'], df['Gender']], df['Platform'])
print("\nPlatform usage by age and gender:")
print(platform_demographics)

# Watch reasons by platform
platform_reason = pd.crosstab(df['Platform'], df['Watch Reason'])
print("\nWatch reasons by platform:")
print(platform_reason)

# Best time to reach users
platform_time = pd.crosstab(df['Platform'], df['Frequency'])
print("\nBest time to reach users by platform:")
print(platform_time)