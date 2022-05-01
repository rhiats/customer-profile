import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore') # To supress warnings
sns.set(style="ticks",palette="Paired") # set the background for the graphs

def prelim_data(data_csv):
    dffitness=pd.read_csv(data_csv)
    print(dffitness.info())
    return dffitness

def violin_plot(df,output_path):
    v = sns.violinplot(x="Gender", y="Fitness", data=df)
    fig = v.get_figure()
    fig.savefig(output_path+"/gender_fitness_distribution.png")


def main(filename,delivery_folder):
    df=prelim_data(filename)
    violin_plot(df,delivery_folder)


if __name__ == "__main__":
    main("CardioGoodFitness.csv","output")
