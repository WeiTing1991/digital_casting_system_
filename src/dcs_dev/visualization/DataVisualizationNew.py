## install panda, matplotlib, scipy
import os
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import odr

#from sklearn.preprocessing import StandardScaler
from scipy.optimize import curve_fit


class CSVToDataFrame:
    """ CSV data to Panda Dataframe
    """

    def __init__(self, filename:str, data_folder_path:str):
        """ Initialize the csv path
        """
        self.CSV_DIR = os.path.abspath(os.path.join(data_folder_path, filename))

    # Setter and Getter
    def set_data_frame(self) -> None:
        """ set panda data frame
        """
        self.df = pd.read_csv(self.CSV_DIR)

    def get_data_frame(self)-> object:
        """ get panda data frame
        """
        return self.df

    # printer
    def print_head(self)-> None:
        """ print whole head of data frame
        """
        print(self.df.head())

    def print_columns(self)-> None:
        """ print whole colums of data frame
        """
        print(self.df.columns)

    def print_single_column(self, col)-> None:
        """ print the data from a column
        """
        print(self.df[col])

    def get_time_interval(self)-> float:
        """
        """
        start_time_str = self.df["Time"][0]
        end_time_str = self.df["Time"][1]

        delta_time = datetime.strptime(end_time_str, '%H:%M:%S.%f') - datetime.strptime(start_time_str, '%H:%M:%S.%f')
        return delta_time.total_seconds()

    # Method
    def clean_noise_data(self, colume_name: str, replace_num:int, tolerance:int) -> None:
        """
        """
        min_num = replace_num - tolerance
        max_num = replace_num + tolerance

        self.df[colume_name] = np.where(self.df[colume_name].between(min_num, max_num), replace_num, self.df[colume_name])

    def average_two_columns(self, col_1, col_2, new_col) -> None:
        """
        average data from the two column to new column
        """
        self.df[new_col] = (self.df[col_1] + self.df[col_2])/2

    def standardize_data(self, col:str, type:str)-> None:
        """
        standardize data
        TODO: check the standardscaler
        """
        if type == "first":
        # Standardize data with first value
            self.df[col] = self.df[col] - self.df[col][0]

        elif type == "mean":
        # Standardize data with mean
            self.df[col] = self.df[col] - self.df[col].mean()

    def standardize_allcolumn_data(self)-> None:
        """
        standardize data
        """
        # Standardize data with first value
        for column in self.df.columns.values:
            if column != "Time":
                self.standardize_data(column, "mean")

    def normalize_data(self, col, remap_Max)-> None:
        """
        normalize the data
        """
        scale_data = (self.df[col] - self.df[col].min()) / (self.df[col].max() - self.df[col].min())
        self.df[col] = (scale_data*remap_Max).round(2)

    def log_to_time(self, col, record_time) -> None:
        """
        convert Log to real time
        """
        self.df[col] = (self.df["Log"]*record_time)/60

    def smooth(self, col, factor) -> None:
        """
        smooth the data with average
        """
        self.df[col] = (self.df[col]*(1-factor) + self.df[col].mean()*factor).round(2)


class PlotData:
    """ the class is to plot data from Panda DataFrame
        dataframe_list:list
        col_x:str
        col_y:str

    """
    def __init__(self, dataframe_list:list, col_x:str, col_y:str):
        """ Initialize the plot attribute
        """
        self.df_list = dataframe_list
        self.data_x_col = col_x
        self.data_y_col = col_y

        self.fig, self.ax = plt.subplots()

            # plot atrribute
        self.make_type_list = ['o', '^', '*', 'x', '.','d']
        self.color_list = ['blue', 'red', 'green', 'orange', 'purple', 'cyan']

    # getter
    def get_column_data(self, col) -> object:
        return self.df[col]

    # print
    def print_df(self)-> None:
        """
        """
        print(self.df_list)

    # Method
    def linar_func(self, x, a, c) -> float:
        return a*x + c
    def exponential_func(self, x, a, b, c) -> float:
        return a*np.exp(-b * x) + c

    def fitting_curve(self, data_x:list, data_y:list, func_type:str, curve_dgree = 2) -> dict:
        """
        func_type: linar: linar_func; exp:exponential_func; poly: polynomial_func

        data_dict["result"] = residuals
        data_dict["label_line"] = label_line
        data_dict["R_squared"] = R_squared

        """
        label_func:str
        data_dict ={}

        if func_type == "linar":
            func = self.linar_func
            params, params_covariance = curve_fit(func, data_x, data_y) # popt, pcov, a*x + c

            label_func = f"y = {params[0].round(5)}x + {params[1].round(5)}"
            result = func(data_x, *params)

        elif func_type == "exp":
            func = self.exponential_func
            params, params_covariance = curve_fit(func, data_x, data_y) # popt, pcov

            label_func = f"y ={params[0].round(5)}" + f"e$^{{{params[2].round(5)}}}$$^x$ + " + f"{params[2].round(5)}"
            result = func(data_x, *params)

        elif func_type == "poly":

            poly_model = odr.polynomial(2)  # using third order polynomial model
            data = odr.Data(data_x, data_y)
            odr_obj = odr.ODR(data, poly_model)
            output = odr_obj.run()  # running ODR fitting
            params = output.beta[::-1]
            poly = np.poly1d(params)

            label_func = f"y = {params[0].round(5)}x$^2$ + {params[1].round(5)}x + {params[2].round(5)}"
            result = poly(data_x)

        #R squred
        residuals = data_y- result
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((data_y-np.mean(data_x))**2)
        r_squared = round(1 - (ss_res / ss_tot), 3)
        R_squared = f"R$^2$:{r_squared}"


        print(params)
        print(R_squared)
        #print(label_line)

        data_dict["result"] = result
        data_dict["label_func"] = label_func + ", "+ R_squared
        #data_dict["R_squared"] = R_squared
        return data_dict

    def set_label(self):
        label = input("Please enter the name of this plot: ")
        return str(label).lower()


    def plot_layout(self,
                    xlabel:str = "None", ylabel:str = "Nnne",
                    xlim_min = 0, xlim_max=90,
                    ylim_min = 0, ylim_max=30,
                    xinterval = 10, yinterval = 5,
                    axis_fontsize = 20, fontsize = 30, fontweight = "regular"
                    ):
        """
        Set the plot layout
        """
        # set range of x and y axis
        self.ax.set(xlim = (xlim_min, xlim_max),
                    ylim = (ylim_min ,ylim_max),
                    )
        self.ax.set_xticks(np.arange(xlim_min, xlim_max+5, xinterval), fontweight=fontweight)
        self.ax.set_yticks(np.arange(ylim_min, ylim_max+5, yinterval), fontweight=fontweight)
        self.ax.tick_params(labelsize = axis_fontsize)

        # set x, y axis label
        self.ax.set_xlabel(xlabel, fontweight=fontweight, fontsize=fontsize)
        self.ax.set_ylabel(ylabel, fontweight=fontweight, fontsize=fontsize)


    def draw_plot(self,
                  curve_fitting_type:str ='linar',
                  curve_fit:bool =False,
                  figure_type:str = "plot",
                  ax_x=0, ax_y=0,
                  ax_y_spacing = 0.5, fontsize:int = 15) ->None:

        for i, df in enumerate(self.df_list):

            data_x = df[self.data_x_col]
            data_y = df[self.data_y_col]
            data_dict = self.fitting_curve(data_x, data_y, curve_fitting_type)

            plot_label = self.set_label()

            if figure_type == "plot":
                # draw plot
                self.ax.plot(data_x, data_y, linestyle = '-', linewidth = 0.5, color = self.color_list[i],label= plot_label)
            elif figure_type == "point":
                # draw point
                self.ax.scatter(data_x, data_y, marker=self.make_type_list[i], s=10, color = self.color_list[i], alpha=0.5,label= plot_label)

            if curve_fit:
                self.ax.plot(data_x, data_dict["result"], linestyle = '-.', linewidth = 2, color = self.color_list[i], label= plot_label)

                x = self.ax.get_xlim()[1]*3/4
                y = self.ax.get_ylim()[1]*3/4

                self.ax.annotate(xy=(x, y+i*ax_y_spacing), text= data_dict["label_func"],
                                fontsize = fontsize, color = self.color_list[i])

        plt.legend(loc="upper left", fontsize = fontsize)

    def run(self) -> None:
        plt.show()


#Test
#################################################################################

def single_file_test(DATA_LIST):

    xlabel = " Time, min"
    ylabel = " Temperature, ℃"

    data_frame_list = []
    column_list = [
                   "mixer_temperature_Funnel_outlet",
                   "mixer_temperature_Funnel",
                   "mixer_temperature_Funnel_plate",
                   "mixer_motor_temperature_M1",
                   "mixer_motor_temperature_M2"
                    ]

    data_x_name = "Log"
    data_y_name = "Temperature"

    for i, file_name in enumerate(DATA_LIST):
        print(file_name)
        print("Are you decide to use this file")
        bool_sellected = str(input("Please enter y or n: "))

        if bool_sellected.lower() == "y" :
            CsvToDf = CSVToDataFrame(file_name, DATA)
            CsvToDf.set_data_frame()

            #CsvToDf.standardize_allcolumn_data()
            CsvToDf.normalize_data("Log", 90)

            df = CsvToDf.get_data_frame()

            for column in column_list:
                new_df = df[[column, "Log"]].copy()
                new_df["Temperature"] = new_df[column].copy()
                data_frame_list.append(new_df)
        else:
            continue

    plot = PlotData(dataframe_list=data_frame_list, col_x= data_x_name, col_y= data_y_name)

    plot.plot_layout(xlabel = xlabel, ylabel= ylabel,
                    xlim_min = 0, xlim_max=90, xinterval = 10,
                    ylim_min = 15, ylim_max=40, yinterval = 5)


    plot.draw_plot(curve_fitting_type ='linar', figure_type = "plot",
                   ax_x=0, ax_y=0,
                   ax_y_spacing = 0.8, fontsize= 15)
    plot.run()

def mutlifile_test(DATA_LIST, xlabel, ylabel, data_x_name, data_y_name, standardize_data_x: bool = False, standardize_data_y: bool = True):

    total_time = 90 # min
    data_frame_list = []
    for i, file_name in enumerate(DATA_LIST):

        print(file_name)
        print("Are you decide to use this file")
        bool_sellected = str(input("Please enter y or n: "))
        if bool_sellected.lower() == "y" :
            CsvToDf = CSVToDataFrame(file_name, DATA)
            CsvToDf.set_data_frame()

            # normalize the log to time data, time interval is 1 second
            interval_time = CsvToDf.get_time_interval()
            print(interval_time)


            CsvToDf.log_to_time("Real_Time_inteval", interval_time)

            #CsvToDf.normalize_data('Log', 90)
            CsvToDf.smooth(data_y_name, factor=0.5)

            if standardize_data_x:
                CsvToDf.standardize_data(data_x_name, "first")
            if standardize_data_y:
                CsvToDf.standardize_data(data_y_name, "first")


            df = CsvToDf.get_data_frame()
            data_frame_list.append(df)

        else:
            continue

    # Plot the data
    plot = PlotData(dataframe_list=data_frame_list, col_x=data_x_name, col_y=data_y_name)

    plot.plot_layout(xlabel = xlabel, ylabel= ylabel,
                    xlim_min = 0, xlim_max=90, xinterval = 10,
                    ylim_min = 15, ylim_max=40, yinterval = 10)

    plot.draw_plot(curve_fit=False, curve_fitting_type ='linar', figure_type = "plot",
                   ax_x=0, ax_y=0,
                   ax_y_spacing = 0.8, fontsize= 15)
    plot.run()

    #label_list = [50agg_60rpm, 50agg_120rpm, 54agg_120rpm, 54agg_120rpm_Acc]

"""
## Data sorting naming:
### Log
Data log order

### Inline mixer:
two motor system, M1 is motor 1, M2 is Motor 2
- mixer_motor_temperature_M2
- mixer_motor_temperature_M1
- mixer_torque_M2
- mixer_torque_M1
- mixer_speed_M2
- mixer_speed_M1

### Funnel
- mixer_temperature_Funnel_outlet
- mixer_temperature_Funnel
- mixer_temperature_Funnel_plate

### Concrete pump
- cp_temperature : concrete pump temperature
- cp_pressure : concrete pump pressure
- cp_flowrate : concrete pump set flowrate

### Accelerator pump
- ac_flowrate : accelerator pump flowrate

### Time
real time format : Min:Sec
"""


if __name__ == "__main__":

    HERE = os.path.dirname(__file__)
    HOME = os.path.abspath(os.path.join(HERE, "../../../"))
    DATA = os.path.abspath(os.path.join(HOME, "data/csv"))

    FILFE_NAME_LIST = ["20230626_50agg_70S_1.5FW_ETH_temperature_60rpm.csv",
                       "20230704_50agg_72S_1.5FW_ETH_temperature_120rpm.csv",
                       "20230706_54agg_72S_1.5FW_ETH_temperature_120rpm.csv",
                       "20230713_54agg_70S_1.5FW_TemperatureCAC_120rpm.csv"
                       ]


    input_plot_mode = input("the plot will be muitifile comparsion?: \n Please enter yes or no: ")
    DATA_LIST = FILFE_NAME_LIST

    if input_plot_mode == "y":
        #mutlifile_test(DATA_LIST, xlabel= "Time, min", ylabel= "Δ Funnel Temperature, ℃", data_x_name="Log", data_y_name= "mixer_temperature_Funnel")

        mutlifile_test(DATA_LIST, xlabel= "Time, min", ylabel= "Funnel Temperature, ℃",
                       standardize_data_y= False, data_x_name="Real_Time_inteval", data_y_name= "mixer_temperature_Funnel")

        # mutlifile_test(DATA_LIST, xlabel= "Time, min", ylabel= "Motor Temperature, ℃",
        #                standardize_data_y= False, data_x_name="Log", data_y_name= "mixer_motor_temperature_M2")


        # mutlifile_test(DATA_LIST, xlabel= "Time, min", ylabel= "CP Temperature, ℃",
        #                standardize_data_y= False, data_x_name="Log", data_y_name= "cp_temperature")

        #mutlifile_test(DATA_LIST, xlabel= "Time, min", ylabel= "Δ Motor Temperature, ℃", data_x_name="Log", data_y_name= "mixer_motor_temperature_M2")

        # mutlifile_test(DATA_LIST, xlabel= "Δ Motor Temperature, ℃", ylabel= "Torque, Nm",
        #                 standardize_data_x= True, standardize_data_y= False,
        #                 data_x_name="mixer_motor_temperature_M2", data_y_name= "mixer_torque_M2")

        # mutlifile_test(DATA_LIST, xlabel= "Δ funnel Temperature, ℃", ylabel= "Torque, Nm",
        #                 standardize_data_x= True, standardize_data_y= False,
        #                 data_x_name="mixer_temperature_Funnel", data_y_name= "mixer_torque_M2")


    else:
        single_file_test(DATA_LIST)
