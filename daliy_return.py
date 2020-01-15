import pickle
import os
import pandas as pd
import matplotlib.pyplot as plt


record = pickle.load(open('s.pkl','rb')) #read
# tmp = record['SW公交'][:-1]

file_SW_return = ['data/SW收益率\\SW交通运输\\SW公交.CSV',
 'data/SW收益率\\SW交通运输\\SW机场.CSV',
 'data/SW收益率\\SW交通运输\\SW港口.CSV',
 'data/SW收益率\\SW交通运输\\SW物流.CSV',
 'data/SW收益率\\SW交通运输\\SW航空运输.CSV',
 'data/SW收益率\\SW交通运输\\SW航运.CSV',
 'data/SW收益率\\SW交通运输\\SW铁路运输.CSV',
 'data/SW收益率\\SW交通运输\\SW高速公路.CSV',
 'data/SW收益率\\SW休闲服务\\SW旅游综合.CSV',
 'data/SW收益率\\SW休闲服务\\SW景点.CSV',
 'data/SW收益率\\SW休闲服务\\SW酒店.CSV',
 'data/SW收益率\\SW休闲服务\\SW餐饮.CSV',
 'data/SW收益率\\SW传媒\\SW互联网传媒.CSV',
 'data/SW收益率\\SW传媒\\SW文化传媒.CSV',
 'data/SW收益率\\SW传媒\\SW营销传播.CSV',
 'data/SW收益率\\SW公用事业\\SW水务.CSV',
 'data/SW收益率\\SW公用事业\\SW燃气.CSV',
 'data/SW收益率\\SW公用事业\\SW环保工程及服务.CSV',
 'data/SW收益率\\SW公用事业\\SW电力.CSV',
 'data/SW收益率\\SW农林牧渔\\SW农产品加工.CSV',
 'data/SW收益率\\SW农林牧渔\\SW动物保健.CSV',
 'data/SW收益率\\SW农林牧渔\\SW渔业.CSV',
 'data/SW收益率\\SW农林牧渔\\SW畜禽养殖.CSV',
 'data/SW收益率\\SW农林牧渔\\SW种植业.CSV',
 'data/SW收益率\\SW农林牧渔\\SW饲料.CSV',
 'data/SW收益率\\SW化工\\SW化学制品.CSV',
 'data/SW收益率\\SW化工\\SW化学原料.CSV',
 'data/SW收益率\\SW化工\\SW化学纤维.CSV',
 'data/SW收益率\\SW化工\\SW塑料.CSV',
 'data/SW收益率\\SW化工\\SW橡胶.CSV',
 'data/SW收益率\\SW化工\\SW石油化工.CSV',
 'data/SW收益率\\SW医药生物\\SW中药.CSV',
 'data/SW收益率\\SW医药生物\\SW化学制药.CSV',
 'data/SW收益率\\SW医药生物\\SW医疗器械.CSV',
 'data/SW收益率\\SW医药生物\\SW医疗服务.CSV',
 'data/SW收益率\\SW医药生物\\SW医药商业.CSV',
 'data/SW收益率\\SW医药生物\\SW生物制品.CSV',
 'data/SW收益率\\SW商业贸易\\SW一般零售.CSV',
 'data/SW收益率\\SW商业贸易\\SW专业零售.CSV',
 'data/SW收益率\\SW商业贸易\\SW商业物业经营.CSV',
 'data/SW收益率\\SW商业贸易\\SW贸易.CSV',
 'data/SW收益率\\SW国防军工\\SW地面兵装.CSV',
 'data/SW收益率\\SW国防军工\\SW航天装备.CSV',
 'data/SW收益率\\SW国防军工\\SW航空装备.CSV',
 'data/SW收益率\\SW国防军工\\SW船舶制造.CSV',
 'data/SW收益率\\SW家用电器\\SW视听器材.CSV',
 'data/SW收益率\\SW建筑材料\\SW其他建材.CSV',
 'data/SW收益率\\SW建筑材料\\SW水泥制造.CSV',
 'data/SW收益率\\SW建筑材料\\SW玻璃制造.CSV',
 'data/SW收益率\\SW建筑装饰\\SW专业工程.CSV',
 'data/SW收益率\\SW建筑装饰\\SW园林工程.CSV',
 'data/SW收益率\\SW建筑装饰\\SW基础建设.CSV',
 'data/SW收益率\\SW建筑装饰\\SW房屋建设.CSV',
 'data/SW收益率\\SW建筑装饰\\SW装修装饰.CSV',
 'data/SW收益率\\SW房地产\\SW园区开发.CSV',
 'data/SW收益率\\SW房地产\\SW房地产开发.CSV',
 'data/SW收益率\\SW有色金属\\SW工业金属.CSV',
 'data/SW收益率\\SW有色金属\\SW稀有金属.CSV',
 'data/SW收益率\\SW有色金属\\SW金属非金属新材料.CSV',
 'data/SW收益率\\SW有色金属\\SW黄金.CSV',
 'data/SW收益率\\SW机械设备\\SW专用设备.CSV',
 'data/SW收益率\\SW机械设备\\SW仪器仪表.CSV',
 'data/SW收益率\\SW机械设备\\SW运输设备.CSV',
 'data/SW收益率\\SW机械设备\\SW通用机械.CSV',
 'data/SW收益率\\SW机械设备\\SW金属制品.CSV',
 'data/SW收益率\\SW汽车\\SW其他交运设备.CSV',
 'data/SW收益率\\SW汽车\\SW汽车整车.CSV',
 'data/SW收益率\\SW汽车\\SW汽车服务.CSV',
 'data/SW收益率\\SW汽车\\SW汽车零部件.CSV',
 'data/SW收益率\\SW电子\\SW元件.CSV',
 'data/SW收益率\\SW电子\\SW光学光电子.CSV',
 'data/SW收益率\\SW电子\\SW其他电子.CSV',
 'data/SW收益率\\SW电子\\SW半导体.CSV',
 'data/SW收益率\\SW电子\\SW电子制造.CSV',
 'data/SW收益率\\SW电气设备\\SW电机.CSV',
 'data/SW收益率\\SW电气设备\\SW电气自动化设备.CSV',
 'data/SW收益率\\SW电气设备\\SW电源设备.CSV',
 'data/SW收益率\\SW电气设备\\SW高低压设备.CSV',
 'data/SW收益率\\SW纺织服装\\SW服装家纺.CSV',
 'data/SW收益率\\SW纺织服装\\SW纺织制造.CSV',
 'data/SW收益率\\SW综合\\SW综合.CSV',
 'data/SW收益率\\SW计算机\\SW计算机应用.CSV',
 'data/SW收益率\\SW计算机\\SW计算机设备.CSV',
 'data/SW收益率\\SW轻工制造\\SW包装印刷.CSV',
 'data/SW收益率\\SW轻工制造\\SW家用轻工.CSV',
 'data/SW收益率\\SW轻工制造\\SW造纸.CSV',
 'data/SW收益率\\SW通信\\SW通信设备.CSV',
 'data/SW收益率\\SW通信\\SW通信运营.CSV',
 'data/SW收益率\\SW石油开采\\SW其他采掘.CSV',
 'data/SW收益率\\SW石油开采\\SW煤炭开采.CSV',
 'data/SW收益率\\SW石油开采\\SW石油开采.CSV',
 'data/SW收益率\\SW石油开采\\SW采掘服务.CSV',
 'data/SW收益率\\SW钢铁\\SW钢铁.CSV',
 'data/SW收益率\\SW银行\\SW银行.CSV',
 'data/SW收益率\\SW非银金融\\SW保险.CSV',
 'data/SW收益率\\SW非银金融\\SW多元金融.CSV',
 'data/SW收益率\\SW非银金融\\SW证券.CSV',
 'data/SW收益率\\SW食品饮料\\SW食品加工.CSV',
 'data/SW收益率\\SW食品饮料\\SW饮料制造.CSV']

base = ["000016.SH", "000300.SH", "000852.SH", "000905.SH", "399005.SZ", "399006.SZ"]


keys = list(record.keys())


cum_r = pd.DataFrame()
for a in range(0, len(file_SW_return)):
    data = pd.read_csv(file_SW_return[a], header=[0], encoding='gbk')
    data = data.set_index('日期')
    data.index = pd.to_datetime(data.index)
    data = data.pct_change().fillna(0)

    r = pd.DataFrame()
    for i in range(0, record[keys[a]][:-1].shape[0]):
        year = record[keys[a]][:-1].index[i].year
        month = record[keys[a]][:-1].index[i].month
        if month == 11:
            future = str(year+1) + "-01"
        elif month == 12:
            future = str(year+1) + "-02"
        else:
            future = str(year) + '-' + str(month+2)
        r_i = []
        for j in [0, 1, 2]:
            r_j = data[str(year)+'-'+str(month):future].iloc[:, j]
            r_i.append(r_j.values)
        r_i = pd.DataFrame(r_i).mean().T
        r_i.index = r_j.index
        r_i.name = "return"
        if i == 1:
            r = r_i
        else:
            r = r.append(r_i)

    cum_r[a] = r


def get_return(index):
    df = pd.read_csv(os.path.join('baselines', index + '.csv'),
                     encoding="gbk")
    df = df.set_index('date')
    df.index = pd.to_datetime(df.index)
    df_r = (df['yield']["2014-07":]).cumsum()
    return df_r


for i in base:
    df_i = get_return(i)
    plt.plot(df_i, label=i)


plt.plot(cum_r.mean(axis=1).cumsum(), color='k', label='Portfolio', linewidth='3')
plt.legend()
plt.title("Portfolio Return vs. Baselines")
plt.show()
