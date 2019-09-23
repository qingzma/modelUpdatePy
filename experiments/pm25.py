# Created by Qingzhi Ma at 2019-09-21
# All right reserved
# Department of Computer Science
# the University of Warwick
# Q.Ma.2@warwick.ac.uk
from __future__ import print_function

import modelupdate.main
import pandas as pd
import numpy as np

from crosstrainer import CrossTrainer
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error

import pickle


def run_pm25():
    df = pd.read_csv("data/pm25.csv", header=0)
    # names=['year', 'month', 'day', 'hour', 'pm2.5', 'DEWP', 'TEMP', 'PRES', 'cbwd', 'Iws', 'Is', 'Ir'])
    df = df.dropna(subset=['pm2.5'])

    headers = list(df.columns)
    headers.remove('pm2.5')
    headers.remove('cbwd')

    X = df[headers].values
    Y = df['pm2.5'].values

    X_target, X_source, y_target, y_source = train_test_split(X, Y, test_size=0.4, random_state=11)
    X_new, X_test, y_new, y_test = train_test_split(X_target, y_target, test_size=0.5, random_state=11)

    lr_weighted = linear_model.LogisticRegression()
    ct = CrossTrainer(lr_weighted, k=5, delta=0.01)
    lr_weighted, alpha = ct.fit(X_target, y_target, X_source, y_source)

    y_pred_test = lr_weighted.predict(X_test)

    print("For weighted combination")
    print("alpha is " + str(alpha))
    print(mean_absolute_error(y_test, y_pred_test))
    print(mean_squared_error(y_test, y_pred_test))
    print("-------------------------------------------")
    print()

    print("on all data")
    X_combined = np.concatenate((X_target, X_new))
    y_combined = np.concatenate((y_target, y_new))

    lr_combined = linear_model.LogisticRegression()
    lr_combined.fit(X_combined, y_combined)
    y_pred_combined = lr_combined.predict(X_test)
    print(mean_absolute_error(y_test, y_pred_combined))
    print(mean_squared_error(y_test, y_pred_combined))
    print("-------------------------------------------")
    print()

    print("saving model...")
    with open("lr_weighted.pkl", 'wb') as f_weighted:
        pickle.dump(lr_weighted, f_weighted, protocol=pickle.HIGHEST_PROTOCOL)
    with open("l_combined.pkl", 'wb') as f_combined:
        pickle.dump(lr_combined, f_combined, protocol=pickle.HIGHEST_PROTOCOL)
    print("Models saved.")


if __name__ == '__main__':
    modelupdate.main.main()
    run_pm25()
