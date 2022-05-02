import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


file = pd.read_csv("/Users/rithwikkamalesh/Downloads/archive (3)/nba2021_advanced.csv")

players=file["Player"]

ts_percent=file["TS%"]
PER=file["PER"]




# Question 1
print(max(ts_percent))
print(max(PER))



#Question 2
sortedPlayers=file.sort_values(by="PER",ascending=False)
print(sortedPlayers["Player"].head(10))


#Question 3
print(sortedPlayers["Player"].tail(10))

#Question 4
plt.plot(file["PER"])
plt.plot(file["TS%"])
