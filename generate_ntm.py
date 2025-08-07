import pandas as pd
from datetime import datetime
import random

ntm_data = [
    {
        'NTM_ID': f'NTM-{i+1:03d}',
        'Date': datetime.now().strftime('%Y-%m-%d'),
        'Location': random.choice(['Block Island', 'Vineyard Wind', 'South Fork']),
        'Message': random.choice([
            'Construction scheduled from 08:00 to 17:00. Avoid area.',
            'Maintenance work on turbines. Reduced vessel traffic advised.',
            'Survey operations in progress. Contact WATERFRONT for details.'
        ]),
        'Stakeholder': 'All Mariners'
    } for i in range(5)
]

df_ntm = pd.DataFrame(ntm_data)
df_ntm.to_csv('ntm_data.csv', index=False)
print("Notice to Mariners Data:")
print(df_ntm)