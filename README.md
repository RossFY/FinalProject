# FinalProject
# Author: Ye Fang
# CWID: 10431002
# purpose: data analysis
# method: K-nearest neighbors algorithm
# language: Python
# dataset: https://www.kaggle.com/drgilermo/nba-players-stats-20142015

This project is about data analysis. I am going to use k-nearest neighbors algorithm to analyze the NBA players stats. 

Through the players stats, we can predict which position the players are acting. There are 5 positions on the court, point guard(PG), shooting guard(SG), small forward(SF), power forward(PF) and center(C).

Different positions play different roles, PG often control the ball and pass to his teammates in order to finishing scoring. SG is often responsible for scoring, that's why call them shooting guard. SF sometimes are responsible for scoring, and sometimes are responsible for organization. PF sometimes are responsible for rebounds, and sometimes are responsible for scoring. C are often responsible for rebounds and defence.

In the dataset, I am going to use the following columns to finish my project:
● Height: Height of the player
● Weight: Weight of the player
● Pos: Position of the player
● PTSPM: Points Per Minutes
● ASTPM: Assists Per Minutes
● STLPM: Steals Per Minutes
● BLKPM: Blocks Per Minutes
● DREBPM: Defensive Rebound Per Minutes
● OREBPM: Offensive Rebound Per Minutes
● AST/TOV: The Proportion of Assists and Turnovers
● STL/TOV: The Proportion of Steals and Turnovers

These data will clearly show which positions are the players act.

However, as we know, some positions may have the similiar data. For example, SG and SF may be hard to recognize, they may have the similiar data on points or rebounds. Due to this situation, the correct rate will not be really high, which means that some players may be predicted to another position. Though the correct rate isn't really high, we can still save much time on finding the most suitable position for a player.

Practical Used:
● Imagine that we have a list of players stats of the rookies(the freshmen in NBA).
● We can easily find the most suitable position for a rookie.
