#Import Libraries
import matplotlib.pyplot as plt
import pandas as pd
# Read DataFrame ( and parse axis dates)
df = pd.read_csv("haz_ping.csv", usecols=['timestamp','ping'])
# Use Date as index
df.set_index('timestamp',inplace=True)
# Plot & show
plt.plot(df['ping'])
plt.show()
