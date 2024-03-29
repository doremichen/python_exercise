# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 08:57:30 2019

@author: AdamChen
"""
from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

head_Html_lotto='http://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx'
res = requests.get(head_Html_lotto, timeout=30)
# print(res.text)

winning_Numbers_Sort_lotto = ['Lotto649Control_history_dlQuery_No1_', \
                              'Lotto649Control_history_dlQuery_No2_', \
                              'Lotto649Control_history_dlQuery_No3_', \
                              'Lotto649Control_history_dlQuery_No4_', \
                              'Lotto649Control_history_dlQuery_No5_', \
                              'Lotto649Control_history_dlQuery_No6_', \
                              'Lotto649Control_history_dlQuery_SNo_']

def search_winning_numbers(css_class):
    global winning_Numbers_Sort_lotto
    if(css_class != None):
        for i in range(len(winning_Numbers_Sort_lotto )):
            if winning_Numbers_Sort_lotto [i] in css_class:
                return css_class
            

def parse_tw_lotto_html(data_Info,number_count):  
    data_Info_List = []
    data_Info_Dict = {}
    tmp_index = 0
    for index  in range(len(data_Info)) :
        if (index == 0):
            #用data_Info[index].text 即可取得獎號
            data_Info_List.append(data_Info[index].text)  
        else:
            if(index % number_count != 0):
                data_Info_List.append(data_Info[index].text)
            else:
                data_Info_Dict[str(tmp_index)] = list(data_Info_List)
                data_Info_List= []
                data_Info_List.append(data_Info[index].text)
                tmp_index = tmp_index+1
        data_Info_Dict[str(tmp_index)] = list(data_Info_List)
    return data_Info_List,data_Info_Dict


soup = BeautifulSoup(res.text,'lxml')

header_Info = soup.find_all(id=search_winning_numbers)
data_Info_List,data_Info_Dict  = parse_tw_lotto_html(header_Info,7)
print(data_Info_Dict)
    

with open('index.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(data_Info_List)
    
with open('index.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for k,v in data_Info_Dict.items():
        writer.writerow([k, data_Info_Dict[str(k)]])
    
    



