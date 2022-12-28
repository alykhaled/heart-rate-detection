import scipy.io
import numpy as np
import pandas as pd

def read_data(path):
    data = pd.read_csv(path)
    return data
    

def downsample(data, initial_hz, target_hz):
    """Downsample data from initial_hz to target_hz.
    Args:
        data: 1D numpy array of data to downsample.
        initial_hz: Initial sampling rate of data.
        target_hz: Target sampling rate of data.
    Returns:
        downsampled_data: 1D numpy array of downsampled data.
    """

    # Calculate the number of samples to skip
    skip = int(initial_hz / target_hz)

    # Downsample the data
    downsampled_data = data[::skip]

    return np.array(downsampled_data)
