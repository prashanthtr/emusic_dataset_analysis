
# Analysing the emusic dataset

Here's a snippet to produce correation values between features in the Emboided musicking dataset 
https://github.com/Creative-AI-Research-Group/embodiedMusickingDataset

# All Features 

The main features included in this analysis are: flow, backing track data, and hardware information. The features are run through a correaltion function to derive insights about feature relations.

## Flow

	Flow

### Track

	mic,  delta, backing_track_position, chorus_id, 

## Hardware

	bitalino 

### EEG: 

	eegT3, eegT4, eeg01, eeg02, 

### Body

        r_shoudlerx, r_shoudlery, r_shoudlerconf, 
        r_elbowx, r_elbowy, r_elbowconf, 
        r_wristx, r_wristy, r_wristconf, 
        r_eyex, r_eyey, r_eyeconf,
        r_earx, r_eary, r_earconf,
        l_shoudlerx, l_shoudlery, l_shoudlerconf,
        l_elbowx, l_elbowy, l_elbowconf,
        l_wristx, l_wristy, l_wristconf,
        l_eyex, l_eyey, l_eyeconf,
        l_earx, l_eary, l_earconf

## Visualization

Customize the "fields" variable in Line 119 to produce different visualizations of features in the dataset.

	fields = ["flow", "eegT3", "eegT4", "eeg01", "eeg02"]
