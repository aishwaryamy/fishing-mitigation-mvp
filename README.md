# Fishing Mitigation App MVP - Sentiment Analysis Dashboard
## Purpose
A prototype for Ithaca Clean Energy's Fishing Mitigation App, analyzing stakeholder sentiment to support offshore wind project engagement.
## How to Run
1. Install dependencies: `pip install nltk pandas numpy plotly dash`
2. Ensure NLTK VADER lexicon is downloaded (included in setup).
3. Run `app.py`: `python3 app.py`
4. Access dashboard at `http://127.0.0.1:8050`
## Relevance
Supports Ithaca Clean Energy’s WATERFRONT platform by providing data-driven insights into stakeholder concerns, aiding fishing mitigation strategies.
# Fishing Mitigation App MVP - Sentiment Analysis Dashboard

## Overview
This project is a Minimum Viable Product (MVP) for Ithaca Clean Energy's Fishing Mitigation App. It provides data-driven insights for the WATERFRONT platform by analyzing stakeholder sentiment, visualizing sentiment trends, and generating mock Notices to Mariners (NTMs) to support engagement with fishing communities in offshore wind projects.

## Purpose
The dashboard leverages Natural Language Processing (NLP) to classify stakeholder comments as Positive, Negative, or Neutral, displays sentiment trends over time, and includes an interactive comment viewer. Additionally, it generates sample NTMs to simulate WATERFRONT’s real-time communication features. These tools help Ithaca Clean Energy understand fishermen’s concerns, reduce conflicts, and optimize offshore wind project costs, aligning with Module 1 of the Machine Learning Internship.

## Technologies Used
- Python 3
- NLTK (VADER for sentiment analysis)
- Pandas, NumPy
- Plotly, Dash (for interactive visualizations and data tables)

## How to Run
1. **Set up a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Mac/Linux

2. **Install dependencies:**
   pip install nltk pandas numpy plotly dash

3. **Download NLTK VADER lexicon:**
   python3 setup_nltk.py

4. **Run the dashboard:**
   python3 app.py

5. **Access the dashboard:**
   Open http://127.0.0.1:8050 in a web browser to view:

   A histogram of sentiment counts (e.g., 2 Positive, 2 Negative, 1 Neutral).
   A line plot of sentiment scores over time.
   An interactive table of comments, sentiment scores, and classifications.


   Check sentiment_results.csv for processed data.
   View dashboard_screenshot.png for a static image of the dashboard.


6. **Generate mock Notices to Mariners (NTMs):**
   python3 generate_ntm.py

  - Outputs ntm_data.csv with sample NTM data (e.g., construction alerts).
  - View terminal output or ntm_data.csv for results.

## File Structure
- app.py: Main script for sentiment analysis, trend visualization, and interactive dashboard.

- setup_nltk.py: Script to download the NLTK VADER lexicon.

- generate_ntm.py: Script to generate mock NTM data for WATERFRONT communication.

- sentiment_results.csv: Output file with sentiment analysis results (comments, dates, scores, classifications).

- ntm_data.csv: Output file with mock NTM data (ID, date, location, message, stakeholder).

- dashboard_screenshot.png: Screenshot of the enhanced dashboard.

- .gitignore: Excludes virtual environment and cache files.


## Features
### Sentiment Analysis Dashboard (app.py):

Histogram of stakeholder sentiment counts.
Line plot showing sentiment score trends over a simulated timeline.
Interactive table displaying comments, dates, sentiment scores, and classifications.

### NTM Data Generator (generate_ntm.py):

Creates sample NTMs with fields like ID, date, location, and message, supporting WATERFRONT’s real-time communication.

## Relevance
This prototype enhances Ithaca Clean Energy’s WATERFRONT platform by providing actionable insights into stakeholder sentiments and simulating NTM communication, addressing fishermen’s concerns about offshore wind impacts. The sentiment trend plot supports ODISY’s focus on data-driven lifecycle analytics. By integrating back-end NLP with front-end Dash visualizations and data generation, it fulfills Module 1’s emphasis on innovative, data-driven solutions for fishing mitigation strategies.

## Notes

* Ensure port 8050 is free; if not, modify the port in app.py (e.g., 8051).
* For issues, verify dependencies and NLTK data (~/nltk_data/sentiment).
* The dashboard uses sample data (5 comments, 5 NTMs); real data can be integrated by updating app.py or generate_ntm.py.
* Update dashboard_screenshot.png after dashboard changes to reflect the latest interface.