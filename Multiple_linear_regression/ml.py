# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn import linear_model
from pymongo import MongoClient
import json
import math
import sys

def main():
    con = MongoClient('localhost', 27017)
    db = con["mydb"]
    col = db.ml
    # mongodbからデータを取得してくる
    data = pd.DataFrame(list(col.find()))
    # idを削除
    del data['_id']
    ### 検証用
    # print(data)
    # data = pd.read_csv("data.csv", sep=",")
    # pre_data = pd.read_csv("pre_data.csv", sep=",")
    pre_data = pd.read_json(sys.argv[1], orient='records', lines=True)
    clf = linear_model.LinearRegression()
    # 説明変数に "x1"のデータを使用
    X = data.loc[:, ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8']].values
    ### 検証用
    # print("X:\n", X)
    pre_X = pre_data.loc[:, ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8']].values
    # 目的変数に "x2"のデータを使用
    Y = data['x9'].values
    # 予測モデルを作成(重回帰)
    clf.fit(X, Y)
    # 回帰係数と切片の抽出
    a = clf.coef_
    b = clf.intercept_
    # 回帰係数
    ### 検証用
    # print("回帰係数:", a)
    # print("切片:", b)
    # print("決定係数:", clf.score(X, Y))
    # print("予測値:", clf.predict(pre_X))
    # print("パラメータ:", clf.get_params())
    predict = clf.predict(pre_X)[0]
    # predict = 500
    # predict = round(predict,0)
    predict = math.floor(predict)
    # 0~360にする
    if 360 <= predict:
        predict = 360
    elif predict <= 0:
        predict = 0
    print(predict)
    # dump_data_json = json.dumps(sys.argv[1])
    # pre_data_json = json.loads(dump_data_json)
    # print(sys.argv[1])
    # print(dump_data_json)
    # print(pre_data_json['x1']
    # print(sys.argv[1])
    # json_data = json.loads(sys.argv[1])
    # print(json_data)
    # print(json_data['x1'])
    #
    # dump_data_json = json.dumps(sys.argv[1])
    # # print(dump_data_json)
    # pre_data_json = json.loads(dump_data_json)
    # # print(pre_data_json)
    # pdj = pd.read_json(sys.argv[1], orient='records', lines=True)
    # # pdj = pd.DataFrame(sys.argv[1])
    # print(pdj)
    # pdj2 = pdj.loc[:, ['x1', 'x2']].values
    # print(pdj2)

    con.close()

if __name__ == "__main__":
    main()
