
## install panda, matplotlib, scipy
import math
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit


class CSVToDataFrame:
    """ CSV data to panda dataframe"""
    def __init__(self, filename:str, data_folder_path:str):

        CSV_DIR = os.path.abspath(os.path.join(data_folder_path, filename))
        self.df = pd.read_csv(CSV_DIR)

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

    def average_data(self, col_1, col_2, new_col):
        self.df[new_col] = (self.df[col_1] + self.df[col_2])/2


    def group_by_column(self, col_1, col_2,):
        """
        TODO: **kwargs
        """
        gp_by_columns = self.df[[col_1, col_2]].groupby(col_1).mean()

        col_1_list = np.array(list(gp_by_columns.index))
        col_2_list = gp_by_columns.to_numpy().flatten().round(3)

        self.col_1_list = col_1_list
        self.col_2_list = col_2_list

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



class PlotFromData:
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


    ###########################################################
    # TODO put in to function
    # Input the file Name
    # number_files = input("How many data you want plot")

    # file_name_list = []
    # for i in number_files:
    #     """
    #     example:
    #     FILFE_NAME_LIST = ["20230116_54agg_40G_70S_5FW_Thun.csv",
    #                     "20230117_56agg_40G_67S_5FW_Thun.csv"
    #                     ]
    #     """
    #     file_name = input("file_name")
    #     file_name_list.append(file_name)

    FILFE_NAME_LIST = ["20230110_54agg_30G_73.5S_3FW_Thun.csv",
                        "20230110_56agg_40G_78S_3FW_Thun.csv",
                        "20230123_58agg_30G_75S_3FW_Thun_3.csv",
                        "20230123_60agg_30G_79S_3FW_Thun.csv"
                       ]

    FILFE_NAME_LIST_2 = ["20230110_56agg_40G_78S_5FW_Thun.csv",
                       "20230123_60agg_30G_79S_3FW_Thun.csv",
                       "20230117_56agg_40G_54S_5FW_Thun.csv",
                       ]

    FILFE_NAME_LIST_3 = ["20230123_60agg_30G_79S_3FW_Thun.csv",
                        "20230123_60agg_30G_79S_5FW_Thun.csv",
                        "20230123_60agg_30G_79S_7FW_Thun.csv",
                        ]
    FILFE_NAME_LIST_4 = ["20230511_56agg_30G_76S_3FW_Thun_setuup.csv",
                        "20230511_56agg_30G_76S_3FW_Thun_setuup.csv"
                       ]


    ###########################################################

    DATA_LIST = FILFE_NAME_LIST_4

    data_frame_list = []
    for file_name in DATA_LIST:
        data = CSVToDataFrame(file_name, DATA)
        data_frame_list.append(data)

    ######################################################
    # replace the speed noise
    motor_speed_list= [20, 40, 60, 80, 100, 120]

    arr_speed_torque_list = []
    arr_power_speedspaue_list = []
    for data_frame in data_frame_list:
        data_frame.average_data("mixer_speed_M1", "mixer_speed_M2", "mixer_speed_average")
        data_frame.average_data("mixer_torque_M1", "mixer_torque_M2", "mixer_torque_average")
        for speed in motor_speed_list:
            data_frame.clean_noise_data("mixer_speed_average",speed, 10)

        data_frame.group_by_column("mixer_speed_average", "mixer_torque_average")

        arr_speed_torque, arr_power_speedspaue = data_frame.two_cols_to_arr()
        arr_speed_torque_list.append(arr_speed_torque)
        arr_power_speedspaue_list.append(arr_power_speedspaue)

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
    speed_torque_info_dicts = dataframe_to_dict(arr_speed_torque_list,
                                                label_list,
                                                make_type_list[:len(label_list)],
                                                color_list[:len(label_list)])

    power_speedspaue_info_dicts = dataframe_to_dict(arr_power_speedspaue_list,
                                                    label_list,
                                                    make_type_list[:len(label_list)],
                                                    color_list[:len(label_list)])


    # for i in DATA_LIST:
    #     draw(speed_torque_info_dicts[i], xlabel='Speed [rpm]', ylabel='Torque [Nm]', ylimit=18.96/2)


    # plot speed-torque
    draw(speed_torque_info_dicts[0],
         speed_torque_info_dicts[1],

         xlabel='Speed [rpm]', ylabel='Torque [Nm]', ylimit=18.96/2)

    # plot speedspaue-power
    draw(power_speedspaue_info_dicts[0],
         power_speedspaue_info_dicts[1],
         xlabel='$Speed^2$ [$(rpm)^2$]', ylabel='Power [w]', ylimit=1.38*1000/10)
