import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)

raw_data = pd.read_csv('EPL_Set.csv',dayfirst=True, parse_dates=['Date'])
conditions = [raw_data['FTHG'] >raw_data['FTAG'], raw_data['FTHG'] ==raw_data['FTAG'],raw_data['FTHG'] <raw_data['FTAG']]
choices = ["Home", 'Draw', 'Away']
raw_data["FT Result"] = np.select(conditions, choices, default=np.nan)
conditions = [raw_data['HTHG'] >raw_data['HTAG'], raw_data['HTHG'] ==raw_data['HTAG'],raw_data['HTHG'] <raw_data['HTAG']]
raw_data["HT Result"] = np.select(conditions, choices, default=np.nan)
gamedays = raw_data.groupby(['Season']).agg({'Date': [np.max]})
gamedays.columns=gamedays.columns.droplevel(0)
gamedays.reset_index(inplace=True)
gamedays.rename(columns={'amax':'Last Gameday'}, inplace=True)
raw_data=raw_data.merge(gamedays,how='left',on=['Season'])
raw_data['is Last Gameday'] = raw_data['Last Gameday']==raw_data['Date']
home = raw_data[['Season','Date','HomeTeam','FT Result',"HT Result",'is Last Gameday']]

conditions = [raw_data['FT Result'] =='Home',raw_data['FT Result'] =='Draw',raw_data['FT Result'] =='Away']
choices = [3,1,0]
home["FT Points"] = np.select(conditions, choices, default=np.nan)
conditions = [raw_data['HT Result'] =='Home',raw_data['HT Result'] =='Draw',raw_data['HT Result'] =='Away']
choices = [3,1,0]
home["HT Points"] = np.select(conditions, choices, default=0)

away = raw_data[['Season','Date','AwayTeam','FT Result',"HT Result",'is Last Gameday']]
conditions = [raw_data['FT Result'] =='Home',raw_data['FT Result'] =='Draw',raw_data['FT Result'] =='Away']
choices = [0,1,3]
away["FT Points"] = np.select(conditions, choices, default=np.nan)
conditions = [raw_data['HT Result'] =='Home',raw_data['HT Result'] =='Draw',raw_data['HT Result'] =='Away']
away["HT Points"] = np.select(conditions, choices, default=np.nan)

home.rename(columns={'HomeTeam':'Team'}, inplace=True)
away.rename(columns={'AwayTeam':'Team'}, inplace=True)
all = pd.concat([home, away], ignore_index=True)

all['FT Points Doubled'] = np.where(all['is Last Gameday']==True, all['FT Points']*2 ,all['FT Points'])
# points = all.groupby(['Season','Team']).agg({'Date': [np.max]})
# determine points per season
# determine points at halftime per season
# determine points using a F1 type scoring with the last game getting double points
# determine which team would have won and which relegated using the 3 different scoring methods

points = all.groupby(['Season','Team']).agg({'FT Points': np.sum,'HT Points': np.sum,'FT Points Doubled': np.sum})
points.reset_index(inplace=True)
points['rank FT'] = points.groupby('Season')['FT Points'].rank(ascending=False)
points['rank HT'] = points.groupby('Season')['HT Points'].rank(ascending=False)
points['rank FT Doubled'] = points.groupby('Season')['FT Points Doubled'].rank(ascending=False)
points= points[points['Season']!='1993-94'].copy()
points= points[points['Season']!='1994-95'].copy()
points = points.drop(['FT Points','HT Points','FT Points Doubled'], axis=1)
winners = points[(points['rank FT']==1) ]
winners = winners.drop(['rank HT','rank FT Doubled'], axis=1)
winners.rename(columns={'Team':'FT Team'}, inplace=True)
HT_winners = points[(points['rank HT']==1) ]
HT_winners = HT_winners.drop(['rank HT','rank FT Doubled'], axis=1)
HT_winners.rename(columns={'Team':'HT Team'}, inplace=True)
FT_winners_Doubled = points[(points['rank FT Doubled']==1) ]
FT_winners_Doubled = FT_winners_Doubled.drop(['rank HT','rank FT Doubled'], axis=1)
FT_winners_Doubled.rename(columns={'Team':'FT Team D'}, inplace=True)

winners=winners.merge(HT_winners,how='left',on=['Season'])
winners=winners.merge(FT_winners_Doubled,how='left',on=['Season'])

double_impact = winners[winners['FT Team']!= winners['FT Team D']]
print (double_impact)
HT_impact = winners[winners['FT Team']!= winners['HT Team']].reset_index()
print (HT_impact)

plt.bar(HT_impact['Season'],HT_impact['rank FT_y'],tick_label=HT_impact['HT Team'])
plt.show()