# import pandas and matplotlib 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from connection import setConnection

def liabilityasset():
    dataT=setConnection(["profitloss"])
    labels=[]
    Income_of_all_trips=[]
    Expenditure_of_the_year=[]
    data=[]
    for x in dataT:
            data.append(list(x))    
    for x in data:
        for n,i in enumerate(x):
            if i==None:
               x[n]=0
        print("##########",x)
        labels.append(x[0])
        Income_of_all_trips.append(int(x[1]))
        Expenditure_of_the_year.append(int(x[2]))
    
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, Income_of_all_trips, width, label='Yearly Income')
    rects2 = ax.bar(x + width/2, Expenditure_of_the_year, width, label='Yearly Expenditure')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Amount in Rs')
    ax.set_title('LIABILITY OR ASSET', bbox={'facecolor':'0.8', 'pad':5})
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()


    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.show()
def Maintenance():
    data=setConnection(["maintenanceCategory"])
    Maintenance=[]
    amount=[]
    for x in data:
        Maintenance.append(x[0])
        amount.append(x[1])
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
    plt.pie(amount, labels=Maintenance, colors=colors,autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title("MAINTENANCE", bbox={'facecolor':'0.8', 'pad':5})
    plt.show()


def Expenditure():
       
        data=setConnection(["expenseView"])
        dataList=[]
        index=[]
        for x in data:
            index.append(x[0])
            dataList.append(list(x))
        for x in dataList:
            x.remove(x[0])
        dataListNum=[]
        for x in dataList:
            col=[]
            for y in x:
                col.append(int(y))
            dataListNum.append(col)    

        # dataframe created with 
        # the above data array 
        df = pd.DataFrame(dataListNum, columns = ['Insurance_Amt','Tax_Amt','Permit_Amt','Maintenance_Amt'],index=index ) 

        df.plot.bar() 
        plt.show() 