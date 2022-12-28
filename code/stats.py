import scipy.io
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from read_data import read_data, downsample
from ecgdetectors import Detectors
from beat_to_beat import compute_rate,heart_rate
import os



def calculate_stats(ecg,bcg):

    #mean abs error

    root_mean_square_error=0
    mean_absolute_percentage_error=0

    for i in range (0,len(ecg)):

        #mean abs error
        
        
        root_mean_square_error += (ecg[i] - bcg[i]) ** 2
        
        mean_absolute_percentage_error += np.abs((ecg[i] - bcg[i]) / bcg[i])


    root_mean_square_error = root_mean_square_error / len(ecg)
    root_mean_square_error = np.sqrt(root_mean_square_error)

    mean_absolute_percentage_error = mean_absolute_percentage_error / len(ecg)
    mean_absolute_percentage_error = mean_absolute_percentage_error * 100


    print("-----------ERROR CALCULATIONS-----------")
    #mean abs error
    print("Root Mean Square Error = " + str(root_mean_square_error))
    print("Mean Absolute Percentage Error = " + str(mean_absolute_percentage_error)+ "%")

