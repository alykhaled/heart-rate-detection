import scipy.io
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from read_data import read_data, downsample
from ecgdetectors import Detectors
from beat_to_beat import compute_rate,heart_rate
import os
from bland_altman import bland_altman_plot
import seaborn as sns
from scipy import stats
 
rows = 2
columns = 2
fig = plt.figure(figsize=(20, 15))

def get_bland_altman_plot(ecg,bcg):

    ecg_array = np.asarray(ecg)
    bcg_array = np.asarray(bcg)
    # print("ECG ISSSSSSSSSSSSSS"+ str(ecg))
    # print("BCG ISSSSSSSSSSSSSS"+ str(bcg)) # use debugger to see the values
    calc_bland_altman_plot = bland_altman_plot(ecg_array, bcg_array)
    # plt.savefig("bland_altman_plot.png")

    # fig.add_subplot(rows, columns, 1)

    # plt.imshow(calc_bland_altman_plot)
    # plt.axis('off')
    # plt.title("Bland-Altman Plot")

def get_boxplot(ecg,bcg):

    ecg = np.asarray(ecg)
    bcg = np.asarray(bcg)
    plt.boxplot(ecg)
    # plt.savefig("ecg_boxplot.png")

    # fig.add_subplot(rows, columns, 3)
    # plt.imshow(plt.boxplot(ecg))
    # plt.axis('off')
    # plt.title("ECG Boxplot")

    plt.boxplot(bcg)
    # plt.savefig("bcg_boxplot.png")

    # fig.add_subplot(rows, columns, 4)
  
   
    # plt.imshow(plt.boxplot(bcg))
    # plt.axis('off')
    # plt.title("BCG Boxplot")


def get_pearson_correlation(ecg, bcg):
    ecg_array = np.asarray(ecg)
    bcg_array = np.asarray(bcg)
    calc_pearson_correlation = np.corrcoef(ecg_array, bcg_array)


    #convert to pandas dataframe with two columns
    dataframe = pd.DataFrame(columns=["ECG", "BCG"])
    # instert ecg and bcg values into dataframe
    dataframe["ECG"] = ecg_array
    dataframe["BCG"] = bcg_array
    

    # Line of best fit
    sns.lmplot(x="ECG", y="BCG", data=dataframe)

    plt.scatter(ecg_array, bcg_array)
    plt.title("Pearson Correlation of " + str(calc_pearson_correlation))
    plt.xlabel("ECG")
    plt.ylabel("BCG")
    plt.savefig("results/pearson_correlation.png")
    # plt.imshow()


def get_pearson_HeatMap(ecg, bcg):
    ecg_array = np.asarray(ecg)
    bcg_array = np.asarray(bcg)
    calc_pearson_correlation = np.corrcoef(ecg_array, bcg_array)
    heatmap_labels = sns.heatmap(calc_pearson_correlation, annot=True, linewidths=.5)
    heatmap_labels.set_title("Pearson Correlation Heatmap")
    heatmap_labels.set_xlabel("ECG")
    heatmap_labels.set_ylabel("BCG")
    # plt.savefig("results/pearson_correlation_heatmap.png")
    












    
   

