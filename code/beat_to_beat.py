import numpy as np

from detect_peaks import detect_peaks


def compute_rate(beats, time, mpd, indices= None):
    if indices is None:
        indices = detect_peaks(beats, mpd=mpd)
    else:
        #TODO: this needs review
        # get indecies of peaks in beats array
        indices = np.array([i for i, x in enumerate(beats) if x in indices])

    if len(indices) > 1:
        peak_to_peak = []
        for i in range(0, indices.size - 1):
            peak_to_peak = np.append(peak_to_peak, time[indices[i + 1]] - time[indices[i]])
        mean_heart_rate = np.average(peak_to_peak, axis=0)
        bpm_avg = 1000 * (60 / mean_heart_rate)
        return np.round(bpm_avg, decimals=2), indices
    else:
        return 0.0, 0.0

def heart_rate(peaks):
    diff_sample = peaks[-1] - peaks[0] + 1
    t_N = diff_sample / 50
    heartRate = (len(peaks) - 1) / t_N * 60
    return heartRate
