import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="AI Jobs KPI Dashboard", layout="wide")
st.title("💼 AI Job Market - Executive Dashboard")

@st.cache_data

def load_data():
    df = pd.read_csv("ai_job_dataset.csv", parse_dates=['posting_date'])
    df['required_skills_list'] = df['required_skills'].fillna("").str.split(',').apply(lambda x: [s.strip() for s in x if s.strip()])
    return df

df = load_data()
df['YearMonth'] = df['posting_date'].dt.to_period('M').astype(str)

# KPI CALCULATIONS
col1, col2, col3, col4 = st.columns(4)

# Total Jobs
with col1:
    total_jobs = len(df)
    prev_month_jobs = df[df['posting_date'] < df['posting_date'].max() - pd.DateOffset(months=1)].shape[0]
    change = ((total_jobs - prev_month_jobs) / prev_month_jobs) * 100 if prev_month_jobs else 0
    st.metric("Total Job Postings", f"{total_jobs:,}", f"{change:.1f}% from last month")
    fig = px.bar(df['YearMonth'].value_counts().sort_index(), labels={'index': 'Month', 'value': 'Postings'})
    st.plotly_chart(fig, use_container_width=True)

# Avg Salary
with col2:
    avg_salary = df['salary_usd'].mean()
    st.metric("Avg. Salary (USD)", f"${avg_salary:,.0f}")
    fig = px.line(df.groupby('YearMonth')['salary_usd'].mean().reset_index(), x='YearMonth', y='salary_usd', title="")
    st.plotly_chart(fig, use_container_width=True)

# Top Skill Count
with col3:
    skills = df.explode('required_skills_list')
    top_skill = skills['required_skills_list'].value_counts().idxmax()
    count = skills['required_skills_list'].value_counts().max()
    st.metric("Top Skill", f"{top_skill} ({count})")
    fig = px.bar(skills['required_skills_list'].value_counts().nlargest(10).reset_index(), x='required_skills_list', y='count', labels={'index': 'Skill', 'required_skills_list': 'Count'})
    st.plotly_chart(fig, use_container_width=True)

# Remote Rate
with col4:
    remote_rate = (df['remote_ratio'] > 50).mean() * 100
    st.metric("Remote Job Rate", f"{remote_rate:.1f}%")
    fig = px.area(df.groupby('YearMonth')['remote_ratio'].mean().reset_index(), x='YearMonth', y='remote_ratio')
    st.plotly_chart(fig, use_container_width=True)

# Bottom Section - Skills Over Time
st.markdown("### 🔍 Top Skills Trend Over Time")
skill_counts = skills.groupby(['YearMonth', 'required_skills_list']).size().reset_index(name='count')
top_skills = skills['required_skills_list'].value_counts().nlargest(6).index.tolist()
skill_counts = skill_counts[skill_counts['required_skills_list'].isin(top_skills)]

fig_bottom = px.bar(
    skill_counts,
    x='YearMonth', y='count', color='required_skills_list',
    title='Top Skills Over Time', barmode='stack',
    labels={'YearMonth': 'Month', 'count': 'Frequency', 'required_skills_list': 'Skill'}
)
st.plotly_chart(fig_bottom, use_container_width=True)

st.caption("Designed to mirror KPI dashboard layout – powered by Streamlit & Plotly")