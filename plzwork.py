from mpl_toolkits import mplot3d

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

AplayerStatsClean = pd.read_csv('C:/Users/matth/Documents/python/csv/playerstatsA.csv')
APoints = AplayerStatsClean['PTS']
ARebounds = AplayerStatsClean['TRB']
AAssists = AplayerStatsClean['AST']

BplayerStatsClean = pd.read_csv('C:/Users/matth/Documents/python/csv/playerstatsB.csv')
BPoints = BplayerStatsClean['PTS']
BRebounds = BplayerStatsClean['TRB']
BAssists = BplayerStatsClean['AST']

CplayerStatsClean = pd.read_csv('C:/Users/matth/Documents/python/csv/playerstatsC.csv')
CPoints = CplayerStatsClean['PTS']
CRebounds = CplayerStatsClean['TRB']
CAssists = CplayerStatsClean['AST']

DplayerStatsClean = pd.read_csv('C:/Users/matth/Documents/python/csv/playerstatsD.csv')
DPoints = DplayerStatsClean['PTS']
DRebounds = DplayerStatsClean['TRB']
DAssists = DplayerStatsClean['AST']

EplayerStatsClean = pd.read_csv('C:/Users/matth/Documents/python/csv/playerstatsE.csv')
EPoints = EplayerStatsClean['PTS']
ERebounds = EplayerStatsClean['TRB']
EAssists = EplayerStatsClean['AST']

PG = "PG"
SG = "SG"
SF = "SF"
PF = "PF"
C = "C"

ax.scatter(APoints, AAssists, ARebounds, marker='o', label=PG)
ax.scatter(BPoints, BAssists, BRebounds, marker='^', label=SG)
ax.scatter(CPoints, CAssists, CRebounds, marker='o', label=SG)
ax.scatter(DPoints, DAssists, DRebounds, marker='o', label=PF)
ax.scatter(EPoints, EAssists, ERebounds, marker='o', label=C)

ax.set_xlabel('Points')
ax.set_ylabel('Assists')
ax.set_zlabel('Rebounds')

plt.show()