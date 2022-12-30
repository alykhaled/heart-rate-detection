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
    plt.savefig("bland_altman_plot.png")

    # fig.add_subplot(rows, columns, 1)

    # plt.imshow(calc_bland_altman_plot)
    # plt.axis('off')
    # plt.title("Bland-Altman Plot")

def get_boxplot(ecg,bcg):

    ecg = np.asarray(ecg)
    bcg = np.asarray(bcg)
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


def get_pearson_correlation(ecg,bcg):
    ecg_array = np.asarray(ecg)
    bcg_array = np.asarray(bcg)

    #CALCULATING PEARSON CORRELATION returns 2d matrix
    calc_pearson_correlation = np.corrcoef(ecg_array, bcg_array)
    print("Pearson Correlation Matrix is " + str(calc_pearson_correlation))
    
    #Returns Correlation Coefficient and P-value
    #stats.pearsonr(con['ecg_array'], con['bcg_array'])

    
    #Plotting Data
    plt.savefig("pearson_correlation.png")
    fig.add_subplot(rows, columns, 2)
    sns.scatterplot(x=ecg_array, y=bcg_array,data=calc_pearson_correlation)

    #Plotting Labels and Title
    add_labels = sns.scatterplot(x=ecg_array, y=bcg_array, data=calc_pearson_correlation)
    add_labels.set_title("Pearson Correlation")
    add_labels.set_xlabel("ECG")
    add_labels.set_ylabel("BCG")

    #Line of best fit
    sns.lmplot(x="ECG", y="BCG", data=calc_pearson_correlation)
    

    #Heatmap:annot to represent cell values
    heatmap_labels=sns.heatmap(calc_pearson_correlation, annot=True, linewidth=.5, cmap="YlGnBu")
    heatmap_labels.set_title("Pearson Correlation Heatmap")
    heatmap_labels.set_xlabel("ECG")
    heatmap_labels.set_ylabel("BCG")
    plt.savefig("pearson_correlation_heatmap.png")

    
   

