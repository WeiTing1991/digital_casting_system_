
## install panda, matplotlib, scipy

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import os


from sklearn.preprocessing import MinMaxScaler
from scipy.optimize import curve_fit

class CSVToDataFrame():

    """ CSV data to panda dataframe
    """
    def __init__(self, filename:str, data_folder_path:str):
        """
        """
        self.CSV_DIR = os.path.abspath(os.path.join(data_folder_path, filename))

    def set_data_frame(self):
        """
        """
        self.df = pd.read_csv(self.CSV_DIR)

    def get_data_frame(self):
        """
        """
        return self.df

    def print_head(self):
        """
        """
        print(self.df.head())

    def print_columns(self):
        """
        """
        print(self.df.columns)


    def clean_noise_data(self, colume_name: str, replace_num:int, tolerance:int):
        """
        """
        min_num = replace_num - tolerance
        max_num = replace_num + tolerance

        self.df[colume_name] = np.where(self.df[colume_name].between(min_num, max_num), replace_num, self.df[colume_name])

    def average_tow_column_data(self, col_1, col_2, new_col):
        """
        average adata from the two column to new column
        """
        self.df[new_col] = (self.df[col_1] + self.df[col_2])/2

    def remap_data(self, col, remap_Max):
        """
        remap the data
        """
        scale_data = (self.df[col] - self.df[col].min()) / (self.df[col].max() - self.df[col].min())
        self.df[col] = (scale_data*remap_Max).round(2)

    def smooth_data(self, col, factor):
        """
        smooth the data with average
        """
        self.df[col] = (self.df[col]*(1-factor) + self.df[col].mean()*factor).round(2)

    def two_cols_to_arr(self):
        """
        """
        #print(f"speed:{data_1.col_1_list}")
        # col_1_list : Speed [rpm]
        # col_2_list : Torque [Nm]

        self.col_1_list = (self.col_1_list).round(2) # rpm
        self.col_2_list = (self.col_2_list).round(2) # Nm

        speed_list = self.col_1_list
        torque_list = self.col_2_list
        power_list = ((2*math.pi*(self.col_2_list/1000)*self.col_1_list)/60).round(4) # kw = (2pi* rpm* kNm)/60

        data_arr_speed_torque = np.array([self.col_1_list, self.col_2_list], dtype=np.ufunc)
        data_arr_power_speedspaue = np.array([list(map(lambda x: x ** 2, self.col_1_list)), power_list*1000], dtype=np.ufunc) # kw to w

        print(f"speed_vs_torque:{data_arr_speed_torque}\n")
        print(f"power_vs_speed^2:{data_arr_power_speedspaue}\n")

        return data_arr_speed_torque, data_arr_power_speedspaue



class PlotFromData():
    """
    plot data
    """
    def __init__(self) -> None:
        pass
    def linarfunc(self):
        pass
    def expfunc(self):
        pass
    def show_plot(self):
        pass


def linar_func(x, a, c):
    return a*x + c

def exponential_func(x, a, b, c):
    return a*np.exp(x*b) + c

def dataframe_to_dict(data_list, label_list, make_type_list, color_list):
    # create dictionary for plot
    data_plot_info_dicts = {}
    for i, d in enumerate(data_list):
        if data_plot_info_dicts != None:
            data_plot_info_dicts[i] = {}
        data_plot_info_dicts[i]['data'] = data_list[i]
        data_plot_info_dicts[i]['label'] = label_list[i]
        data_plot_info_dicts[i]['make_type'] = make_type_list[i]
        data_plot_info_dicts[i]['markersize'] = 10
        data_plot_info_dicts[i]['color'] = color_list[i]
        data_plot_info_dicts[i]['linewidth'] = 1
        data_plot_info_dicts[i]['linestyle'] = 'solid'
    return data_plot_info_dicts

def draw(*data_dict, xlabel, ylabel, ylimit):
    """
    TODO:
    data_arr : numpay array

    """
    ax = plt.axes()
    ax.set_xlabel(xlabel, fontsize=24)
    ax.set_ylabel(ylabel, fontsize=24)

    ax.axes.set_ylim(0.00, ylimit)

    for i, data in enumerate(data_dict):
        # linear curves fit
        # gradient, intercept, r_value, p_value, slop_std_error = stats.linregress(data['data'][0], data['data'][1])
        # predict_y = gradient * data['data'][0] + intercept

        # non-linear curve fit
        params, params_covariance = curve_fit(linar_func, data['data'][0], data['data'][1]) # popt, pcov
        # a*x + c
        a = params[0]
        c = params[1]
        #print(data['data'][1], data['data'][0])
        print(params)
        # R squred
        residuals = data['data'][1]- linar_func(data['data'][0], *params)
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((data['data'][1]-np.mean(data['data'][1]))**2)
        r_squared = round(1 - (ss_res / ss_tot), 3)
        print(f"R^2:{r_squared}")

        label_line = f"{params[0].round(5)}*x + {params[1].round(4)}, $R^2$:{r_squared}"
        print(label_line)

        # fitting curve plot
        plt.grid(b=None)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.plot(data['data'][0], linar_func(data['data'][0], a, c), linestyle = data['linestyle'], color = data['color'], linewidth = 1,)
        ax.annotate(xy=(data['data'][0][-1], data['data'][1][-1]), xytext=(5,i*5), textcoords='offset points', text= label_line, va='center', fontsize = '10')
        plt.plot(data['data'][0], data['data'][1], data['make_type'],color = data['color'], markersize = data['markersize'], label = data['label'])


    plt.grid()
    plt.legend(loc="upper left", fontsize = 20)
    plt.show()


if __name__ == "__main__":

    HERE = os.path.dirname(__file__)
    HOME = os.path.abspath(os.path.join(HERE, "../../../"))
    DATA = os.path.abspath(os.path.join(HOME, "data/csv"))

    FILFE_NAME_LIST = ["20230706_54_agg_72S_1.5FW_ETH_temperature_120.csv",
                       "20230713_54agg_70S_1.5FW_Temperature_withCAC.csv"
                       ]


    DATA_LIST = FILFE_NAME_LIST


    data_frame_list = []
    for file_name in DATA_LIST:
        CsvToDf = CSVToDataFrame(file_name, DATA)
        CsvToDf.set_data_frame()

        CsvToDf.print_columns()
        CsvToDf.remap_data('Log', 90)
        #CsvToDf.smooth_data('mixer_temperature_Funnel',0)

        data_frame_list.append(CsvToDf)

    df1 = data_frame_list[0].get_data_frame()
    df2 = data_frame_list[1].get_data_frame()

    #print(df1['Log'])
    #print(df1['mixer_temperature_Funnel'])

    def temp_data(x_data, y_data):

        # non-linear curve fit
        params, params_covariance = curve_fit(linar_func, x_data, y_data) # popt, pcov
        # a*x + c
        a = params[0]
        c = params[1]
        #print(data['data'][1], data['data'][0])
        print(params)

        #R squred
        residuals = y_data- linar_func(x_data, *params)
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((y_data-np.mean(x_data))**2)
        r_squared = round(1 - (ss_res / ss_tot), 3)
        print(f"R^2:{r_squared}")

        label_line = f"y = {params[0].round(5)}*x + {params[1].round(4)}"
        print(label_line)

        return x_data, y_data, params, label_line

    temp_data_1 = temp_data(df1['Log'], df1['mixer_torque_M2'])
    temp_data_2 = temp_data(df2['Log'], df2['mixer_torque_M2'])



    xlabel = " Time, mins"
    ylabel = " Torque, Nm"
    ax = plt.axes()
    ax.set_xlabel(xlabel, fontsize=24)
    ax.set_ylabel(ylabel, fontsize=24)


    #plt.scatter(x_data, y_data, label='50agg', linestyle = 'solid', linewidth = 0.1, color ='b')




    plt.plot(temp_data_1[0], temp_data_1[1], linestyle = 'solid', linewidth = 0.1, color ='b')
    plt.plot(temp_data_1[0], linar_func(temp_data_1[0], *temp_data_1[2]), linestyle = 'solid', color = 'b', linewidth = 2, label='non-accelerated')
    ax.annotate(xy=(70,35), textcoords='offset points', text= temp_data_1[3], va='center', fontsize = '20')

    plt.plot(temp_data_2[0], temp_data_2[1], linestyle = 'solid', linewidth = 0.1, color ='r')
    plt.plot(temp_data_2[0], linar_func(temp_data_2[0], *temp_data_2[2]), linestyle = 'solid', color = 'r', linewidth = 2, label='accelerated')
    ax.annotate(xy=(70,30), textcoords='offset points', text= temp_data_2[3], va='center', fontsize = '20')


    plt.xlim()
    plt.ylim(0 ,8)

    plt.yticks(np.arange(0, 8, 5))
    plt.xticks(np.arange(0, 95, 10))

    plt.legend(loc="upper left", fontsize = 20)
    #plt.grid()
    plt.show()




"""
    ######################################################
    # replace the speed noise
    ## motor_speed_list= [20, 40, 60, 80, 100, 120]

    arr_list_data_1 = []
    arr_list_data_2 = []

    for data_frame in data_frame_list:
        data_frame.group_by_column("mixer_temperature_Funnel", "Time")
        arr_data_1, arr_data_2 = data_frame.two_cols_to_arr()
        arr_list_data_1.append(arr_data_1)
        arr_list_data_2.append(arr_data_2)
    # data for each impeller

    ######################################################
    # plot atrribute
    plot_attribute = ['data',
                      'label',
                      'make_type',
                      'markersize',
                      'color',
                      'linewidth'
                      'linestyle']


    label_list = []
    for i, file_name in enumerate(DATA_LIST):
        label = input("Enter the experment name here :  ")
        #label = file_name[9:-9] # TODO make to function
        label_list.append(label)


    make_type_list = ['o', '^', '*', 'x', '.','d']
    color_list = ['g', 'b', 'r', 'y', 'm', 'c']

    # to dictionary
    two_data_info_dicts = dataframe_to_dict(arr_list_data_1,
                                                label_list,
                                                make_type_list[:len(label_list)],
                                                color_list[:len(label_list)])


    # for i in DATA_LIST:
    #     draw(speed_torque_info_dicts[i], xlabel='Speed [rpm]', ylabel='Torque [Nm]', ylimit=18.96/2)


    # plot speed-torque
    draw(two_data_info_dicts[0],
         two_data_info_dicts[1],
         xlabel='Time', ylabel='Temperature', ylimit=50)
"""
