from sklearn.datasets import load_breast_cancer

import pandas as pd
from pandas.io.json import json_normalize

import seaborn as sns

import matplotlib.pyplot as plt

import json

#df = pd.read_json('data/20210402_NewHaven01-02.json')

with open('data/20210402_NewHaven01-02.json') as jsonfile:
    data = json.load(jsonfile)    

flat_data = []

for d in data:

    sync = d["sync"]
    hardware = d["hardware"]
    
    flow = d["flow"]

    mic = d["files"]["mic_volume"]

    delta = sync["delta"]
    backing_track_position = sync["backing_track_position"]
    chorus_id = sync["chorus_id"]

    bitalino = hardware["bitalino"]
    eegT3 = hardware["brainbit"]["eeg-T3"] 
    eegT4 = hardware["brainbit"]["eeg-T4"]
    eeg01 = hardware["brainbit"]["eeg-O1"]
    eeg02 = hardware["brainbit"]["eeg-O2"]

    nosex = hardware["skeleton"]["nose"]["x"]
    nosey = hardware["skeleton"]["nose"]["y"]
    noseconf = hardware["skeleton"]["nose"]["confidence"]

    neckx = hardware["skeleton"]["neck"]["x"]
    necky = hardware["skeleton"]["neck"]["y"]
    neckconf = hardware["skeleton"]["neck"]["confidence"]

    r_shoudlerx = hardware["skeleton"]["r_shoudler"]["x"]
    r_shoudlery = hardware["skeleton"]["r_shoudler"]["y"]
    r_shoudlerconf = hardware["skeleton"]["r_shoudler"]["confidence"]

    r_elbowx = hardware["skeleton"]["r_elbow"]["x"]
    r_elbowy = hardware["skeleton"]["r_elbow"]["y"]
    r_elbowconf = hardware["skeleton"]["r_elbow"]["confidence"]

    r_wristx = hardware["skeleton"]["r_wrist"]["x"]
    r_wristy = hardware["skeleton"]["r_wrist"]["y"]
    r_wristconf = hardware["skeleton"]["r_wrist"]["confidence"]

    r_earx = hardware["skeleton"]["r_ear"]["x"]
    r_eary = hardware["skeleton"]["r_ear"]["y"]
    r_earconf = hardware["skeleton"]["r_ear"]["confidence"]

    r_eyex = hardware["skeleton"]["r_eye"]["x"]
    r_eyey = hardware["skeleton"]["r_eye"]["y"]
    r_eyeconf = hardware["skeleton"]["r_eye"]["confidence"]

    l_shoudlerx = hardware["skeleton"]["l_shoudler"]["x"]
    l_shoudlery = hardware["skeleton"]["l_shoudler"]["y"]
    l_shoudlerconf = hardware["skeleton"]["l_shoudler"]["confidence"]

    l_elbowx = hardware["skeleton"]["l_elbow"]["x"]
    l_elbowy = hardware["skeleton"]["l_elbow"]["y"]
    l_elbowconf = hardware["skeleton"]["l_elbow"]["confidence"]

    l_wristx = hardware["skeleton"]["l_wrist"]["x"]
    l_wristy = hardware["skeleton"]["l_wrist"]["y"]
    l_wristconf = hardware["skeleton"]["l_wrist"]["confidence"]

    l_earx = hardware["skeleton"]["l_ear"]["x"]
    l_eary = hardware["skeleton"]["l_ear"]["y"]
    l_earconf = hardware["skeleton"]["l_ear"]["confidence"]

    l_eyex = hardware["skeleton"]["l_eye"]["x"]
    l_eyey = hardware["skeleton"]["l_eye"]["y"]
    l_eyeconf = hardware["skeleton"]["l_eye"]["confidence"]

    flat_data.append([flow,
        mic, 
        delta, backing_track_position, chorus_id, 
        bitalino, 
        eegT3, eegT4, eeg01, eeg02, 
        r_shoudlerx, r_shoudlery, r_shoudlerconf, 
        r_elbowx, r_elbowy, r_elbowconf, 
        r_wristx, r_wristy, r_wristconf, 
        r_eyex, r_eyey, r_eyeconf,
        r_earx, r_eary, r_earconf,
        l_shoudlerx, l_shoudlery, l_shoudlerconf,
        l_elbowx, l_elbowy, l_elbowconf,
        l_wristx, l_wristy, l_wristconf,
        l_eyex, l_eyey, l_eyeconf,
        l_earx, l_eary, l_earconf])


all_features = ["flow",
        "mic", 
        "delta", "backing_track_position", "chorus_id", 
        "bitalino", 
        "eegT3", "eegT4", "eeg01", "eeg02", 
        "r_shoudlerx", "r_shoudlery", "r_shoudlerconf", 
        "r_elbowx", "r_elbowy", "r_elbowconf", 
        "r_wristx", "r_wristy", "r_wristconf", 
        "r_eyex", "r_eyey", "r_eyeconf",
        "r_earx", "r_eary", "r_earconf",
        "l_shoudlerx", "l_shoudlery", "l_shoudlerconf",
        "l_elbowx", "l_elbowy", "l_elbowconf",
        "l_wristx", "l_wristy", "l_wristconf",
        "l_eyex", "l_eyey", "l_eyeconf",
        "l_earx", "l_eary", "l_earconf"]

df = pd.DataFrame(flat_data, columns = all_features)

fields = ["flow", "eegT3", "eegT4", "eeg01", "eeg02"]

feature_yes = []

for f in all_features:
    if f in fields:
        feature_yes.append(True)
    else:
        feature_yes.append(False)

print(df.shape)

#print(features)

df_small = df.iloc[:,feature_yes]

correlation_mat = df_small.corr()

sns.heatmap(correlation_mat, annot = True)

plt.show()