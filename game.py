import numpy as np
import copy

np.set_printoptions(precision=2, suppress=True)

pD = np.load("processedData.npy", allow_pickle=True).item()

y             =pD["y"]
sr            =pD["sr"]
beatSamples   =pD["beatSamples"]
beatTime      =pD["beatTime"]
totalBeats    =pD["totalBeats"]
bY            =pD["bY"]
RMS           =pD["RMS"]
mean          =pD["mean"]
median        =pD["median"]
min           =pD["min"]
max           =pD["max"]




#randomizes the top,bottom,left and right
direction=["top","bottom","left","right"]
randirectionIndex=[]
for i in range(totalBeats):
    if(np.abs(bY[i])>RMS):
        num= np.random.randint(3,4)
    elif(np.abs(bY[i])<=RMS):
        num= np.random.randint(1,3)

    randomize=np.random.choice(4,size=(num), replace = False).tolist()                           
    randirectionIndex.append(randomize)

randirection = [[direction[idx] for idx in sub_idx]for sub_idx in randirectionIndex]

beatDirection=[]
for i in range(totalBeats):
    beatDirection.append([beatTime[i].tolist(), randirection[i]])

#print(RMS)
#print(bY[:5]," Amplitudes of beats on times")
#print([[f"{item[0]:.2f}", item[1]] for item in beatDirection[:5]])
print(beatTime[:20]," Beat times")
#print(randirectionIndex[:5])
#print(randirection[:5])

#print(sr)

