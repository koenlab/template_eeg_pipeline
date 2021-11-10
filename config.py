"""
Script: config.py
Creator: Joshua D. Koen
Description: This is the main variables and parameters to define
for preprocessing EEG data. 
"""

# Import libraries
from pathlib import Path
import platform
from mne.channels import read_custom_montage

import os
os.chdir(os.path.split(__file__)[0])
my_os = platform.system()

# STEP 1: TASK AND SUBJECT SPECIFIC VARIABLES
# Project ID and Experiment number
project_id = 'nd012'
experiment_id = 'exp1'

# Define task name
task = '1back'

# Bad Subjects not included in group analysis
bad_subs = []

# List of Known Bad Channels
# This is a dictionary of dictionaries. The top dictionary has keys
# for the subject ID, and the value is another dictionary. This other
# dictionary should have two fields: channels and reason. Both should be
# a list with the channel name that is bad, and the reson why.
bad_chans = {
    '999': {
        'channels': ['Cz'],
        'reason': ['a test for bad channels']
        }
}

# List of data columns to drop from behavioral data file(s)
cols_to_keep = ['id', 'stim_set', 'frameRate', 'psychopyVersion',
                'TrialNumber', 'image', 'category', 'subcategory', 'repeat',
                'jitter', 'resp', 'rt', 'correct']

# Rename mapper for behavioral data file
cols_to_rename = {
    'frameRate': 'frame_rate',
    'psychopyVersion': 'psychopy_version',
    'TrialNumber': 'trial_number'
}

# List of columns to add to *events.tsv from behavioral data
cols_to_add = ['trial_number', 'category', 'subcategory', 'repeat', 'resp',
               'rt', 'correct']

# STEP 2: Define Preprocessing Options
# Dictionary of preprocessing options
preprocess_opts = {
    'reference_chan': 'FCz',
    'photosensor_chan': 'Photosensor',
    'resample': 250,
    'l_freq': .1,
    'h_freq': None,
    'tmin': -1.0,
    'tmax': 1.0,
    'baseline': (-.2, 0),
    'bad_chan_thresh': 3,
    'ext_voltage': 150e-6,
    'blink_thresh': 150e-6
}

# BVEF File and Montage
bv_montage = read_custom_montage('old_64ch.bvef', head_size=.08)

# Event ID Marker for BV
bv_event_id = {
    'Marker/M 11': 11,
    'Marker/M 12': 12,
    'Marker/M 21': 21,
    'Marker/M 22': 22,
    'Marker/M 31': 31,
    'Marker/M 32': 32
}

# Rename mapper for BV Stimulus
rename_markers = {
    'Marker/M 11': 'scene/novel',
    'Marker/M 12': 'scene/1back',
    'Marker/M 21': 'object/novel',
    'Marker/M 22': 'object/1back',
    'Marker/M 31': 'face/novel',
    'Marker/M 32': 'face/1back'
}

# Rename mapper for BV Stimulus
event_id = {
    'scene/novel': 11,
    'scene/1back': 12,
    'object/novel': 21,
    'object/1back': 22,
    'face/novel': 31,
    'face/1back': 32
}

# STEP 3: DEFINE THE SERVER AND DATA DIRECTORIES
# This is platform dependent and returns a Path class object
# Get the server directory
# UNCOMMENT THIS FOR A REAL PROJECT
# if my_os == 'Darwin':
#     server_dir = Path('/Volumes/koendata/EXPT')
# elif my_os == 'Linux':
#     server_dir = Path('/koenlab/koendata/EXPT')
# else:
#     server_dir = Path('X:\EXPT')
# data_dir = server_dir / project_id / experiment_id / 'data'

# DELETE THESE TWO LINES FOR A REAL PROJECT
data_dir = Path('data')

# STEP 4: DEFINE PATHS (DO NOT CHANGE AFTER THIS)
# This is the source_data directory
source_dir = data_dir / 'sourcedata'

# This is the bids formatted output directory
bids_dir = data_dir / 'bids'
bids_dir.mkdir(parents=True, exist_ok=True)

# Derivatives directory
deriv_dir = data_dir / 'derivatives' / f'task-{task}'
deriv_dir.mkdir(parents=True, exist_ok=True)

# Report directory
report_dir = deriv_dir / 'reports'
report_dir.mkdir(parents=True, exist_ok=True)

# Analysis Directory
analysis_dir = data_dir / 'analyses' / f'task-{task}'
analysis_dir.mkdir(parents=True, exist_ok=True)
