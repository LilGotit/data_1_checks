import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

dataframe = pd.read_csv("assets/fireInjuries.csv")

Total_Injuries = dataframe["Total_Injuries"]
Injury_Date = pd.to_datetime(dataframe["Injury_Date"], errors = "coerce")


plt.plot(Injury_Date, Total_Injuries, marker="^")
plt.show()