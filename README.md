# Sleep Apnea Heart Rate Detection

## Introduction

This program makes use of ECG and BCG signals to detect heart rate and generates comparative plots to show the difference between the two signals, and the accuracy of the heart rate detection using ballistocardiography (BCG) signal used in sleep apnea detection.

## How to run

1. Clone the repository

2. Install the dependencies

    ```bash
    pip install -r requirements.txt
    ```

3. Download the dataset from [here](https://ieee-dataport.org/open-access/bed-based-ballistocardiography-dataset) and extract it.

4. Convert the dataset to .csv files using matlab script **"dataset_parser.m"** and place the .csv files in the "data" directory of the project.

5. Run the program

    ```bash
    python main.py
    ```

## Documentation

### Program Flow Diagram

![Program Flow Diagram](/docs/block_diagram.png)

### Explanation Report Link

[Report link](/docs/Report.pdf)

## Outputs

### Statistical summary text file

[Results file](results/summary.txt)

### Plots

| Bland Altman | Boxplots |
| --- | --- | 
| ![Bland-Altman](/results/bland_altman_plot.png) | ![Boxplots](/results/boxplot.png) |

| Pearson Correlation | Pearson Corr. Heatmap |
| --- | --- |
| ![Pearson](/results/pearson_correlation.png) | ![Pearson Heatmap](/results/pearson_correlation_heatmap.png) |


## Team Members

| Name | Github |
| --- | --- |
|Aly Khaled|[@alykhaled](https://www.github.com/alykhaled)|
|Mariam Aly|[@MariaamAly](https://www.github.com/MariaamAly)|
|Maryam Moataz|[@MaryamMoataz](https://www.github.com/MaryamMoataz)|
|Mohamed Nasser|[@mo-gaafar](https://www.github.com/mo-gaafar)|

## References

> Sadek, Ibrahim, and Bessam Abdulrazak. “A comparison of three heart rate
detection algorithms over ballistocardiogram signals.” Biomedical Signal
Processing and Control (2021).

> Sadek, Ibrahim, et al. “A new approach for detecting sleep apnea using a
contactless bed sensor: Comparison study.” Journal of medical Internet research
(2020).
