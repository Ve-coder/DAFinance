import matplotlib.pyplot as plt
fig, ax = plt.subplots()
import pandas as pd

data= pd.read_csv("netflix_titles.csv")

x = data["title"].head(10)
y1 = data["country"].head(10)
ax.plot(x, y1, marker="v", color="green", linestyle="dashdot")
ax.plot(x, y1)
plt.show()
print(data.head())
