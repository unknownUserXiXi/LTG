import pandas as pd
import numpy as np


test = pd.read_csv("s.csv", encoding="unicode_escape")
test = test.set_index('date')
print(test)
#LTGreturn(test)
SWGangtie = pd.read_excel('SW.xlsx', encoding="unicode_escape")
# delete two lines

SWGangtie = SWGangtie.set_index('日期')
SWGangtie.index = pd.to_datetime(SWGangtie.index)

gt_monthly = SWGangtie.resample('3M').mean()
return_monthly = gt_monthly.pct_change()[1:]
print(return_monthly)

LTGreturn = pd.DataFrame()
for i in test.index:
    for j in ['0', '1', '2']:
        LTGreturn.loc[i, j] = return_monthly.loc[i, test.loc[i, j]]
print(LTGreturn+1)
