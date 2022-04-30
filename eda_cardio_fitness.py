import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore') # To supress warnings
sns.set(style="whitegrid") # set the background for the graphs

def prelim_data(data_csv):
    dffitness=pd.read_csv(data_csv)
    print(dffitness.info())

def main(filename):
    prelim_data(filename)


if __name__ == "__main__":
    main("customer-profile/CardioGoodFitness.csv")
