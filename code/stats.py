import scipy.io
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from read_data import read_data, downsample
from ecgdetectors import Detectors
from beat_to_beat import compute_rate,heart_rate
import os



def calculate_stats(ecg,bcg, patient_id):
    mean_absolute_error=0
    root_mean_square_error=0
    mean_absolute_percentage_error=0

    for i in range (0,len(ecg)):
        mean_absolute_error += np.abs(ecg[i] - bcg[i])

        root_mean_square_error += (ecg[i] - bcg[i]) ** 2
        
        mean_absolute_percentage_error += np.abs((ecg[i] - bcg[i]) / ecg[i])

    mean_absolute_error = mean_absolute_error / len(ecg)
    mean_absolute_error = np.abs(mean_absolute_error)

    root_mean_square_error = root_mean_square_error / len(ecg)
    root_mean_square_error = np.sqrt(root_mean_square_error)

    mean_absolute_percentage_error = mean_absolute_percentage_error / len(ecg)
    mean_absolute_percentage_error = mean_absolute_percentage_error * 100


    print("-----------ERROR CALCULATIONS FOR PATIENT WITH ID : "+ str(patient_id)+"-----------")
    print("Mean Absolute Error = " + str(mean_absolute_error))
    print("Root Mean Square Error = " + str(root_mean_square_error))
    print("Mean Absolute Percentage Error = " + str(mean_absolute_percentage_error)+ "%")

    #return dictionary of stats
    return {"MAE":mean_absolute_error,"RMSE":root_mean_square_error,"MAPE":mean_absolute_percentage_error}
