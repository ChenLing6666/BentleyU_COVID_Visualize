import pandas as pd
import os



states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

df_frames = []
for state in states:
    path = 'D:\\Bentley\\DataScienceFinalProject\\statesData\\'
    path += state + '.csv'
    
    df = pd.read_csv(path, index_col=1)
    df.drop('Unnamed: 0', inplace=True, axis=1)
    
    df_frames.append(df)


df_final = pd.concat(df_frames, join='outer', axis=1, sort= True)
df_final.fillna(0, inplace=True)
df_final.to_csv('D:\\OneDrive\\Desktop\\df.csv')
