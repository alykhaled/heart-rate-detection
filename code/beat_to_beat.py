import numpy as np

from detect_peaks import detect_peaks


def compute_rate(beats,mpd, indices= None):
    if indices is None:
        indices = detect_peaks(beats, mpd=mpd)
    else:
        #TODO: this needs review
        # get indecies of peaks in beats array
        indices = np.array([i for i, x in enumerate(beats) if x in indices])

    if len(indices) > 1:
        diff_sample = indices[-1] - indices[0] + 1
        t_N = diff_sample / 50
        heartRate = (len(indices) - 1) / t_N * 60
        return heartRate, indices
    else:
        return 0.0, 0.0

def heart_rate( peaks:np.array, sig_length:int, t_window_sec = 5 , fs = 50):
    """
    Calculate heart rate from peaks given window size.
    
    :param peaks: array of peak indexes
    :param sig_length: length of the signal
    :param t_window_sec: time window in seconds
    :param fs: sampling frequency

    :return: heart rate array
    """
    heartRate = []
    t_window_n = t_window_sec * fs
    # loop over all peaks and count how many peaks are in the window
    for i in range(0, sig_length, round(t_window_n)):
        # calculate the time window in seconds
        t_window_sec  = t_window_n / fs
        # calculate the heart rate from counting peak indexes that fall in the window
        peak_count = 0
        for peak in peaks:
            if peak > i and peak < i + t_window_n:
                peak_count += 1
        # calculate heart rate
        heartRate.append(peak_count / t_window_sec * 60)
    
    return heartRate

