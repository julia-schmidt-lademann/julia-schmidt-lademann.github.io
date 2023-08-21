# -*- coding: utf-8 -*-

# # !pip install nfl_data_py
# import nfl_data_py as nfl
import pandas as pd
import matplotlib.pyplot as plt
"""
Here I was identifying what data is available in the nfl_data_py dataset. However the size of the data was rendering the processing very slow, and I didn't need the data, so this is kept to show my work but not currently used.
"""
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# # pd.set_option('display.width', None)
# #https://pypi.org/project/nfl-data-py/

# pbp_2022 = nfl.import_pbp_data([2022])
# weekl_2022 = nfl.import_weekly_data([2022])
# ids = nfl.import_ids() # join to weekly using ids.gsis_id=weekl_2022.player_id
# depth = nfl.import_depth_charts([2022]) # # join to weekly using depth.gsis_id=weekl_2022.player_id
# injuries = nfl.import_injuries([2022])
# # qbr = nfl.import_qbr([2022], level=nfl, frequency='weekly')

# #### ideas for things we might want to look at from pbp:
# # -- offense_personnel ""1 RB, 2 TE, 2 WR - most frequent lineup run
# # -- offense_players ""47969;53059;42500;46279;53575;48364; - share of plays a player was on the field at (vs targets?)
# # -- target_share/air_yards_share 0.035714

# #### calculate hppr points and join the tables together
# # print (ids[(ids["name"]=="Tom Brady")].head())
# weekl_2022['fantasy_points_hppr'] = weekl_2022['fantasy_points_ppr']-(weekl_2022['receptions']/2)
# weekl_2022=weekl_2022.merge(ids, left_on='player_id', right_on='gsis_id', how='left')
# weekl_2022=weekl_2022.merge(depth, left_on=['player_id','week','season'], right_on=['gsis_id','week','season'], how='left')

# #### pivot data to allow joining to draft dataset
# weekly_results = weekl_2022[['player_id','name','position_x','recent_team','season','week','fantasy_points_hppr']].copy()
# weekly_results['dupl'] = weekly_results.duplicated()
# weekly_results=weekly_results[(weekly_results["dupl"]==False)]
# weekly_results['week'] =  'week ' + weekly_results['week'].astype(str)
# weekly_results.fantasy_points_hppr = weekly_results.fantasy_points_hppr.round(2)
# weekly_results=weekly_results.pivot(index=['player_id','name','position_x','recent_team','season',], columns='week', values='fantasy_points_hppr')
# weekly_results=weekly_results.fillna(0)


import numpy as np
import os

 ####  PART 1 ####
    #### pull all files together into one place
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
paths = ['https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_00.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_01.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_02.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_03.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_04.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_05.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_06.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_07.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_08.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_09.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_10.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_11.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_12.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_13.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_14.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_15.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_16.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_17.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_18.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_19.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_20.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_21.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_22.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_23.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_24.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_25.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/fast/part_26.csv'


         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/mixed/part_01.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/mixed/part_02.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/mixed/part_03.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/mixed/part_04.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/mixed/part_05.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/mixed/part_06.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/mixed/part_07.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/regular_season/mixed/part_08.csv'


         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/post_season/finals/part_00.csv'

         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/post_season/semifinals/part_00.csv'

         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/post_season/quarterfinals/part_01.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/post_season/quarterfinals/part_02.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/post_season/quarterfinals/part_03.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/post_season/quarterfinals/part_04.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/post_season/quarterfinals/part_05.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/post_season/quarterfinals/part_06.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/post_season/quarterfinals/part_07.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/post_season/quarterfinals/part_08.csv'
         ,'https://raw.githubusercontent.com/fantasydatapros/best-ball-data-bowl/master/data/2022/post_season/quarterfinals/part_09.csv'


         ]
df = pd.DataFrame()

for x in paths:
    df_append = pd.read_csv(x)

    # print(reading(x).shape)
    df = pd.concat([df,df_append],ignore_index=True)
# df.reset_index(drop=True)
# final_weekly_performance_data = weekly_results.copy()

"""# Creating a single dataset combining draft and performance data, currently commented out but readily available when needed."""
print ("Ingestion done")
# # this resets the data to the original without requiring re-ingesting
df2=df.copy() ###.merge(final_weekly_performance_data, left_on='player_name', right_on='name', how='outer')
# # print (df2.head())

# df2['regular_fantasy_season_points'] = df2['week 1'] + df2['week 2'] + df2['week 3'] + df2['week 4'] + df2['week 5'] + df2['week 6'] + df2['week 7'] + df2['week 8'] + df2['week 9'] + df2['week 10'] + df2['week 11'] + df2['week 12'] + df2['week 13'] + df2['week 14']
# df2['full_season_fantasy_points'] = df2['week 1'] + df2['week 2'] + df2['week 3'] + df2['week 4'] + df2['week 5'] + df2['week 6'] + df2['week 7'] + df2['week 8'] + df2['week 9'] + df2['week 10'] + df2['week 11'] + df2['week 12'] + df2['week 13'] + df2['week 14'] + df2['week 15'] + df2['week 16'] + df2['week 17']

# pbp_clean = pbp_2022[['id','game_id','play_type','play_type_nfl','down','week','season','replay_or_challenge_result','pass_length','ydstogo',
                      # 'yardline_100','air_yards','no_score_prob','penalty','penalty_type','penalty_team','possession_team',
                      # 'offense_formation','offense_personnel','offense_players','drive_end_transition','special_teams_play','st_play_type','qb_scramble']].copy()
# # df[df['A'].str.contains("hello")] use this to separate offense_players
# print (pbp_clean.head())
# # per player count of distinct game IDs
# # per player of special team plays as % of all plays (especially if low on depth chart)
# # per player count of times they are in offense players EVEN IF NOT ON THEIR ROW!
# # ID and 3rd down plays they carried & success rate

""" #### Part 2 ####
    ### add columns

    # per pick a column for target share
    # column for which players are elite (ADP in the first 3 rounds)

    # per team a column for points scored + total + total until fantasy post-season#
    # team structure

  # Ideas:
  - value vs result of rookie that is top of depth chart?
  - players used on 3rd and 1, impact on advancement rate
  - teams that go for it on 4th and <4 - advancement rate impact
  - per week and team determine most frequently used offensive lineup.
  - correlation with points scored per position per week (I want WRs that play in this offensive lineup most of the time, and RBs that are in this lineup)
  -  who was misjudged and do they have common traits
  - payers who play special teams get less?
  - team structure best for progressing vs team structure best for going to final

### APD Value
- for what position is ADP value the most valuable
- how many rounds of ADP value calculation give the best indicator for advancement rate
- ADP value coefficient by round
- closing line value


#### Data observations
- final has its own draft id
- dates are only tracked in regular season
- a team progressing will keep the same tournament entry id
"""

res = df2.groupby('tournament_entry_id').agg({'tournament_round_number': max})
df2 = df2[(df2["tournament_round_number"]==1)]
df2.reset_index()
df2 = df2.drop('tournament_round_number', axis=1)
df2=df2.merge(res, left_on='tournament_entry_id', right_on='tournament_entry_id', how='inner')

"""- Add ADP value per pick
- sum up adp value after each round
- aggregate table to drafts
"""

df2['adp_value']=df2['overall_pick_number']-round(df2['projection_adp'],0)
""" Values provided by existing analysis by Mike Leone in his Best Ball Mania Manifesto."""
draft_capital={1: 133,
2: 132, 3: 130, 4: 129, 5: 128, 6: 127, 7: 125, 8: 124, 9: 123,
10: 122,11: 121, 12: 119,13: 118, 14: 117, 15: 116, 16: 115, 17: 114,
18: 112, 19: 111, 20: 110, 21: 109, 22: 108, 23: 107, 24: 106, 25: 104,
26: 103, 27: 102, 28: 101, 29: 100, 30: 99, 31: 98, 32: 97, 33: 96,
34: 95, 35: 94, 36: 93, 37: 92, 38: 90, 39: 89, 40: 88, 41: 87,
42: 86, 43: 85, 44: 84, 45: 83, 46: 82, 47: 81,
48: 80, 49: 79, 50: 78, 51: 78, 52: 77, 53: 76, 54: 75, 55: 74,
56: 73, 57: 72, 58: 71, 59: 70, 60: 69, 61: 68, 62: 67, 63: 66,
64: 66, 65: 65, 66: 64, 67: 63, 68: 62, 69: 61, 70: 60, 71: 60,
72: 59, 73: 58, 74: 57, 75: 56, 76: 55, 77: 55, 78: 54, 79: 53,
80: 52, 81: 51, 82: 51, 83: 50, 84: 49, 85: 48, 86: 48, 87: 47,
88: 46, 89: 45, 90: 45, 91: 44, 92: 43, 93: 42, 94: 42, 95: 41,
96: 40, 97: 40, 98: 39, 99: 38, 100: 38, 101: 37, 102: 36, 103: 36,
104: 35, 105: 34, 106: 34, 107: 33, 108: 32, 109: 32, 110: 31, 111: 31,
112: 30, 113: 29, 114: 29, 115: 28, 116: 28, 117: 27, 118: 27, 119: 26,
120: 25, 121: 25, 122: 24, 123: 24, 124: 23, 125: 23, 126: 22, 127: 22,
128: 21, 129: 21, 130: 20, 131: 20, 132: 19, 133: 19, 134: 18, 135: 18,
136: 17, 137: 17, 138: 17, 139: 16, 140: 16, 141: 15, 142: 15, 143: 14,
144: 14, 145: 14, 146: 13, 147: 13, 148: 12, 149: 12, 150: 12, 151: 11,
152: 11, 153: 11, 154: 10, 155: 10, 156: 9, 157: 9, 158: 9, 159: 9,
160: 8, 161: 8, 162: 8, 163: 7, 164: 7, 165: 7, 166: 6, 167: 6,
168: 6, 169: 6, 170: 5, 171: 5, 172: 5, 173: 5, 174: 4, 175: 4,
176: 4, 177: 4, 178: 4, 179: 3, 180: 3, 181: 3, 182: 3, 183: 3,
184: 2, 185: 2, 186: 2, 187: 2, 188: 2, 189: 2, 190: 2, 191: 1,
192: 1, 193: 1, 194: 1, 195: 1, 196: 1, 197: 1, 198: 1, 199: 1,
200: 0, 201: 0, 202: 0, 203: 0, 204: 0, 205: 0, 206: 0, 207: 0,
208: 0, 209: 0, 210: 0, 211: 0, 212: 0, 213: 0, 214: 0, 215: 0, 216: 0,
}

df2['draft_capital'] = df['overall_pick_number'].map(draft_capital)
df2['adp_value_weighted']=df2['adp_value']*df2['draft_capital']

""" These columns show how many picks before or after Average Draft Pick position a player is picked. this is called the ADP Value"""

res = df2.copy()
# res=res.rename(columns={"adp_value": "adp_value_18"})
res['adp_value_17'] = np.where (res['team_pick_number']<18,res['adp_value'],0)
res['adp_value_16'] = np.where (res['team_pick_number']<17,res['adp_value'],0)
res['adp_value_15'] = np.where (res['team_pick_number']<16,res['adp_value'],0)
res['adp_value_14'] = np.where (res['team_pick_number']<15,res['adp_value'],0)
res['adp_value_13'] = np.where (res['team_pick_number']<14,res['adp_value'],0)
res['adp_value_12'] = np.where (res['team_pick_number']<13,res['adp_value'],0)
res['adp_value_11'] = np.where (res['team_pick_number']<12,res['adp_value'],0)
res['adp_value_10'] = np.where (res['team_pick_number']<11,res['adp_value'],0)
res['adp_value_09'] = np.where (res['team_pick_number']<10,res['adp_value'],0)
res['adp_value_08'] = np.where (res['team_pick_number']<9,res['adp_value'],0)
res['adp_value_07'] = np.where (res['team_pick_number']<8,res['adp_value'],0)
res['adp_value_06'] = np.where (res['team_pick_number']<7,res['adp_value'],0)
res['adp_value_05'] = np.where (res['team_pick_number']<6,res['adp_value'],0)
res['adp_value_04'] = np.where (res['team_pick_number']<5,res['adp_value'],0)
res['adp_value_03'] = np.where (res['team_pick_number']<4,res['adp_value'],0)
res['adp_value_02'] = np.where (res['team_pick_number']<3,res['adp_value'],0)
res['adp_value_01'] = np.where (res['team_pick_number']<2,res['adp_value'],0)
res['adp_value_QB'] = np.where (res['position_name']=="QB",res['adp_value'],0)
res['adp_value_RB'] = np.where (res['position_name']=="RB",res['adp_value'],0)
res['adp_value_WR'] = np.where (res['position_name']=="WR",res['adp_value'],0)
res['adp_value_TE'] = np.where (res['position_name']=="TE",res['adp_value'],0)
res=res.rename(columns={"adp_value": "adp_value_18"})
res=res.rename(columns={"adp_value_weighted": "adp_value_18_weighted"})

res = res.groupby('tournament_entry_id').agg({'adp_value_QB': sum,'adp_value_RB': sum,'adp_value_TE': sum,'adp_value_WR': sum,'adp_value_18': sum,'adp_value_17': sum,'adp_value_16': sum,'adp_value_15': sum,'adp_value_14': sum,'adp_value_13': sum,'adp_value_12': sum,'adp_value_11': sum,'adp_value_10': sum,'adp_value_09': sum,'adp_value_08': sum,'adp_value_07': sum,'adp_value_06': sum,'adp_value_05': sum,'adp_value_04': sum,'adp_value_03': sum,'adp_value_02': sum,'adp_value_01': sum})
df3 = df2.groupby('tournament_entry_id').agg({'draft_time': max,'clock': max,'pick_order': max,'tournament_round_number': max})
df3.reset_index()
df3=df3.merge(res, left_on='tournament_entry_id', right_on='tournament_entry_id', how='inner')


""" These columns show how many picks before or after Average Draft Pick position a player is picked, weighted by the Capital as indicated by the pverall pick number"""

res = df2.copy()
res['adp_value_17_weighted'] = np.where (res['team_pick_number']<18,res['adp_value_weighted'],0)
res['adp_value_16_weighted'] = np.where (res['team_pick_number']<17,res['adp_value_weighted'],0)
res['adp_value_15_weighted'] = np.where (res['team_pick_number']<16,res['adp_value_weighted'],0)
res['adp_value_14_weighted'] = np.where (res['team_pick_number']<15,res['adp_value_weighted'],0)
res['adp_value_13_weighted'] = np.where (res['team_pick_number']<14,res['adp_value_weighted'],0)
res['adp_value_12_weighted'] = np.where (res['team_pick_number']<13,res['adp_value_weighted'],0)
res['adp_value_11_weighted'] = np.where (res['team_pick_number']<12,res['adp_value_weighted'],0)
res['adp_value_10_weighted'] = np.where (res['team_pick_number']<11,res['adp_value_weighted'],0)
res['adp_value_09_weighted'] = np.where (res['team_pick_number']<10,res['adp_value_weighted'],0)
res['adp_value_08_weighted'] = np.where (res['team_pick_number']<9,res['adp_value_weighted'],0)
res['adp_value_07_weighted'] = np.where (res['team_pick_number']<8,res['adp_value_weighted'],0)
res['adp_value_06_weighted'] = np.where (res['team_pick_number']<7,res['adp_value_weighted'],0)
res['adp_value_05_weighted'] = np.where (res['team_pick_number']<6,res['adp_value_weighted'],0)
res['adp_value_04_weighted'] = np.where (res['team_pick_number']<5,res['adp_value_weighted'],0)
res['adp_value_03_weighted'] = np.where (res['team_pick_number']<4,res['adp_value_weighted'],0)
res['adp_value_02_weighted'] = np.where (res['team_pick_number']<3,res['adp_value_weighted'],0)
res['adp_value_01_weighted'] = np.where (res['team_pick_number']<2,res['adp_value_weighted'],0)
res['adp_value_QB_weighted'] = np.where (res['position_name']=="QB",res['adp_value_weighted'],0)
res['adp_value_RB_weighted'] = np.where (res['position_name']=="RB",res['adp_value_weighted'],0)
res['adp_value_WR_weighted'] = np.where (res['position_name']=="WR",res['adp_value_weighted'],0)
res['adp_value_TE_weighted'] = np.where (res['position_name']=="TE",res['adp_value_weighted'],0)
res=res.rename(columns={"adp_value_weighted": "adp_value_18_weighted"})

res = res.groupby('tournament_entry_id').agg({'adp_value_QB_weighted': sum,'adp_value_RB_weighted': sum,'adp_value_TE_weighted': sum,'adp_value_WR_weighted': sum,'adp_value_18_weighted': sum,'adp_value_17_weighted': sum,'adp_value_16_weighted': sum,'adp_value_15_weighted': sum,'adp_value_14_weighted': sum,'adp_value_13_weighted': sum,'adp_value_12_weighted': sum,'adp_value_11_weighted': sum,'adp_value_10_weighted': sum,'adp_value_09_weighted': sum,'adp_value_08_weighted': sum,'adp_value_07_weighted': sum,'adp_value_06_weighted': sum,'adp_value_05_weighted': sum,'adp_value_04_weighted': sum,'adp_value_03_weighted': sum,'adp_value_02_weighted': sum,'adp_value_01_weighted': sum})

df3=df3.merge(res, left_on='tournament_entry_id', right_on='tournament_entry_id', how='inner')


df_barchart = pd.DataFrame(columns = ["Round", "Correlation"])
df_barchart.loc[len(df_barchart.index)] = ['adp_value_01_weighted',df3['adp_value_01_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_01',df3['adp_value_01'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_02_weighted',df3['adp_value_02_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_02',df3['adp_value_02'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_03_weighted',df3['adp_value_03_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_03',df3['adp_value_03'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_04_weighted',df3['adp_value_04_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_04',df3['adp_value_04'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_05_weighted',df3['adp_value_05_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_05',df3['adp_value_05'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_06_weighted',df3['adp_value_06_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_06',df3['adp_value_06'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_07_weighted',df3['adp_value_07_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_07',df3['adp_value_07'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_08_weighted',df3['adp_value_08_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_08',df3['adp_value_08'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_09_weighted',df3['adp_value_09_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_09',df3['adp_value_09'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_10_weighted',df3['adp_value_10_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_10',df3['adp_value_10'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_11_weighted',df3['adp_value_11_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_11',df3['adp_value_11'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_12_weighted',df3['adp_value_12_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_12',df3['adp_value_12'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_13_weighted',df3['adp_value_13_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_13',df3['adp_value_13'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_14_weighted',df3['adp_value_14_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_14',df3['adp_value_14'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_15_weighted',df3['adp_value_15_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_15',df3['adp_value_15'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_16_weighted',df3['adp_value_16_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_16',df3['adp_value_16'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_17_weighted',df3['adp_value_17_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_17',df3['adp_value_17'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_18_weighted',df3['adp_value_18_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_18',df3['adp_value_18'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_TE_weighted',df3['adp_value_TE_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_TE',df3['adp_value_TE'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_WR_weighted',df3['adp_value_WR_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_WR',df3['adp_value_WR'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_QB_weighted',df3['adp_value_QB_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_QB',df3['adp_value_QB'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_RB_weighted',df3['adp_value_RB_weighted'].corr(df3['tournament_round_number'])]
df_barchart.loc[len(df_barchart.index)] = ['adp_value_RB',df3['adp_value_RB'].corr(df3['tournament_round_number'])]

       # findings:
       # - weighting gives the correlation (i.e. prediction value) a ~17% boost
       # - Round giving the best acuracy is 13, but from 9 onwards there is really not much improvement. could save time
       # - correlation by position is overall lower than first 9 or 13 rounds; but weighting has a much bigger impact

# assuming we use rounds 1-14. as this is the accepted standard
# what teams would fall into different bins for weighted vs unweighted ADP.
# accuracy may not be massively improved but a better selection of teams may be forecasted
# df4 = df3[['draft_time', 'clock', 'pick_order', 'tournament_round_number','adp_value_14','adp_value_14_weighted']].copy()
# df4['binned_variable'] = pd.qcut(df['adp_value_14'], 10, labels=False)
# df4['binned_weighted_variable'] = pd.qcut(df['adp_value_14_weighted'], 10, labels=False)
#
print (df_barchart.head())
#
# res2 = df4.groupby(['binned_variable','binned_weighted_variable'])['binned_variable'].count()
# print (res2)

df_barchart.plot.bar(x="Round", y="Correlation", title="Advancement rate correlation by ADO per round")
plt.show(block=True)