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
fig = plt.figure(figsize=(8, 8))

def get_bland_altman_plot(ecg,bcg):

    ecg_array = np.asarray(ecg)
    bcg_array = np.asarray(bcg)

    plt.title("Bland-Altman Plot")
    # fig.add_subplot(rows, columns, 1)
    calc_bland_altman_plot = bland_altman_plot(ecg_array, bcg_array)
    plt.savefig("results/bland_altman_plot.png")
    plt.show()


def get_boxplot(ecg,bcg):

    ecg = np.asarray(ecg)
    bcg = np.asarray(bcg)

    # make the boxplots in a two figure layout
    fig, axs  = plt.subplots(1, 2, figsize=(8, 8))
    
    axs[0].boxplot(ecg)
    axs[0].set_title("ECG Boxplot")

    axs[1].boxplot(bcg)
    axs[1].set_title("BCG Boxplot")
    plt.savefig("results/boxplot.png")
    # plt.show(plt.boxplot(bcg))


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
    plt.title("Pearson Correlation of " + str(calc_pearson_correlation.flatten()))
    plt.xlabel("ECG")
    plt.ylabel("BCG")
    plt.savefig("results/pearson_correlation.png")
    plt.show()


def get_pearson_heatmap(ecg, bcg):
    ecg_array = np.asarray(ecg)
    bcg_array = np.asarray(bcg)
    calc_pearson_correlation = np.corrcoef(ecg_array, bcg_array)
    heatmap_labels = sns.heatmap(calc_pearson_correlation, annot=True, linewidths=.5)
    heatmap_labels.set_title("Pearson Correlation Heatmap")
    heatmap_labels.set_xlabel("ECG")
    heatmap_labels.set_ylabel("BCG")
    plt.savefig("results/pearson_correlation_heatmap.png")
    plt.show()
    












    
   

