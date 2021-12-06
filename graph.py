import numpy as np
import matplotlib.pyplot as plt

timeRandom = np.array([0.35,1.18,2.78,3.92,9.26,15.11,27.22,44.07])
timeRR = np.array([0.36,1.13,1.77,3.10,8.38,13.70,26.94,40.18])
timeRegRR = np.array([0.37,1.2,1.79,3.08,7.94,13.44,25.67,38.65])
timeWeightRR = np.array([1.3,1.32,2.77,4.59,12.00,19.88,41.45,58.25])
timeLeastLatency = np.array([6.14,3.35,3.95,5.19,10.349,15.36,28.18,40.53])
timeLeastConnection = np.array([1.85,2.20,3.24, 4.96,11.71,18.28,32.53,47.29])
users =   np.array([1,10,50,100,300,500,1000,1500])


y_pos = np.arange(len(users))

fig = plt.figure(figsize=(15,8))

plt.bar(y_pos-0.2, timeRandom,align='center', width = 0.1,color='black')
plt.bar(y_pos-0.1, timeRR,align='center', width = 0.1,color='pink')
plt.bar(y_pos, timeRegRR,align='center', width = 0.1,color='blue')
plt.bar(y_pos+0.1, timeWeightRR,align='center', width = 0.1,color='green')
plt.bar(y_pos+0.2, timeLeastLatency, align='center', width = 0.1,color='purple')
plt.bar(y_pos+0.3, timeLeastConnection,align='center', width = 0.1,color='grey')

colors = {'Random' : 'black', 'RoundRobin' : 'pink', 'RegionRR':'blue', 
          'WeightedRR':'green', 'LeastLatency':'purple', 'LeastConnection':'grey'} 
labels = list(colors.keys())
handles =[plt.Rectangle((0,0),1,1, color = colors[label]) for label in labels]
plt.legend(handles, labels)
plt.title("Load Balancing Policies Performance")
plt.xticks(y_pos,users)
plt.xlabel("Users")
plt.ylabel("Time Elapsed")
