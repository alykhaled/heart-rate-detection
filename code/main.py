from read_data import read_data, downsample
from ecgdetectors import Detectors
from beat_to_beat import heart_rate
import plots
import stats
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
from detect_peaks import detect_peaks
from compute_vitals import vitals
import numpy as np
import math
from modwt_matlab_fft import modwt
from modwt_mra_matlab_fft import modwtmra
import os

T1 = 0
T2 = 100000
F_SAMPLE = 50
WINDOW_TIME_SEC = 10
WINDOW_N = WINDOW_TIME_SEC * F_SAMPLE


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
            hr_ecg = heart_rate(r_peaks, len(ecg), t_window_sec= WINDOW_TIME_SEC, fs= F_SAMPLE) # Calculate heart rate from R peaks
            ecg_hr.append(hr_ecg)

            print("Heart rate (ECG): " + str(hr_ecg))

            # Detect Peaks of BCG by adapting the dr's code
            print("Detecting peaks of BCG...")
            w = modwt(bcg, 'bior3.9', 4)
            dc = modwtmra(w, 'bior3.9')
            wavelet_cycle = dc[4]
            # t1, t2, window_length, window_shift = 0, 500, 500, 500
            limit = int(math.floor(bcg.size / WINDOW_N))
            j_peaks = detect_peaks(bcg, show=False) # Detect J peaks

            # hr_bcg = heart_rate(j_peaks, len(bcg), t_window_sec= WINDOW_TIME_SEC, fs= F_SAMPLE) # Calculate heart rate from J peaks
            
            hr_bcg = vitals(T1, WINDOW_N, WINDOW_N, bcg.size, wavelet_cycle,mpd=1, plot=0)
            # bcg_hr.append(np.around(np.mean(hr_bcg)))
            bcg_hr.append(hr_bcg)
            print("Heart rate (BCG): " + str(hr_bcg))

            print('\nHeart Rate Information')
            print('Minimum pulse : ', np.around(np.min(hr_bcg)))
            print('Maximum pulse : ', np.around(np.max(hr_bcg)))
            print('Average pulse : ', np.around(np.mean(hr_bcg)))

            # Plot the results of the two methods 
            print("Plotting results...")

            # plots.get_bland_altman_plot(ecg_hr,bcg_hr)
            # plots.get_boxplot(ecg_hr,bcg_hr)

            # stats.calculate_stats(ecg_hr,bcg_hr)


        # plt.figure(figsize=(10, 5))
        # plt.plot(ecg_hr, label='ECG')
        # plt.plot(bcg_hr, label='BCG')
        # plt.xlabel('Patient')
        # plt.ylabel('Heart rate (bpm)')
        # plt.legend()
        # plt.show()

if __name__ == '__main__':
    main()
