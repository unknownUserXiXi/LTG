import Function as fc
import matplotlib.pyplot as plt
import os
import pandas as pd
import time
import pickle


# 获取行业因子数据的文件路径，返回一个list
def get_file_path_list(path):
    file_path = []
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            # 获取文件路径
            file_path.append(os.path.join(root, file))
            file_list.append(file.split('.')[0])
    return file_path, file_list


def get_return_path(name, path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if name == file:
                # 获取文件路径
                file_path=os.path.join(root, file)
                break
    return file_path


if __name__ == "__main__":
    file_SW, file_list = get_file_path_list("data/SW")  # 行业因子文件list
    file_SW_return = []  # 对应行业收益率文件路径list
    for i in file_SW:
        file_name = i.split("\\")[2]
        file_SW_return.append(get_return_path(file_name, "data/SW收益率"))

    total_r = []
    total_s = {}
    begin_time=time.time()
    j=0

    w = pd.read_csv("weights.csv", index_col=[0])
    for i in range(0, len(file_SW)):
        j = j+1
        if j % 10 == 0:
            print(time.time()-begin_time)

        print("Loading Factor.....", file_SW[i])
        LTG_pd_month_standard, n = fc.get_factor_data(file_SW[i])
        if n>=3:
            s = fc.get_LTG(list(w.iloc[i]), LTG_pd_month_standard, n)
            total_s[file_SW[i].split("\\")[2].split('.')[0]]=s
            print("Loading Return.....", file_SW_return[i])
            cum_r = fc.get_LTG_return(file_SW_return[i], s)
            total_r.append(cum_r.values.flatten())
        else:
            print(file_SW[i].split("\\")[2].split('.')[0] + 'industry is too small!')

    r = pd.DataFrame(total_r, index=file_list)
    r.to_csv("total_r.csv")

    pickle.dump(total_s, open('s.pkl','wb'))  #save
    # record = pickle.load(open('s.pkl','rb')) #read


