# Social Media Analytics Dashboard
# DataSculpt Hackathon 2025

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page configuration
st.set_page_config(
    page_title="Social Media Analytics Dashboard",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to enhance the dashboard appearance
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.8rem;
        color: #0277BD;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.5rem;
        color: #0288D1;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    .insight-text {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 5px;
        border-left: 5px solid #1E88E5;
    }
    .stPlotlyChart {
        background-color: white;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='main-header'>📱 Social Media Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown("This interactive dashboard provides insights into social media usage trends, user behavior, and platform effectiveness.")
st.markdown("---")

# Load the data
@st.cache_data
def load_data():
    df = pd.read_csv('Time-Wasters on Social Media.csv')
    # Basic cleaning
    df['Debt'] = df['Debt'].astype(bool)
    df['Owns Property'] = df['Owns Property'].astype(bool)
    
    # Create Age Group column
    age_bins = [0, 18, 25, 35, 45, 55, 65, 100]
    age_labels = ['Under 18', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
    df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)
    
    return df

df = load_data()

# Sidebar for filters
st.sidebar.markdown("## 🔍 Filters")

# Platform filter
platforms = ['All'] + sorted(df['Platform'].unique().tolist())
selected_platform = st.sidebar.selectbox("Select Platform", platforms)

# Age range filter
min_age = int(df['Age'].min())
max_age = int(df['Age'].max())
age_range = st.sidebar.slider("Age Range", min_age, max_age, (min_age, max_age))

# Gender filter
genders = ['All'] + sorted(df['Gender'].unique().tolist())
selected_gender = st.sidebar.selectbox("Select Gender", genders)

# Location filter
locations = ['All'] + sorted(df['Location'].unique().tolist())
selected_location = st.sidebar.selectbox("Select Location", locations)

# Apply filters
filtered_df = df.copy()
if selected_platform != 'All':
    filtered_df = filtered_df[filtered_df['Platform'] == selected_platform]
filtered_df = filtered_df[(filtered_df['Age'] >= age_range[0]) & (filtered_df['Age'] <= age_range[1])]
if selected_gender != 'All':
    filtered_df = filtered_df[filtered_df['Gender'] == selected_gender]
if selected_location != 'All':
    filtered_df = filtered_df[filtered_df['Location'] == selected_location]

# Display filter summary
st.sidebar.markdown("### Applied Filters:")
st.sidebar.markdown(f"**Platform:** {selected_platform}")
st.sidebar.markdown(f"**Age Range:** {age_range[0]} to {age_range[1]}")
st.sidebar.markdown(f"**Gender:** {selected_gender}")
st.sidebar.markdown(f"**Location:** {selected_location}")
st.sidebar.markdown(f"**Filtered Data Size:** {filtered_df.shape[0]} records")

# Overview section
st.markdown("<h2 class='sub-header'>📊 Platform Overview</h2>", unsafe_allow_html=True)

# KPI cards in row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### Total Users")
    st.markdown(f"<h2 style='text-align: center; color: #1E88E5;'>{filtered_df.shape[0]}</h2>", unsafe_allow_html=True)

with col2:
    avg_time = round(filtered_df['Total Time Spent'].mean(), 2)
    st.markdown("### Avg. Time Spent")
    st.markdown(f"<h2 style='text-align: center; color: #1E88E5;'>{avg_time} min</h2>", unsafe_allow_html=True)

with col3:
    avg_satisfaction = round(filtered_df['Satisfaction'].mean(), 2)
    st.markdown("### Avg. Satisfaction")
    st.markdown(f"<h2 style='text-align: center; color: #1E88E5;'>{avg_satisfaction}/10</h2>", unsafe_allow_html=True)

with col4:
    avg_addiction = round(filtered_df['Addiction Level'].mean(), 2)
    st.markdown("### Avg. Addiction Level")
    st.markdown(f"<h2 style='text-align: center; color: #1E88E5;'>{avg_addiction}/10</h2>", unsafe_allow_html=True)

st.markdown("---")

# User Demographics Section
st.markdown("<h2 class='sub-header'>👥 User Demographics</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Age distribution
    fig_age = px.histogram(
        filtered_df, 
        x='Age', 
        color='Platform' if selected_platform == 'All' else None,
        nbins=20,
        title='Age Distribution',
        labels={'Age': 'Age', 'count': 'Number of Users'},
        opacity=0.8
    )
    fig_age.update_layout(height=400)
    st.plotly_chart(fig_age, use_container_width=True)

with col2:
    # Gender distribution
    gender_counts = filtered_df['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']
    
    fig_gender = px.pie(
        gender_counts, 
        values='Count', 
        names='Gender', 
        title='Gender Distribution',
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig_gender.update_layout(height=400)
    st.plotly_chart(fig_gender, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    # Location map
    location_counts = filtered_df['Location'].value_counts().reset_index()
    location_counts.columns = ['Location', 'Count']
    
    fig_location = px.choropleth(
        location_counts,
        locations='Location',
        locationmode='country names',
        color='Count',
        hover_name='Location',
        color_continuous_scale='Blues',
        title='User Distribution by Country',
    )
    fig_location.update_layout(height=400, geo=dict(showframe=False, showcoastlines=True))
    st.plotly_chart(fig_location, use_container_width=True)

with col2:
    # Profession distribution
    profession_counts = filtered_df['Profession'].value_counts().reset_index()
    profession_counts.columns = ['Profession', 'Count']
    profession_counts = profession_counts.sort_values('Count', ascending=True).tail(10)
    
    fig_profession = px.bar(
        profession_counts,
        y='Profession',
        x='Count',
        orientation='h',
        title='Top 10 Professions',
        color='Count',
        color_continuous_scale='Blues'
    )
    fig_profession.update_layout(height=400)
    st.plotly_chart(fig_profession, use_container_width=True)

st.markdown("---")

# Platform Usage Analysis
st.markdown("<h2 class='sub-header'>📱 Platform Usage Analysis</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Platform usage count
    if selected_platform == 'All':
        platform_counts = filtered_df['Platform'].value_counts().reset_index()
        platform_counts.columns = ['Platform', 'Count']
        
        fig_platform = px.bar(
            platform_counts, 
            x='Platform', 
            y='Count',
            title='Platform Usage',
            color='Platform',
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig_platform.update_layout(height=400)
        st.plotly_chart(fig_platform, use_container_width=True)
    else:
        st.info(f"Filter is set to {selected_platform} only.")

with col2:
    # Time spent by platform
    platform_time = filtered_df.groupby('Platform')['Total Time Spent'].mean().reset_index()
    platform_time = platform_time.sort_values('Total Time Spent', ascending=False)
    
    fig_time = px.bar(
        platform_time, 
        x='Platform', 
        y='Total Time Spent',
        title='Average Time Spent by Platform (minutes)',
        color='Platform',
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig_time.update_layout(height=400)
    st.plotly_chart(fig_time, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    # Device type usage
    device_counts = filtered_df['DeviceType'].value_counts().reset_index()
    device_counts.columns = ['DeviceType', 'Count']
    
    fig_device = px.pie(
        device_counts, 
        values='Count', 
        names='DeviceType', 
        title='Device Type Distribution',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig_device.update_layout(height=400)
    st.plotly_chart(fig_device, use_container_width=True)

with col2:
    # Operating Systems
    os_counts = filtered_df['OS'].value_counts().reset_index()
    os_counts.columns = ['OS', 'Count']
    
    fig_os = px.pie(
        os_counts, 
        values='Count', 
        names='OS', 
        title='Operating System Distribution',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig_os.update_layout(height=400)
    st.plotly_chart(fig_os, use_container_width=True)

st.markdown("---")

# Content Analysis
st.markdown("<h2 class='sub-header'>🎬 Content Analysis</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Video category popularity
    category_counts = filtered_df['Video Category'].value_counts().reset_index()
    category_counts.columns = ['Video Category', 'Count']
    category_counts = category_counts.sort_values('Count', ascending=False)
    
    fig_category = px.bar(
        category_counts, 
        x='Video Category', 
        y='Count',
        title='Popularity of Video Categories',
        color='Count',
        color_continuous_scale='Viridis'
    )
    fig_category.update_layout(height=450)
    st.plotly_chart(fig_category, use_container_width=True)

with col2:
    # Engagement by video category
    category_engagement = filtered_df.groupby('Video Category')['Engagement'].mean().reset_index()
    category_engagement = category_engagement.sort_values('Engagement', ascending=False)
    
    fig_engagement = px.bar(
        category_engagement, 
        x='Video Category', 
        y='Engagement',
        title='Average Engagement by Video Category',
        color='Engagement',
        color_continuous_scale='Viridis'
    )
    fig_engagement.update_layout(height=450)
    st.plotly_chart(fig_engagement, use_container_width=True)

# Video Length vs Time Spent
fig_video_time = px.scatter(
    filtered_df,
    x='Video Length',
    y='Time Spent On Video',
    color='Platform' if selected_platform == 'All' else None,
    size='Engagement',
    hover_data=['Video Category'],
    title='Video Length vs Time Spent Watching',
    labels={
        'Video Length': 'Video Length (minutes)',
        'Time Spent On Video': 'Time Spent Watching (minutes)'
    },
    opacity=0.7
)
fig_video_time.update_layout(height=500)
st.plotly_chart(fig_video_time, use_container_width=True)

st.markdown("---")

# User Behavior Analysis
st.markdown("<h2 class='sub-header'>🧠 User Behavior Analysis</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Watch reasons
    reason_counts = filtered_df['Watch Reason'].value_counts().reset_index()
    reason_counts.columns = ['Watch Reason', 'Count']
    
    fig_reason = px.pie(
        reason_counts, 
        values='Count', 
        names='Watch Reason', 
        title='Reasons for Watching',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig_reason.update_layout(height=400)
    st.plotly_chart(fig_reason, use_container_width=True)

with col2:
    # Watch time distribution
    time_counts = filtered_df['Watch Time'].value_counts().reset_index()
    time_counts.columns = ['Watch Time', 'Count']
    
    # Sort by time (Morning, Afternoon, Evening, Night)
    time_order = {"8:00 AM": 1, "2:00 PM": 2, "5:00 PM": 3, "9:00 PM": 4}
    time_counts['Order'] = time_counts['Watch Time'].map(time_order)
    time_counts = time_counts.sort_values('Order')
    
    fig_watch_time = px.bar(
        time_counts, 
        x='Watch Time', 
        y='Count',
        title='Watch Time Distribution',
        color='Watch Time',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig_watch_time.update_layout(height=400)
    st.plotly_chart(fig_watch_time, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    # Self Control vs Addiction Level
    fig_control = px.scatter(
        filtered_df, 
        x='Self Control', 
        y='Addiction Level',
        color='Platform' if selected_platform == 'All' else None,
        title='Self Control vs Addiction Level',
        labels={'Self Control': 'Self Control (1-10)', 'Addiction Level': 'Addiction Level (0-10)'},
        opacity=0.7
    )
    fig_control.update_layout(height=400)
    st.plotly_chart(fig_control, use_container_width=True)

with col2:
    # Productivity Loss by Platform
    platform_productivity = filtered_df.groupby('Platform')['ProductivityLoss'].mean().reset_index()
    platform_productivity = platform_productivity.sort_values('ProductivityLoss', ascending=False)
    
    fig_productivity = px.bar(
        platform_productivity, 
        x='Platform', 
        y='ProductivityLoss',
        title='Average Productivity Loss by Platform (1-10)',
        color='Platform',
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    fig_productivity.update_layout(height=400)
    st.plotly_chart(fig_productivity, use_container_width=True)

st.markdown("---")

# Insights for Stakeholders
st.markdown("<h2 class='sub-header'>💡 Insights for Stakeholders</h2>", unsafe_allow_html=True)

# Tabs for different team insights
tab1, tab2, tab3 = st.tabs(["Operations Team", "Sales Team", "Marketing Team"])

with tab1:
    st.markdown("<h3 class='section-header'>Supply Chain Insights</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Connection Type Analysis
        connection_counts = filtered_df['ConnectionType'].value_counts().reset_index()
        connection_counts.columns = ['ConnectionType', 'Count']
        
        fig_connection = px.pie(
            connection_counts,
            values='Count',
            names='ConnectionType',
            title='Internet Connection Type Distribution',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_connection, use_container_width=True)
        
    with col2:
        # Platform by Device Type
        platform_device = pd.crosstab(filtered_df['Platform'], filtered_df['DeviceType'])
        platform_device = platform_device.reset_index()
        platform_device_melt = pd.melt(platform_device, id_vars=['Platform'], var_name='DeviceType', value_name='Count')
        
        fig_platform_device = px.bar(
            platform_device_melt,
            x='Platform',
            y='Count',
            color='DeviceType',
            title='Platform Usage by Device Type',
            barmode='group'
        )
        st.plotly_chart(fig_platform_device, use_container_width=True)
    
    # Key insights
    st.markdown("<div class='insight-text'>", unsafe_allow_html=True)
    st.markdown("### Key Supply Chain Insights:")
    st.markdown("""
    - Smartphone is the dominant device for social media access, suggesting a need to optimize mobile app experiences.
    - Wi-Fi and Mobile Data usage patterns indicate where users access content, which can inform infrastructure investments.
    - Android is the leading OS, followed by iOS, showing where development resources should be allocated.
    - Device preferences vary by platform, which should inform hardware procurement and compatibility planning.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<h3 class='section-header'>Vendor Collaboration Insights</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Engagement by platform
        platform_engagement = filtered_df.groupby('Platform')['Engagement'].mean().reset_index()
        platform_engagement = platform_engagement.sort_values('Engagement', ascending=False)
        
        fig_platform_engagement = px.bar(
            platform_engagement,
            x='Platform',
            y='Engagement',
            title='Average Engagement by Platform',
            color='Platform',
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        st.plotly_chart(fig_platform_engagement, use_container_width=True)
        
    with col2:
        # Top video categories by engagement
        top_categories = filtered_df.groupby('Video Category')['Engagement'].mean().reset_index()
        top_categories = top_categories.sort_values('Engagement', ascending=False).head(5)
        
        fig_top_categories = px.bar(
            top_categories,
            x='Video Category',
            y='Engagement',
            title='Top 5 Video Categories by Engagement',
            color='Video Category',
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        st.plotly_chart(fig_top_categories, use_container_width=True)
    
    # Platform-category matrix
    platform_category = pd.crosstab(filtered_df['Platform'], filtered_df['Video Category'])
    fig_heatmap = px.imshow(
        platform_category,
        labels=dict(x="Video Category", y="Platform", color="Count"),
        title="Video Category Popularity by Platform",
        color_continuous_scale="Blues"
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)
    
    # Key insights
    st.markdown("<div class='insight-text'>", unsafe_allow_html=True)
    st.markdown("### Key Sales Insights:")
    st.markdown("""
    - Higher engagement platforms represent prime opportunities for partnership and advertising investments.
    - Entertainment and Educational content generate the highest engagement, suggesting potential for targeted product placement.
    - Each platform has distinct content preferences, indicating the need for platform-specific sales strategies.
    - Cross-platform analysis shows opportunities to target underserved content categories on specific platforms.
    - User satisfaction correlates with engagement, suggesting that high-quality content partnerships could drive sales.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.markdown("<h3 class='section-header'>Marketing Strategy Insights</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Age vs Satisfaction by Platform
        fig_age_sat = px.scatter(
            filtered_df,
            x='Age',
            y='Satisfaction',
            color='Platform' if selected_platform == 'All' else None,
            size='Total Time Spent',
            title='Age vs Satisfaction by Platform',
            opacity=0.7
        )
        st.plotly_chart(fig_age_sat, use_container_width=True)
        
    with col2:
        # Watch reason by gender
        gender_reason = pd.crosstab(filtered_df['Gender'], filtered_df['Watch Reason'])
        gender_reason = gender_reason.reset_index()
        gender_reason_melt = pd.melt(gender_reason, id_vars=['Gender'], var_name='Watch Reason', value_name='Count')
        
        fig_gender_reason = px.bar(
            gender_reason_melt,
            x='Gender',
            y='Count',
            color='Watch Reason',
            title='Watch Reasons by Gender',
            barmode='group'
        )
        st.plotly_chart(fig_gender_reason, use_container_width=True)
    
    # Demographics vs content preferences
    demo_content = pd.crosstab([filtered_df['Age Group'], filtered_df['Gender']], filtered_df['Video Category'])
    
    fig_demo_content = px.density_heatmap(
        filtered_df, 
        x='Video Category', 
        y='Age Group',
        color_continuous_scale='Viridis',
        title='Content Preferences by Age Group'
    )
    st.plotly_chart(fig_demo_content, use_container_width=True)
    
    # Key insights
    st.markdown("<div class='insight-text'>", unsafe_allow_html=True)
    st.markdown("### Key Marketing Insights:")
    st.markdown("""
    - Different age groups show distinct platform preferences and content engagement patterns.
    - Entertainment content appeals across demographics, while specialized content has targeted appeal.
    - Gender differences in watch reasons suggest opportunities for tailored marketing campaigns.
    - Peak usage times vary by demographic, indicating optimal scheduling for marketing campaigns.
    - Location-based analysis reveals regional preferences that can inform localized marketing strategies.
    - Engagement metrics correlate with specific content types, suggesting where to focus creative resources.
    """)
    st.markdown("</div>", unsafe_allow_html=True)