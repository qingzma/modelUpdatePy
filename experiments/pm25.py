# Created by Qingzhi Ma at 2019-09-21
# All right reserved
# Department of Computer Science
# the University of Warwick
# Q.Ma.2@warwick.ac.uk
from __future__ import print_function

import modelupdate.main
import pandas as pd

def run_pm25():
    df= pd.read_csv("data/pm25.csv", header=['year','month',  'day',  'hour',  'pm2.5',  'TEMP',    'PRES',  'cbwd','Iws',  'Is',  'Ir'])
    print(df)


if __name__ == '__main__':
    modelupdate.main.main()
    run_pm25()
