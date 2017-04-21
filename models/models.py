import warnings
warnings.filterwarnings('ignore')
import time
import pandas as pd

from sklearn.ensemble import RandomForestRegressor, BaggingRegressor, ExtraTreesRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, make_scorer
from sklearn import grid_search
import random

import os  
mingw_path = 'C:\\Program Files\\mingw-w64\\x86_64-5.3.0-posix-seh-rt_v4-rev0\\mingw64\\bin'  
os.environ['PATH'] = mingw_path + ';' + os.environ['PATH']  

import numpy as np  
import xgboost as xgb 


def mean_squared_error_(ground_truth, predictions):
    return mean_squared_error(ground_truth, predictions) ** 0.5

RMSE = make_scorer(mean_squared_error_, greater_is_better=False)

def grid_search_randomforest(X_train,y_train, n_jobs=5, cv=5, n_estimators= [130,140,150,160,170,180,190,200],\
                             max_depth= [13,14,15,16,17,18,19,20]):
    start_time = time.time()

    clf = RandomForestRegressor(n_estimators=50, max_depth=15, random_state=2017)

    param_grid = {'n_estimators': n_estimators, 'max_depth': max_depth}
    model = grid_search.GridSearchCV(estimator=clf, param_grid=param_grid, n_jobs=n_jobs, cv=cv, verbose=20, scoring=RMSE)
    model.fit(X_train, y_train)

    print('--- Grid Search Completed: %s minutes ---' % round(((time.time() - start_time) / 60), 2))

    return model
    
def grid_search_xgboost(X_train,y_train, n_jobs=5, cv=5,n_estimators=[20,30,40,50,60,70,80,90],\
                             max_depth= [3,4,5,6,7,8,9,10]):
    start_time = time.time()

    clf = xgb.XGBRegressor(max_depth = 6, n_estimators = 100, seed=2017)

    param_grid = {'n_estimators': n_estimators, 'max_depth': max_depth}
    model = grid_search.GridSearchCV(estimator=clf, param_grid=param_grid, n_jobs=n_jobs, cv=cv, verbose=20, scoring=RMSE)
    model.fit(X_train, y_train)

    print('--- Grid Search Completed: %s minutes ---' % round(((time.time() - start_time) / 60), 2))

    return model


def grid_search_extraTrees(X_train,y_train, n_jobs=5, cv=5, n_estimators=[50,60,70,80,90,100,110,120,130,140],\
                             max_depth= [5,6,7,8,9,10,11,12,13,14]):
    start_time = time.time()

    clf = ExtraTreesRegressor(n_estimators=150, max_depth=20, random_state=2017)

    param_grid = {'n_estimators': n_estimators, 'max_depth': max_depth}
    model = grid_search.GridSearchCV(estimator=clf, param_grid=param_grid, n_jobs=n_jobs, cv=cv, verbose=20, scoring=RMSE)
    model.fit(X_train, y_train)

    print('--- Grid Search Completed: %s minutes ---' % round(((time.time() - start_time) / 60), 2))

    return model

def grid_search_GB(X_train,y_train, n_jobs=5, cv=5, n_estimators=[50,60,70,80,90,100,110,120,130,140],\
                             max_depth= [5,6,7,8,9,10,11,12,13,14]):
    start_time = time.time()

    clf = GradientBoostingRegressor(n_estimators= 150,max_depth= 6)

    param_grid = {'n_estimators': n_estimators, 'max_depth': max_depth}
    model = grid_search.GridSearchCV(estimator=clf, param_grid=param_grid, n_jobs=n_jobs, cv=cv, verbose=20, scoring=RMSE)
    model.fit(X_train, y_train)

    print('--- Grid Search Completed: %s minutes ---' % round(((time.time() - start_time) / 60), 2))

    return model