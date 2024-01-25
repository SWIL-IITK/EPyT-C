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
name_table = ["Case A", "Case B", "Case C", "Case D"]
y_data = np.zeros((d.getNodeCount(), len(name_table)))
for n in range(len(name_table)):
    folder_name1 = "\\" + name_table[n]
    num_iterations = 50
    num_columns = num_iterations
    num_rows = d.getNodeCount()
    mean_values = np.zeros((num_rows, num_columns))
    for i in range(num_iterations):
        folder_name2 = "\\Results_Iteration " + str(i + 1)
        file_name = "\\Time versus node_concentration.xlsx"
        file_path = getcwd() + folder_name1 + folder_name2 + file_name
        excel_data_df = pd.read_excel(file_path, sheet_name="Bulk parameter 1")
        # excel_data_df = pd.read_excel(file_path, sheet_name='Bulk parameter 3')
        arr = excel_data_df.to_numpy()
        start_row = int(10 * 24 * 3600 / 300) - int(1 * 24 * 3600 / 300)
        start_column = 2
        arr_extracted = arr[start_row:, start_column:]
        arr_extracted[arr_extracted == 0] = np.nan
        mean = np.nanmean(arr_extracted, axis=0)
        mean_values[:, i:] = mean.reshape(len(mean), 1)
        print("Iteration {} completed...".format(i + 1))
    for i in range(num_rows):
        y_data[i, n] = np.mean(mean_values[i])
    print("Analysis completed for {} case!\n".format(n + 1))
# Getting X and Y values for the plots
x = np.sort(y_data, axis=0)
c_range = np.arange(0.1, 1.1, 0.1)
# c_range = np.arange(10, 90, 10)
percentage = np.zeros((len(c_range), len(name_table)))
for n in range(len(name_table)):
    k = 0
    while k < len(c_range):
        base = c_range[k]
        percentage[k][n] = (
            len([a for a in x[:, n] if a >= base]) / (len(x[:, 0]))
        ) * 100
        # percentage[k][n] = (len([a for a in x[:, n] if a <= base])/(len(x[:,0])))*100
        k += 1
# Making plots
mpl.rcParams.update({"font.family": "Arial"})
plt.plot(
    c_range,
    percentage[:, 0],
    marker="o",
    markersize=5,
    markerfacecolor="None",
    markeredgecolor="c",
    linestyle="--",
    linewidth=0.5,
    color="c",
)
plt.plot(
    c_range,
    percentage[:, 1],
    marker="^",
    markersize=5,
    markerfacecolor="None",
    markeredgecolor="r",
    linestyle="--",
    linewidth=0.5,
    color="r",
)
plt.plot(
    c_range,
    percentage[:, 2],
    marker="v",
    markersize=5,
    markerfacecolor="None",
    markeredgecolor="g",
    linestyle="--",
    linewidth=0.5,
    color="g",
)
plt.plot(
    c_range,
    percentage[:, 3],
    marker="s",
    markersize=5,
    markerfacecolor="None",
    markeredgecolor="b",
    linestyle="--",
    linewidth=0.5,
    color="b",
)
plt.xticks(np.arange(0.1, 1.1, 0.1), fontsize=6)
# plt.xticks(np.arange(10, 90, 10), fontsize = 6)
plt.yticks(np.arange(0, 120, 20), fontsize=6)
plt.ylabel("Percentage of nodes", fontsize=8)
plt.xlabel("Mean chlorine concentration (mg/L)", fontsize=8)
# plt.xlabel('Mean THMs concentration (\u03bcg/L)', fontsize = 8)
plt.legend(["Case A", "Case B", "Case C", "Case D"], loc="best", fontsize=6)
plt.savefig("PDF.png", dpi=600)
# plt.savefig('PDF_H.png', dpi = 600)
