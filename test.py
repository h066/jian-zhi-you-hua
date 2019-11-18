# python3
# -*- coding: utf-8 -*-
# @Author  : lina
# @Time    : 2018/5/13 11:40
import fp_growth_py3 as fpg
from csv import reader
import pandas as pd
import csv
import pandas as pd
import num as nu
import numpy as np
import time
import re
pattern = re.compile('"(.*)"')



dataset = list(reader(open('/Users/apple/PycharmProjects/Apriori/python3-fp-growth-master/test')))
print(dataset)


# 数据集
'''
dataset = [
    ['啤酒', '牛奶', '可乐'],
    ['尿不湿', '啤酒', '牛奶', '橙汁'],
    ['啤酒', '尿不湿'],
    ['啤酒', '可乐', '尿不湿'],
    ['啤酒', '牛奶', '可乐'],
    ['尿不湿', '啤酒', '可乐', '橙汁'],
    ['啤酒', '可乐', '牛奶'],
    ['尿不湿', '苹果', '牛奶', '橙汁'],
    ['啤酒', '苹果'],
    ['啤酒', '薯片', '牛奶'],
    ['啤酒', '牛肉', '火腿']
]
'''

if __name__ == '__main__':

    '''
    调用find_frequent_itemsets()生成频繁项
    @:param minimum_support表示设置的最小支持度，即若支持度大于等于minimum_support，保存此频繁项，否则删除
    @:param include_support表示返回结果是否包含支持度，若include_support=True，返回结果中包含itemset和support，否则只返回itemset
    '''
    #print(nu.get_num(1,'/Users/apple/PycharmProjects/Apriori/python3-fp-growth-master/dataset/3-25.csv'))
    #print(nu.get_num(0,'/Users/apple/PycharmProjects/Apriori/python3-fp-growth-master/dataset/3-22.csv'))
    time1 = time.time()
    frequent_itemsets = fpg.find_frequent_itemsets(dataset, minimum_support=50,include_support=True)
    #print(frequent_itemsets)   # print type
    #result = []


    f = open('频繁项集.csv', 'w', encoding='utf-8')
    csv_writer = csv.writer(f)
    i = 0
    for itemset, support in frequent_itemsets:
        i = i + 1
        item = list(map(int, itemset))
        num = csv_writer.writerow([i, item, support]) # 将generator结果存入list
        #print(len(num.readlines()))
        #result.append((itemset, support))
    time2 = time.time()
    print(time2 - time1)




