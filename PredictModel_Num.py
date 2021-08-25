#!/usr/bin/env python
# coding: utf-8

# In[14]:


from pickle import load
import joblib
import pandas as pd
from datetime import date, datetime
import datetime
import xgboost

course = load(open('course.pkl', 'rb'))
DNN_model = joblib.load('Level3_DNN_model.h5')

# month = int(input("월(9~11) : "))
# week = int(input("평일(0), 주말(1) : "))
# time = int(input("시간(24시간) : "))
# c = input('코스 : ')
# weather = float(input('강우량(mm) : '))

# Month = []
# Week_onehot = []
# Time = []
# Rain = []
# Course = course[c]

# for i in range(len(Course)):
#     Month.append(month)
#     Week_onehot.append(week)
#     Time.append(time)
#     Rain.append(weather)

# df = pd.DataFrame([Month, Week_onehot, Time, Course, Rain]).T
# df.columns = ['Month', 'Week_onehot', 'Time', "Course_Num", 'Weather']
# df.to_csv('model_data.csv', encoding = 'euc-kr', index = False)
 
MON, TUE, WED, THU, FRI, SAT, SUN = range(7)

class holiday2020():
    HOLIDAYS = ((1, 1), #"new Year"
                (1, 24), #"new Year"
                (1, 25), #"new Year1"
                (1, 26), #"new Year2"
                (3, 1), #"3.1"
                (4, 30), #"Buddha Day"
                (5, 5), #"Children's Day"
                (6, 6), #"Memorial Day"
                (8, 15), #"Liberation Day"
                (9, 30), #"Thanksgiving"
                (10, 1), #"Thanksgiving1"
                (10, 2), #"Thanksgiving2"
                (10, 3), #"National Foundation Day"
                (10, 9), #"Hangul Day"
                (12, 25) #"Christmas"
                )
 
    def is_holiday(self, daytuple):
        HOLIDAYS = self.HOLIDAYS
        if daytuple in HOLIDAYS:
            return 1
        else:
            return 0
        
class Predict:
    def __init__(self, data):
        self.dataPath = data
    
    def fit(self):
        file = pd.read_csv(self.dataPath)
        t = [0, 0, 0, 0, 0, 1, 1]
        day = file['Week_onehot'][0]
        file['Week_onehot'] = datetime.datetime(2020, int(file['Month'][0]), int(file['Week_onehot'][0])).date().weekday()
        file['Week_onehot'] = t[file['Week_onehot'][0]]
        nowholiday = holiday2020()
        if nowholiday.is_holiday(datetime.datetime(2020, int(file['Month'][0]), int(day)).date()) == 1:
            file['Week_onehot'] = 1
        file.to_csv('test.csv')
        result = DNN_model.predict_classes(file)        
        return result

# print(XGB_model.predict(test))


# In[ ]:





# In[ ]:





# In[ ]:




