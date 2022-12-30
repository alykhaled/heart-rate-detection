from read_data import read_data, downsample
from ecgdetectors import Detectors
import heartpy as hp
from beat_to_beat import heart_rate
import plots
import stats
import prints
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
T2 = 500
F_SAMPLE = 50
WINDOW_TIME_SEC = 10
WINDOW_N = WINDOW_TIME_SEC * F_SAMPLE

detectors = Detectors(F_SAMPLE)

def main():
    # Read dataset from file
    print("Reading data...")
    data_folder = './data/'

    ecg_hr = []
    bcg_hr = []
    # Loop over all files in the folder
    for file in os.listdir(data_folder)[:10]:
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

            # ECG -----------------------------------------------------------------------
            w = modwt(ecg, 'bior3.9', 4)
            dc = modwtmra(w, 'bior3.9')
            wavelet_cycle_ecg = dc[4]
            t1, t2, window_length, window_shift = T1, T2, WINDOW_N, WINDOW_N
            limit = int(math.floor(bcg.size / window_shift))
            hr_ecg = []
            wd, m = hp.process_segmentwise(wavelet_cycle_ecg,F_SAMPLE, WINDOW_TIME_SEC)
            hr_ecg = m["bpm"]

            print("Heart rate (ECG): " + str(hr_ecg))


            ## BCG -----------------------------------------------------------------------
            # Detect Peaks of BCG by adapting the dr's code
            print("Detecting peaks of BCG...")
            w = modwt(bcg, 'bior3.9', 4)
            dc = modwtmra(w, 'bior3.9')
            wavelet_cycle = dc[4]
            limit = int(math.floor(bcg.size / WINDOW_N))
            hr_bcg = vitals(T1, T2, WINDOW_N, limit, wavelet_cycle, F_SAMPLE, mpd=1, plot=0)
            print("Heart rate (BCG): " + str(hr_bcg))


            # OUTPUTS --------------------------------------------------------------------
            
            
            # if nan in hr_ecg or nan in hr_bcg remove it
            if np.isnan(hr_ecg).any():
                hr_ecg = np.nan_to_num(hr_ecg)
            if np.isnan(hr_bcg).any():
                hr_bcg = np.nan_to_num(hr_bcg)

            # if one is larger than the other, remove the last element
            if len(hr_ecg) > len(hr_bcg):
                ecg_hr = hr_ecg[:-1]
            elif len(hr_ecg) < len(hr_bcg):
                hr_bcg = hr_bcg[:-1]
            
            # append to the big list (all patients)
            ecg_hr.append(hr_ecg)
            bcg_hr.append(hr_bcg)
            
            # Print the results of the two methods
            print("Printing results...\n")

            stat_dict = stats.calculate_stats(hr_ecg,hr_bcg, file[1:5])
            prints.print_summary(hr_ecg,hr_bcg, file[1:5])
            prints.print_full_summary(hr_ecg,hr_bcg, stat_dict, file[1:5])
            
    # Plot the results of the two methods 
    print("Plotting results...")

    # flatten ecg_hr and bcg_hr
    ecg_hr = [item for sublist in ecg_hr for item in sublist]
    bcg_hr = [item for sublist in bcg_hr for item in sublist]
    
    plots.get_bland_altman_plot(ecg_hr,bcg_hr)
    plots.get_boxplot(ecg_hr,bcg_hr)
    plots.get_pearson_correlation(ecg_hr,bcg_hr)
    plots.get_pearson_heatmap(ecg_hr,bcg_hr)

    # hold program
    input("Press Enter to continue...")

if __name__ == '__main__':
    main()
