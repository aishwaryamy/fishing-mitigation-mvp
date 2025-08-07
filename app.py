import dash
from dash import dcc, html, dash_table
import plotly.express as px
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
from datetime import datetime, timedelta

# Simulated stakeholder comments with dates
comments = [
    ("The wind farm disrupts our fishing grounds, causing losses.", datetime.now() - timedelta(days=4)),
    ("I appreciate the updates from the WATERFRONT app, very helpful!", datetime.now() - timedelta(days=3)),
    ("Construction noise harms marine life, causing fishing disruptions.", datetime.now() - timedelta(days=2)),
    ("Excited about clean energy but worried about our livelihood.", datetime.now() - timedelta(days=1)),
    ("The app provides updates on wind farm operations.", datetime.now())
]

# Create DataFrame
df = pd.DataFrame(comments, columns=['Comment', 'Date'])

# Analyze sentiment
sia = SentimentIntensityAnalyzer()
df['Sentiment_Score'] = df['Comment'].apply(lambda x: sia.polarity_scores(x)['compound'])
df['Sentiment'] = df['Sentiment_Score'].apply(lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Neutral')

# Debug output
if __name__ == '__main__' and (os.environ.get('WERKZEUG_RUN_MAIN') == 'true'):
    print("DataFrame:")
    print(df)
    print("\nSentiment Counts:")
    print(df['Sentiment'].value_counts())

# Save results
df.to_csv('sentiment_results.csv', index=False)

# Create visualizations
fig_histogram = px.histogram(df, x='Sentiment', title='Stakeholder Sentiment on Offshore Wind')
fig_trend = px.line(df, x='Date', y='Sentiment_Score', title='Sentiment Trend Over Time', markers=True)

# Initialize Dash app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('Fishing Mitigation App: Sentiment Analysis'),
    html.H2('Sentiment Distribution'),
    dcc.Graph(figure=fig_histogram),
    html.H2('Sentiment Trend'),
    dcc.Graph(figure=fig_trend),
    html.H2('Stakeholder Comments'),
    dash_table.DataTable(
        id='comment-table',
        columns=[
            {'name': 'Date', 'id': 'Date'},
            {'name': 'Comment', 'id': 'Comment'},
            {'name': 'Sentiment Score', 'id': 'Sentiment_Score'},
            {'name': 'Sentiment', 'id': 'Sentiment'}
        ],
        data=df.to_dict('records'),
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left', 'padding': '5px'},
        page_size=5
    )
])

if __name__ == '__main__':
    app.run(debug=True, port=8050)