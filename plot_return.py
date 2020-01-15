# -*- coding: utf-8 -*-
import pandas as pd
import os
import matplotlib.pyplot as plt


base = ["000016.SH", "000300.SH", "000852.SH", "000905.SH", "399005.SZ", "399006.SZ"]


def get_return(index):
    df = pd.read_csv(os.path.join('baselines', index + '.csv'),
                     encoding="gbk")
    df = df.set_index('date')
    df.index = pd.to_datetime(df.index)
    df_r = (df['yield']).cumsum()
    return df_r


def plot_base_return(index=None):
    if index is not None:
        df_r = get_return(index)
        plt.plot(df_r)
        plt.show()
    else:
        for i in base:
            df_i = get_return(i)
            plt.plot(df_i)
        plt.legend(base, loc='upper right')
        plt.show()


if __name__ == "__main__":
    # plot_base_return("000300.SH")
    # plot_base_return()

    df = pd.read_csv("total_r.csv", encoding='gbk', index_col=[0]).T
    df.index = pd.to_datetime(df.index)

    # plt.plot(df.index, df.mean(axis=1), label='Portfolio')
    # plt.scatter('2015-10-31', 0.730440)
    # plt.plot(pd.to_datetime(['2015-10-31', '2015-10-31']), [0, 0.730440],
    #          color='blue', linewidth=2.5, linestyle="--")
    # plt.scatter('2018-10-31', 0.440444)
    # plt.plot(pd.to_datetime(['2018-10-31', '2018-10-31']), [0, 0.440444],
    #          color='blue', linewidth=2.5, linestyle="--")
    # plt.legend()

    plt.plot(df.index, df.mean(axis=1).cumsum(), label='Portfolio')
    plt.legend()
    plt.title("Portfolio Return")
    plt.show()
