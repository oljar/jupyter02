import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({"date": ["1", "2", "3", "4"],
                   "column1": [555,525,532,585],
                   "column2": [50,48,49,51],
                    "column3": [600,650,700,750]

                   })

# ax = sns.lineplot()
# ax1 = ax.twinx()
# ax2 = ax.twinx()
#
#
#
# ax1.figure.legend()
#
# ax1 = sns.lineplot(data=df.column2, color="b", ax=ax1)
# ax2 = sns.lineplot(data=df.column1, color="c", ax=ax2)
ax = plt.twinx()
ay = plt.twiny()

ax.grid(which='major', axis='both', linestyle='solid')
ay.grid(which='major', axis='both', linestyle='solid')


sns.lineplot(data=df.column1, color="g",ax=ax)

ax3 = plt.twinx()

sns.lineplot(data=df.column2, color="b", ax=ax)
aaa=sns.scatterplot(data=df.column3, color="red", ax=ax)
aaa.set_title('sample')
plt.show()