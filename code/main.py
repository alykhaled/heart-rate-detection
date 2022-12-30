from read_data import read_data, downsample
from ecgdetectors import Detectors
from beat_to_beat import compute_rate,heart_rate
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
from detect_peaks import detect_peaks
from compute_vitals import vitals
import numpy as np
import math
from modwt_matlab_fft import modwt
from modwt_mra_matlab_fft import modwtmra
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
            w = modwt(bcg, 'bior3.9', 4)
            dc = modwtmra(w, 'bior3.9')
            wavelet_cycle = dc[4]
            t1, t2, window_length, window_shift = 0, 500, 500, 500
            limit = int(math.floor(bcg.size / window_shift))
            j_peaks = detect_peaks(bcg, mpd=1000, show=False) # Detect J peaks
            beats = vitals(t1, t2, window_shift, limit, wavelet_cycle,mpd=1, plot=0)
            print('\nHeart Rate Information')
            print('Minimum pulse : ', np.around(np.min(beats)))
            print('Maximum pulse : ', np.around(np.max(beats)))
            print('Average pulse : ', np.around(np.mean(beats)))
            bcg_hr.append(np.around(np.mean(beats)))

    # Plot the results of the two methods 
    print("Plotting results...")
    plt.figure(figsize=(10, 5))
    plt.plot(ecg_hr, label='ECG')
    plt.plot(bcg_hr, label='BCG')
    plt.xlabel('Patient')
    plt.ylabel('Heart rate (bpm)')
    plt.legend()
    plt.show()




if __name__ == '__main__':
    main()
