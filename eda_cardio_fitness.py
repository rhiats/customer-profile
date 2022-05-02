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

def violin_plot_gender_fitness(df,output_path):
    v = sns.violinplot(x="Gender", y="Fitness", data=df)
    fig = v.get_figure()
    fig.savefig(output_path+"/gender_fitness_distribution.png")

def stacked_bar_product(df,output_path):
    proddf=df[['Product','Income']]
    proddf['Income_Round']=df.Income.round(decimals=-4)

    product_income=proddf.groupby(['Product','Income_Round'])['Income'].count().reset_index()
    #Relative frequency as the Column - drop Frequency
    product_income.rename({'Income':'Freq'},axis=1,inplace=True)
    product_income.to_csv(output_path+"/prod_inc.csv")

    #Create pivot table with relative frequency
    table = pd.pivot_table(product_income, values=['Freq'], columns=['Product'], index=['Income_Round'],aggfunc='sum',fill_value=0)
    table.reset_index(inplace=True)
    table.to_csv(output_path+"/prod_inc_pivot.csv")

    sns.set()
    bars=table.set_index('Income_Round').T.plot(kind='bar', stacked=True)
    plt.xticks((0, 1, 2), ('TM195', 'TM498', 'TM798'))
    plt.xticks(rotation = 0)
    fig = bars.get_figure()

    #Remove x axis title
    #Format Legend

    fig.savefig(output_path+"/stack_product_income.png")

#Pearson-correlation (look at the math)
#K-means clustering

def main(filename,delivery_folder):
    df=prelim_data(filename)
    #violin_plot_gender_fitness(df,delivery_folder)
    stacked_bar_product(df,delivery_folder)


if __name__ == "__main__":
    main("CardioGoodFitness.csv","output")
