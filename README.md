# AI Jobs Market Dashboard

An interactive dashboard for exploring and analyzing the AI job market using Streamlit and Plotly.

## Features
- Visualize key metrics: job titles, salaries, remote ratio, education, locations, and top skills
- Filter jobs by date, experience, education, remote ratio, salary, location, and required skills
- Interactive charts and time series trends

## Getting Started

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Prepare the Dataset

Place your `ai_job_dataset.csv` file in the project directory. The CSV should include columns like:
- `posting_date`, `application_deadline`, `job_title`, `salary_usd`, `remote_ratio`, `education_required`, `experience_level`, `company_location`, `required_skills`

### 3. Run the App

```bash
streamlit run main.py
```

The app will open in your browser. If not, visit the URL shown in your terminal (usually http://localhost:8501).

## How to Use
1. **Filter Options**: Use the filter panel at the top to select date range, experience, education, remote ratio, salary, location, and skills.
2. **Visualizations**: Explore the interactive charts below the filters to gain insights into the AI job market.
3. **Total Jobs**: The number of jobs matching your filters is displayed above the charts.

## Requirements
- Python 3.8+
- Streamlit
- pandas
- plotly

Install all dependencies with `pip install -r requirements.txt`.

