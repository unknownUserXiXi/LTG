import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np


colors = ['black', 'gray', 'lightgray', 'rosybrown', 'lightcoral',
          'maroon', 'red', 'chocolate', 'sandybrown', 'peachpuff',
          'darkgoldenrod', 'gold', 'olive','yellowgreen','greenyellow',
          'honeydew', 'lightseagreen', 'teal', 'cyan', 'deepskyblue',
          'steelblue', 'royalblue','navy','slateblue','blueviolet',
          'violet', 'crimson', 'pink']

df = pd.read_csv("total_r.csv", encoding='gbk', index_col=[0]).T
df.index = pd.to_datetime(df.index)

first_indu = os.listdir("data/SW")

for i in np.arange(0, 28):
    for root, dirs, files in os.walk("data/SW"):
        if root == os.path.join("data/SW", first_indu[i]):
            file_list = []
            for file in files:
                file_list.append(file.split(".")[0])
            df_ind = df[file_list].mean(axis=1)
            plt.plot(df_ind, label=first_indu[i], color=colors[i], linewidth='3')
plt.legend()
plt.title("Return of 28 industries")
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()


