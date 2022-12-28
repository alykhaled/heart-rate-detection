from read_data import read_data, downsample
from ecgdetectors import Detectors
from beat_to_beat import compute_rate,heart_rate
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import os
F_SAMPLE = 50

def main():
    # Read dataset from file
    print("Reading data...")
    data_folder = '../data/'

    ecg_hr = []
    bcg_hr = []
    # Loop over all files in the folder
    for file in os.listdir(data_folder):
        if file.endswith(".csv") and file.startswith("X"):
            print(os.path.join(data_folder, file))
            path = os.path.join(data_folder, file)
            data = read_data(path)    
            # Preprocess data
            print("Preprocessing data...")
            ecg = data['ECG']
            bcg = data['LC_BCG2']

            ecg = downsample(ecg,1000, 50)
            bcg = downsample(bcg,1000, 50)

            # Detect peaks of ECG using pan tompkins library
            print("Detecting peaks of ECG...")
            detectors = Detectors(F_SAMPLE) # Initialize detectors object
            r_peaks = detectors.pan_tompkins_detector(ecg) # Detect R peaks
            hr_ecg = heart_rate(r_peaks) # Calculate heart rate from R peaks
            ecg_hr.append(hr_ecg)

            print("Heart rate: " + str(hr_ecg))

            # Detect Peaks of BCG by adapting the dr's code
            print("Detecting peaks of BCG...")
            j_peaks = detectors.pan_tompkins_detector(bcg) # Detect J peaks
            hr_bcg = heart_rate(j_peaks) # Calculate heart rate from J peaks
            bcg_hr.append(hr_bcg)
            print("Heart rate: " + str(hr_bcg))

    # Plot the results of the two methods 
    print("Plotting results...")
    # plt.plot(ecg_hr, label='ECG')
    # plt.plot(bcg_hr, label='BCG')
    # plt.legend()
    # plt.show()
    


if __name__ == '__main__':
    main()
