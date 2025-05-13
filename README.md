# Data-Sculpt-Hackathon
## Social Media Analytics Dashboard

**A DataSculpt Hackathon 2025 Project**  
*Analyze. Visualize. Understand Social Media Trends.*

---

### **Project Overview**

This project delivers an end-to-end analysis of global social media usage, engagement, and behavioral trends, using a rich, multi-dimensional dataset. It includes:

- **Data Cleaning & EDA:** Comprehensive data wrangling and exploratory analysis in Python.
- **Interactive Dashboard:** A Streamlit web app for dynamic data exploration and stakeholder insights.
- **Deployment:** Hosted live on Streamlit Cloud for easy access and sharing.

---

### **Objectives**

- Extract actionable insights from a large, real-world social media dataset.
- Build an interactive dashboard for users to explore key patterns and KPIs.
- Tailor findings for operations, sales, and marketing teams, supporting data-driven decisions.

---

### **Project Structure**

| File/Folder                      | Description                                               |
|----------------------------------|-----------------------------------------------------------|
| `Hackathon-Streamlit.py`         | Streamlit app code for the analytics dashboard            |
| `Python-EDA-Notebook.py`         | Python script/notebook for EDA and data cleaning          |
| `Time-Wasters-on-Social-Media.csv` | Main dataset (anonymized user-level social media data)  |
| `README.md`                      | Project documentation (this file)                         |
| `requirements.txt`               | Python libraries required                |

---

### **Dataset**

- **File:** `Time-Wasters-on-Social-Media.csv`
- **Features:** 30+ columns, including demographics, platform, time spent, engagement, device/OS, content category, productivity loss, satisfaction, and more.
- **Size:** 1000 user records from multiple countries, platforms (Instagram, Facebook, YouTube, TikTok), and device types.

---

### **Key Analyses & Visualizations**

- **Platform Usage:** Bar charts and boxplots of user count, time spent, and age by platform.
- **Demographics:** Stacked bar charts for rural/urban, gender, and age group analysis.
- **Content Trends:** Popular video categories, watch reasons, and engagement by type.
- **Behavioral Metrics:** Productivity loss, addiction level, self-control, and satisfaction.
- **Device & OS Insights:** Pie charts and crosstabs for device and OS preference.
- **Temporal Patterns:** Watch time, session frequency, and best times for engagement.
- **Correlation Matrix:** Heatmap of numerical features to uncover key relationships.

---

### **Stakeholder Insights**

- **Operations:** Device, OS, and connection type usage patterns to inform technical and supply chain decisions.
- **Sales:** Top content categories and engagement metrics by platform for vendor partnerships.
- **Marketing:** Demographic targeting, watch reasons, and optimal engagement times for campaign planning.

---

### **How to Run Locally**

**Requirements:**
- Python 3.8+
- Libraries: `streamlit`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`

**Install dependencies:**
```bash
pip install streamlit pandas numpy matplotlib seaborn plotly
```

**Run the Streamlit dashboard:**
```bash
streamlit run Hackathon-Streamlit.py
```

**Run the EDA notebook/script:**
- Open `Python-EDA-Notebook.py` in Jupyter, Colab, or your IDE.

---

### **Deployment**

- The Streamlit app is deployed on Streamlit Cloud.  
- 

---

### **Screenshots & Dashboard Description**


- The dashboard features tabs/sections for platform usage, demographics, content trends, behavioral analysis, and stakeholder-specific insights.
- Interactive elements (dropdowns, sliders, filters) let users explore data by platform, category, time, and more.

---

### **How This Project Was Built**

- **Data Cleaning:** Handled missing values, type conversions, and categorical normalization.
- **EDA:** Used pandas, matplotlib, seaborn, and plotly for in-depth analysis and visualization.
- **Dashboard:** Built with Streamlit, leveraging its layout, interactivity, and Plotly integration.
- **Deployment:** Published on Streamlit Cloud for public access.

---

### **How to Contribute**

- Fork the repository and create a new branch for your feature/fix.
- Submit a pull request with a clear description of your changes.

---

### **Acknowledgments**

- Developed for the DataSculpt Hackathon 2025.
- Thanks to the organizers and all contributors!

---

### **License**

MIT License

---

*For feedback, issues, or questions, please open a GitHub issue or contact the maintainer.*

---

**Let’s sculpt insights from social media data!**
