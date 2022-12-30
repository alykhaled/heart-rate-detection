import numpy as np


def print_summary(hr_ecg,hr_bcg,patient_id):

    #convert prints to string
    summary = '----------------------\n'
    summary += 'patient id : ' + str(patient_id) + '\n'
    summary += 'Heart Rate Information\n'
    summary += '----------------------\n'
    summary += 'ECG Method\n'
    summary += 'Minimum pulse : ' + str(np.around(np.min(hr_ecg))) + '\n'
    summary += 'Maximum pulse : ' + str(np.around(np.max(hr_ecg))) + '\n'
    summary += 'Average pulse : ' + str(np.around(np.mean(hr_ecg))) + '\n'
    summary += '----------------------\n'
    summary += 'BCG Method\n'
    summary += 'Minimum pulse : ' + str(np.around(np.min(hr_bcg))) + '\n'
    summary += 'Maximum pulse : ' + str(np.around(np.max(hr_bcg))) + '\n'
    summary += 'Average pulse : ' + str(np.around(np.mean(hr_bcg))) + '\n'
    summary += '----------------------\n'

    # #save summary to file
    # with open('results/summary.txt', 'a') as f:
    #     f.write(summary)

    print(summary)

    return summary

def print_full_summary(hr_ecg,hr_bcg,stats, patient_id):

    filename = 'results/summary.txt'

    #convert prints to string
    summary = '------------------------------------------------------------------\n'
    summary += 'Patient ID : ' + str(patient_id) + '\n'
    summary += '----------------------\n'
    summary += 'ECG \n'
    summary += 'HR Array : ' + str(hr_ecg) + '\n'
    summary += 'Minimum pulse : ' + str(np.around(np.min(hr_ecg))) + '\n'
    summary += 'Maximum pulse : ' + str(np.around(np.max(hr_ecg))) + '\n'
    summary += 'Average pulse : ' + str(np.around(np.mean(hr_ecg))) + '\n'
    summary += '----------------------\n'
    summary += 'BCG \n'
    summary += 'HR Array : ' + str(hr_bcg) + '\n'
    summary += 'Minimum pulse : ' + str(np.around(np.min(hr_bcg))) + '\n'
    summary += 'Maximum pulse : ' + str(np.around(np.max(hr_bcg))) + '\n'
    summary += 'Average pulse : ' + str(np.around(np.mean(hr_bcg))) + '\n'
    summary += '----------------------\n'
    summary += 'Statistics \n'
    summary += 'Mean Absolute Error : ' + str(stats['MAE']) + '\n'
    summary += 'Root Mean Square Error : ' + str(stats['RMSE']) + '\n'
    summary += 'Mean Absolute Percentage Error : ' + str(stats['MAPE']) + '\n'
    summary += '------------------------------------------------------------------\n'

    #append summary to file
    with open(filename, 'a') as f:
        f.write(summary)

    print(summary)

    return summary
