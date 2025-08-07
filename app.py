import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Simulated stakeholder comments
comments = [
    "The wind farm disrupts our fishing grounds, causing losses.",
    "I appreciate the updates from the WATERFRONT app, very helpful!",
    "Construction noise affects marine life, we need solutions.",
    "Excited about clean energy but worried about our livelihood.",
    "The app makes communication with wind farm operators easy."
]
df = pd.DataFrame(comments, columns=['Comment'])

# Analyze sentiment
sia = SentimentIntensityAnalyzer()
df['Sentiment_Score'] = df['Comment'].apply(lambda x: sia.polarity_scores(x)['compound'])
df['Sentiment'] = df['Sentiment_Score'].apply(lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Neutral')

# Save results
df.to_csv('sentiment_results.csv', index=False)

# Create visualization
fig = px.histogram(df, x='Sentiment', title='Stakeholder Sentiment on Offshore Wind')

# Initialize Dash app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('Fishing Mitigation App: Sentiment Analysis'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True, port=8050)