import pandas as pd
import json
import requests
import numpy as np
import datetime
import os


url = 'https://api.covidtracking.com/v1/states/daily.json'
param = {}
covid_req = requests.get(url, param)
covid_req.raise_for_status()
covid = covid_req.json()

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]



for state in states:
    path = 'D:\\OneDrive\\Desktop\\statesData\\'
    path += (state + '.csv')
    
    df = pd.DataFrame()
    date = [item['date'] for item in covid if item['state'] == state]

    positive = [item['positive'] for item in covid if item['state'] == state]
    negative = [item['negative'] for item in covid if item['state'] == state]
    death = [item['death'] for item in covid if item['state'] == state]
    positiveIncrease = [item['positiveIncrease'] for item in covid if item['state'] == state]
    negativeIncrease = [item['negativeIncrease'] for item in covid if item['state'] == state]
    deathIncrease = [item['deathIncrease'] for item in covid if item['state'] == state]
    hospitalizedIncrease = [item['hospitalizedIncrease'] for item in covid if item['state'] == state]
    
    positiveName = 'positive' + '_' + state
    negativeName = 'negative' + '_' + state
    deathName = 'death' + '_' + state
    positiveIncreaseName = 'positiveIncrease' + '_' + state
    negativeIncreaseName = 'negativeIncrease' + '_' + state
    deathIncreaseName = 'deathIncrease' + '_' + state
    hospitalizedIncreaseName = 'hospitalizedIncrease' + '_' + state

    df['date'] = date
    df[positiveName] = positive
    df[negativeName] = negative
    df[deathName] = death
    df[positiveIncreaseName] = positiveIncrease
    df[negativeIncreaseName] = negativeIncrease
    df[deathIncreaseName] = deathIncrease
    df[hospitalizedIncreaseName] = hospitalizedIncrease
    df['date'] = pd.to_datetime(df['date'], format = '%Y%m%d')
    df = df.sort_values(by = ['date'] )
    df = df.fillna(value = 0)
    df.to_csv(path)






