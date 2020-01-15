import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

LTG_pd = pd.read_csv("data/SW\SW休闲服务\SW其他休闲服务.CSV",header=[0],encoding='gbk')
# LTG_pd = pd.read_csv("SW钢铁.csv",header=[0],encoding='gbk')
LTG_pd['日期']=pd.to_datetime(LTG_pd['日期'])
LTG_pd=LTG_pd.set_index('日期')
LTG_pd_month=LTG_pd.resample('3m').mean()
LTG_pd_month_standard=LTG_pd.resample('3m').mean()
LTG_pd_month_number=LTG_pd.resample('3m').mean()
n=int(LTG_pd.shape[1]/6)
LTG_pd_month = LTG_pd_month.fillna(0)
LTG_pd_month_standard = LTG_pd_month_standard.fillna(0)
LTG_pd_month_number = LTG_pd_month_number.fillna(0)

for i in range(LTG_pd_month.shape[0]):   #归一化
    for j in range(LTG_pd_month.shape[1]):
        if (j>=0 and j<n):
            mean=LTG_pd_month.iloc[i,0:n].mean()
            std = LTG_pd_month.iloc[i, 0:n].std()
            LTG_pd_month_standard.iloc[i,j]=(LTG_pd_month_standard.iloc[i,j]-mean)/std
        elif (j>=n and j<2*n):
            mean=LTG_pd_month.iloc[i,n:2*n].mean()
            std = LTG_pd_month.iloc[i, n:2*n].std()
            LTG_pd_month_standard.iloc[i,j]=(LTG_pd_month_standard.iloc[i,j]-mean)/std
        elif (j>=2*n and j<3*n):
            mean=LTG_pd_month.iloc[i,2*n:3*n].mean()
            std = LTG_pd_month.iloc[i, 2 * n:3* n].std()
            LTG_pd_month_standard.iloc[i,j]=(LTG_pd_month_standard.iloc[i,j]-mean)/std
        elif (j>=3*n and j<4*n):
            mean=LTG_pd_month.iloc[i,3*n:4*n].mean()
            std=LTG_pd_month.iloc[i,3*n:4*n].std()
            LTG_pd_month_standard.iloc[i,j]=(LTG_pd_month_standard.iloc[i,j]-mean)/std
        elif (j>=4*n and j<5*n):
            mean=LTG_pd_month.iloc[i,4*n:5*n].mean()
            std = LTG_pd_month.iloc[i, 4 * n:5 * n].std()
            LTG_pd_month_standard.iloc[i,j]=(LTG_pd_month_standard.iloc[i,j]-mean)/std
        else:
            mean=LTG_pd_month.iloc[i,5*n:6*n].mean()
            std = LTG_pd_month.iloc[i, 5 * n:6 * n].std()
            LTG_pd_month_standard.iloc[i,j]=(LTG_pd_month_standard.iloc[i,j]-mean)/std

w=[0.3,0.2,0.2,0.1,0.1,0.1] #权重向量

for i in range(LTG_pd_month_standard.shape[0]):  # 算权重数
    for j in range(n):
        LTG_pd_month_standard.iloc[i, j] = LTG_pd_month_standard.iloc[
                                               i, j] * 0.3 + \
                                           LTG_pd_month_standard.iloc[
                                               i, j + n] * 0.2 + \
                                           LTG_pd_month_standard.iloc[
                                               i, j + 2 * n] * 0.2 + \
                                           LTG_pd_month_standard.iloc[
                                               i, j + 3 * n] * 0.1 + \
                                           LTG_pd_month_standard.iloc[
                                               i, j + 4 * n] * 0.1 + \
                                           LTG_pd_month_standard.iloc[
                                               i, j + 5 * n] * 0.1
LTG_pd_month_standard = LTG_pd_month_standard.iloc[:, 0:n]

s = np.zeros(shape=(LTG_pd_month_standard.shape[0], 3))  # 选龙头股
s = pd.DataFrame(s)
for i in range(LTG_pd_month_standard.shape[0]):  # 排序
    for j in range(3):
        s.iloc[i, j] = \
        LTG_pd_month_standard.iloc[i].sort_values(ascending=False).index[j]
s.index = LTG_pd_month_standard.index
s = s.drop(s.index[0])
# s.to_csv('s.csv')

SWGangtie = pd.read_csv('data/SW收益率\SW休闲服务\SW其他休闲服务.CSV', header=[0],encoding='gbk')
# SWGangtie = pd.read_csv('SWiron.CSV', header=[0],encoding='gbk')
SWGangtie = SWGangtie.set_index('日期')
SWGangtie.index = pd.to_datetime(SWGangtie.index)
# return_monthly = (1+SWGangtie.pct_change()[1:]).resample('3M').prod()
# return_monthly = SWGangtie.resample('3M').last().pct_change()[1:]
# return_monthly = SWGangtie.resample('3M').mean().pct_change()[1:]
# return_monthly = 1+SWGangtie.resample('3M').mean().pct_change()[1:]
# return_monthly = SWGangtie.resample('3M').mean().pct_change()[1:]
return_monthly = (SWGangtie.pct_change()[1:]).resample('3M').sum()

LTGreturn = pd.DataFrame()
for i in s.index:
    for j in [0, 1, 2]:
        LTGreturn.loc[i, j] = return_monthly.loc[i, s.loc[i, j]]
# LTGreturn.to_csv('LTGreturn.csv')

simple_r = []
for i in range(LTGreturn.shape[0]):
    simple_r.append((LTGreturn.iloc[i,:].sum())/3)
simple_r = pd.DataFrame(simple_r, index=LTGreturn.index)
cum_r = (simple_r).cumsum()
# cum_r.to_csv('re.csv')

plt.plot(cum_r)
plt.xlabel("DATE")
plt.ylabel("RETURN")
plt.title("SWiron RETURN")
plt.show()