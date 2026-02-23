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
direction=["Top","Bottom","Left","Right"]
randirectionIndex=[]
for i in range(totalBeats):
    if(np.abs(bY[i])>RMS):
        num= np.random.randint(3,4)
    elif(np.abs(bY[i])<=RMS):
        num= np.random.randint(1,3)

    randomize=np.random.choice(4,size=(num), replace = False).tolist()                           
    randirectionIndex.append(randomize)

"""
randirection=copy.deepcopy(randirectionIndex)
for i in range(len(randirectionIndex)):
    for j in range(len(randirectionIndex[i])):
        match randirectionIndex[i][j]:
            case 0:
                randirection[i][j]=direction[0]
            case 1:
                randirection[i][j]=direction[1]
            case 2:
                randirection[i][j]=direction[2]
            case 3:
                randirection[i][j]=direction[3]
"""
randirection = [[direction[idx] for idx in sub_idx]for sub_idx in randirectionIndex]

beatDirection=[]
for i in range(totalBeats):
    beatDirection.append([beatTime[i].tolist(), randirection[i]])

print(beatTime[:5]," Beat times")
print(bY[:5]," Amplitudes of beats on times")
print([[f"{item[0]:.2f}", item[1]] for item in beatDirection[:5]])