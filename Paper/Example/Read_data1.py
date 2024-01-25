import pandas as pd
from os import getcwd
import numpy as np
import subprocess
import sys
from matplotlib import pyplot as plt
import matplotlib as mpl


def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])


install("epyt")
from epyt import epanet

d = epanet("Net3.inp")
folder_name1 = "\\Case A"
num_iterations = 50
num_columns = num_iterations
num_rows = d.getNodeCount()
mean_values = np.zeros((num_rows, num_columns))
for i in range(num_iterations):
    folder_name2 = "\\Results_Iteration " + str(i + 1)
    file_name = "\\Time versus node_concentration.xlsx"
    file_path = getcwd() + folder_name1 + folder_name2 + file_name
    excel_data_df = pd.read_excel(file_path, sheet_name="Bulk parameter 1")
    arr = excel_data_df.to_numpy()
    start_row = int(10 * 24 * 3600 / 300) - int(1 * 24 * 3600 / 300)
    start_column = 2
    arr_extracted = arr[start_row:, start_column:]
    arr_extracted[arr_extracted == 0] = np.nan
    mean = np.nanmean(arr_extracted, axis=0)
    mean_values[:, i:] = mean.reshape(len(mean), 1)
    print("Iteration {} completed...".format(i + 1))
print("Analysis completed!")
# Getting X and Y values for the plots
x_data = d.getNodeNameID()
y_data = np.zeros((num_rows, 3))
for i in range(num_rows):
    y_data[i, 0] = np.min(mean_values[i])
    y_data[i, 1] = np.mean(mean_values[i])
    y_data[i, 2] = np.max(mean_values[i])
# Making plots
mpl.rcParams.update({"font.family": "Arial"})
plt.plot(
    x_data,
    y_data[:, 0],
    marker="_",
    markersize=2,
    markerfacecolor="None",
    markeredgecolor="c",
    linestyle="",
)
plt.plot(
    x_data,
    y_data[:, 2],
    marker="_",
    markersize=2,
    markerfacecolor="None",
    markeredgecolor="c",
    linestyle="",
)
plt.vlines(
    x=x_data,
    ymin=y_data[:, 0],
    ymax=y_data[:, 2],
    color="c",
    linestyle="--",
    linewidth=0.2,
)
plt.plot(
    x_data,
    y_data[:, 1],
    marker="o",
    markersize=2,
    markerfacecolor="None",
    markeredgecolor="crimson",
    markeredgewidth=0.5,
    linestyle="",
)
plt.xticks(fontsize=2, rotation=90)
plt.yticks(np.arange(0, 1.4, 0.2), fontsize=6)
plt.ylabel("Chlorine concentration (mg/L)", fontsize=8)
plt.xlabel("Node Name", fontsize=8)
plt.savefig("Case A.png", dpi=600)
