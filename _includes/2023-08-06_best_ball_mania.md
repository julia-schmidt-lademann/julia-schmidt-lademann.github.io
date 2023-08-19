<h2 style="text-align: center;">[Best Ball Data Bowl](https://github.com/julia-schmidt-lademann/julia-schmidt-lademann.github.io/blob/main/_includes/best_ball.py)</h2>

#### Plan:
- In July 2023 data covering past fantasy draft data was made available.
- In combination with the nfl_data_py library I wanted to explore the available data and identify interesting learnings. 
- I decided not to include nfl_data_py, as that data is not available when the draft is being done, and therefore any insights from it are not replicable at the time of a draft
- My final decision I pursued was to evaluate the ability of ADP Value to predict advancement rate.
- I used Mike Leone's data from the [Best Ball Mania Manifesto](https://establishtherun.com/best-ball-mania-manifesto-a-guide-to-winning-big-on-underdog-fantasy/) to weight APD value. It means that value in early rounds are more valuable than value gained in later rounds.

#### Process:
- Import & concat data
- Identify which teams advance to the next round
- Calculate adp value for each pick made at the time of the pick
- Give each ADP value a weighting. 
- Calculate ADP value and weighted ADP value after each round and by player position
- Create the correlation between the ADP value and the round achieved
- Create groupings to see what decile ADP value at round 14 (widely accepted standard) falls into
- Compare the groupings between the weighted and unweighted ADP values

#### Findings:
- Weighting gives the correlation (i.e. prediction value) a ~18% drop in correlation. This seems wildly unrealistic. 
- Round giving the best accuracy is 13, but from 9 onwards there is really not much improvement. 
- Correlation by position is overall lower than first 9 or 13 rounds; but weighting has a much bigger negative impact. 

![Correlation](https://github.com/julia-schmidt-lademann/julia-schmidt-lademann.github.io/blob/main/_includes/BBDB.JPG?raw=true)

#### Next steps:
- I want to predict if a team with a certain value will make the (fantasy) playoffs. 
- Will weighting result in better accuracy of predicting this?
- If a team falls into a very different decile when weighting ADP, what does that tell us, and what commonalities are there between these teams.

----------------------------------------------------------------------------------------------------

