import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

dataframe = pd.read_csv("assets/fireInjuries.csv")
ID = dataframe["ID"]
Total_Injuries = dataframe["Total_Injuries"]

plt.plot(ID, Total_Injuries, marker="^")
plt.show()