import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib notebook

notNeeded = list(range(10))
notNeeded.extend(range(33,37))

religions = ['Christian','Buddhist','Hindu','Jewish','Muslim','Sikh','Other religion','No religion','Religion not stated']
totalReligionKey = 'All categories: Religion'
totalAgeKey = 'All categories: Age'

locations = ["England and Wales", "London","South West"]

df = pd.read_csv('All2011.csv', skiprows=notNeeded)
dataAll = df[df['Age']==totalAgeKey]
totalAll = (int(list(dataAll[totalReligionKey])[0].replace(',','')))

df = pd.read_csv('London2011.csv', skiprows=notNeeded)
dataLondon = df[df['Age']==totalAgeKey]
totalLondon = (int(list(dataLondon[totalReligionKey])[0].replace(',','')))

df = pd.read_csv('SouthWest2011.csv', skiprows=notNeeded)
dataSW = df[df['Age']==totalAgeKey]
totalSW = (int(list(dataSW[totalReligionKey])[0].replace(',','')))

religionFrequency = []
for religion in religions:
    values = []
    values.append(int(list(dataAll[religion])[0].replace(',',''))/totalAll)
    values.append(int(list(dataLondon[religion])[0].replace(',',''))/totalLondon)
    values.append(int(list(dataSW[religion])[0].replace(',',''))/totalSW)
    religionFrequency.append(values)

N = len(religionFrequency[0])
ind = np.arange(N)    # the x locations for the groups
width = 0.5       # the width of the bars: can also be len(x) sequence

p = []
runningTotal = [0,0,0]
for i in range(len(religions)):
    p.append(plt.bar(ind, religionFrequency[i], width, bottom=runningTotal, label=religions[i]))
    runningTotal = [sum(x) for x in zip(runningTotal, religionFrequency[i])]

plt.ylabel('Proportion of the population')
plt.yticks([0,0.5,1],['0','50%','100%'])
plt.title('Religious diversity by location in the UK')
plt.xticks(ind, locations, rotation='30')
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles[::-1], labels[::-1], loc=5, bbox_to_anchor=(1.6, 0.5), ncol=1)
plt.subplots_adjust(left=0.2, right=0.7, top=0.9, bottom=0.2)
plt.show()
