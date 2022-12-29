import scipy.io
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from read_data import read_data, downsample
from ecgdetectors import Detectors
from beat_to_beat import compute_rate,heart_rate
import os
from bland_altman import bland_altman_plot

# rows = 2
# columns = 2
# fig = plt.figure(figsize=(20, 15))

def get_bland_altman_plot(ecg,bcg):

    ecg_array = np.asarray(ecg)
    bcg_array = np.asarray(bcg)
    print("ECG ISSSSSSSSSSSSSS"+ str(ecg))
    print("BCG ISSSSSSSSSSSSSS"+ str(bcg))
    calc_bland_altman_plot = bland_altman_plot(ecg_array, bcg_array)
    plt.savefig("bland_altman_plot.png")

    # fig.add_subplot(rows, columns, 1)

    # plt.imshow(calc_bland_altman_plot)
    # plt.axis('off')
    # plt.title("Bland-Altman Plot")

def get_boxplot(ecg,bcg):

    plt.boxplot(ecg)
    plt.savefig("ecg_boxplot.png")

    # fig.add_subplot(rows, columns, 3)
    # plt.imshow(plt.boxplot(ecg))
    # plt.axis('off')
    # plt.title("ECG Boxplot")

    plt.boxplot(bcg)
    plt.savefig("bcg_boxplot.png")

    # fig.add_subplot(rows, columns, 4)
  
   
    # plt.imshow(plt.boxplot(bcg))
    # plt.axis('off')
    # plt.title("BCG Boxplot")

# def get_pearson_correlation(ecg,bcg):
#     ecg_array = np.asarray(ecg)
#     bcg_array = np.asarray(bcg)
#     print("ECG ISSSSSSSSSSSSSS"+ str(ecg))
#     print("BCG ISSSSSSSSSSSSSS"+ str(bcg))
#     calc_pearson_correlation = np.corrcoef(ecg_array, bcg_array)
#     plt.savefig("pearson_correlation.png")
    
#     fig.add_subplot(rows, columns, 2)
#     plt.imshow(calc_pearson_correlation)
#     plt.axis('off')
#     plt.title("Pearson Correlation")    



