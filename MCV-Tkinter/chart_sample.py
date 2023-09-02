import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({"a": [1, 2, 3, 10],
                   "b": [555,525,532,585],
                   "c": [50,48,49,51],
                   "d": [600,650,700,750]

                   })

# ax = sns.lineplot()
# ax1 = ax.twinx()
# ax2 = ax.twinx()
#
#
#

#
# ax1 = sns.lineplot(data=df.column2, color="b", ax=ax1)
# ax2 = sns.lineplot(data=df.column1, color="c", ax=ax2)
# ax = plt.twinx()
# ay = plt.twiny()
#
# ax.grid(which='major', axis='both', linestyle='solid')
# ay.grid(which='major', axis='both', linestyle='solid')
#
#
# sns.lineplot(data=df.column1, color="g",ax=ax, label = 'wwwww')
#
#
# sns.lineplot(data=df.column2, color="b", ax=ax, label = 'jjjj')
# sns.scatterplot(data=df.column3, color="red", ax=ax,label = 'kjhkhk')
#
#
# plt.title("sample")
# plt.ylabel("oś y")
#
# plt.show()

import numpy as np; np.random.seed(42)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.DataFrame({"w": [1,100,500,1000],
                    "fi":[200,500,800,1100]})
df2 = pd.DataFrame({"z": np.sort(np.random.rand(30)),
                    "g": 500-0.1*np.sort(np.random.rayleigh(20,size=30))**2})

fig, ax = plt.subplots()


#
# sns.regplot(x="w", y="fi", data=df1, ax=ax,label = 'wwwww1')
sns.regplot(x="z", y="g", data=df2, ax=ax, label = 'lwwwww')
sns.lineplot(x="a", y="b", data=df, color="g",ax=ax,linewidth=1, label = 'wwwww')
sns.lineplot(x="c", y= "d", data=df, color="c", ax=ax,linewidth=1, label = 'wwwww')
sns.scatterplot(x="w", y="fi", data=df1,c ="orange",s = 50, alpha=0.3,edgecolors='none',label = 'dsfdss')


ax.set_xlabel('Annual rainfall (mm)')

ax.set_ylabel('Likelihood of occurrence')

# ax.scatter(df1.w, df1.fi,c ="blue",linewidths = 2,marker ="^", edgecolor ="red",s = 10)




# Show the major grid and style it slightly.
ax.grid(which='major', color='#DDDDDD', linewidth=1.2)
# Show the minor grid as well. Style it in very light gray as a thin,
# dotted line.
ax.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=1)
# Make the minor ticks and gridlines show.
ax.minorticks_on()



# ax2.legend(handles=[a.lines[0] for a in [ax,ax2]],
#            labels=["f", "g"])


plt.show()

# plt.scatter(x2, y2, c="yellow",
#             linewidths=2,
#             marker="^",
#             edgecolor="red",
#             s=200)