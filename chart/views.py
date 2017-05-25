# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from ChartDjango.settings import CSV_PATH
import os, re, json

# 获取csv文件夹内去除后缀的csv文件名
def get_file_list():
    f_list = os.listdir(CSV_PATH)
    f_list_no_postfix = []
    for f_item in f_list:
        if os.path.splitext(f_item)[1].lower() == '.csv':
            f_list_no_postfix.append(os.path.splitext(f_item)[0])

    return f_list_no_postfix


# 根据URL判断所访问的csv文件名
def get_file_name(request):
    request_url = request.path
    rex = re.compile(r'[\w]*.[\w]*$')
    return rex.findall(request_url)[0]

    # return request_url


# 将get_file_name得到文件名除去后缀
def get_file_name_no_postfix(file_name):
    rex = re.compile(r'[\w]*')
    return rex.findall(file_name)[0]


# 首页
def index(request):
    return render(request, 'index.html', {'file_list': get_file_list()})


# CSV展示页
def show_csv_item(request):
    file_name = get_file_name(request)
    file_name_no_postfix = get_file_name_no_postfix(file_name)

    if file_name:
        try:
            df = pd.read_csv(CSV_PATH + file_name)
        except IOError:
            return HttpResponse("The File does not exist!")
    else:
        return HttpResponse("Please select a File!")


    try:
        dates =  df['dates']
        dates_json = dates.to_json(orient="values")
        values = df.drop('dates', axis=1)
        values_header = list(values)
    except:
        return HttpResponse("Wrong CSV Header!")


    # key_list && datas of panel, 供header分类使用
    p0_key = []
    p1_key = []
    p2_key = []

    p0_y1_key = []
    p1_y1_key = []
    p2_y1_key = []

    p0_json = {}
    p1_json = {}
    p2_json = {}

    p0_y1_json = {}
    p1_y1_json = {}
    p2_y1_json = {}

    # 判断panel数量, key分类 (筛选器)
    for header in values_header:
        p1 = re.search(r'p1', header)
        p2 = re.search(r'p2', header)
        if p1:
            p1_y1 = re.search(r'y1', p1.string)
            if p1_y1:
                p1_y1_key.append(p1_y1.string)
            else:
                p1_key.append(p1.string)

        elif p2:
            p2_y1 = re.search(r'y1', p2.string)
            if p2_y1:
                p2_y1_key.append(p2_y1.string)
            else:
                p2_key.append(p2.string)

        else:
            p0_y1 = re.search(r'y1', header)
            if p0_y1:
                p0_y1_key.append(p0_y1.string)
            else:
                p0_key.append(header)

    # 若有p1 and p2
    if p1_key and p2_key:
        # 若有p0_y1
        if p0_y1_key:
            for header in p0_y1_key:
                p0_y1_json[header] = values[header].to_json(orient="values")

        # 若有p1_y1
        if p1_y1_key:
            for header in p1_y1_key:
                p1_y1_json[header] = values[header].to_json(orient="values")

        # 若有p2_y1
        if p2_y1_key:
            for header in p2_y1_key:
                p2_y1_json[header] = values[header].to_json(orient="values")

        # 若为candle
        if 'openp' and 'closep' and 'highp' and 'lowp' in p0_key:
            # 统一抽出 OCLH (根据echarts排列)
            ohlc = df[['openp', 'closep', 'lowp', 'highp']]
            ohlc_json = ohlc.to_json(orient="values")
            p0_key.remove('openp')
            p0_key.remove('closep')
            p0_key.remove('highp')
            p0_key.remove('lowp')
        else:
            # 若没有ohlc,给空json
            ohlc_json = json.dumps('')

        for header in p2_key:
            p2_json[header] = values[header].to_json(orient="values")

        for header in p1_key:
            p1_json[header] = values[header].to_json(orient="values")

        for header in p0_key:
            p0_json[header] = values[header].to_json(orient="values")

        return render(request, 'three_panels.html', {'dates_json': dates_json, 'ohlc_json': ohlc_json,
                                                   'p0_json': json.dumps(p0_json),
                                                   'p0_y1_json': json.dumps(p0_y1_json),
                                                   'p1_json': json.dumps(p1_json),
                                                   'p1_y1_json': json.dumps(p1_y1_json),
                                                   'p2_json': json.dumps(p2_json),
                                                   'p2_y1_json': json.dumps(p2_y1_json),
                                                   'file_name_no_postfix': file_name_no_postfix,
                                                   'file_list': get_file_list()})


    # 有p1, 2panels
    elif p1_key:
        # 若有p0_y1
        if p0_y1_key:
            for header in p0_y1_key:
                p0_y1_json[header] = values[header].to_json(orient="values")

        # 若有p1_y1
        if p1_y1_key:
            for header in p1_y1_key:
                p1_y1_json[header] = values[header].to_json(orient="values")

        # 若为candle
        if 'openp' and 'closep' and 'highp' and 'lowp' in p0_key:
            # 统一抽出 OCLH (根据echarts排列)
            ohlc = df[['openp', 'closep', 'lowp', 'highp']]
            ohlc_json = ohlc.to_json(orient="values")
            p0_key.remove('openp')
            p0_key.remove('closep')
            p0_key.remove('highp')
            p0_key.remove('lowp')
        else:
            # 若没有ohlc,给空json
            ohlc_json = json.dumps('')

        for header in p1_key:
            p1_json[header] = values[header].to_json(orient="values")

        for header in p0_key:
            p0_json[header] = values[header].to_json(orient="values")

        return render(request, 'two_panels.html', {'dates_json': dates_json, 'ohlc_json': ohlc_json,
                                                     'p0_json': json.dumps(p0_json),
                                                     'p0_y1_json': json.dumps(p0_y1_json),
                                                     'p1_json': json.dumps(p1_json),
                                                     'p1_y1_json': json.dumps(p1_y1_json),
                                                     'file_name_no_postfix': file_name_no_postfix,
                                                     'file_list': get_file_list()})

    # 仅有p0,单panel图
    elif p0_key:

        # 若有p0_y1
        if p0_y1_key:
            for header in p0_y1_key:
                p0_y1_json[header] = values[header].to_json(orient="values")

        # 若为candle
        if 'openp' and 'closep' and 'highp' and 'lowp' in p0_key:
            # 统一抽出 OCLH (根据echarts排列)
            ohlc = df[['openp', 'closep', 'lowp', 'highp']]
            ohlc_json = ohlc.to_json(orient="values")
            p0_key.remove('openp')
            p0_key.remove('closep')
            p0_key.remove('highp')
            p0_key.remove('lowp')

        else:
            # 若没有ohlc,给空json
            ohlc_json = json.dumps('')

        # 除OHLC的p0_key
        for header in p0_key:
            p0_json[header] = values[header].to_json(orient="values")

        return render(request, 'single_panel.html', {'dates_json': dates_json, 'ohlc_json': ohlc_json,
                                                     'p0_json': json.dumps(p0_json),
                                                     'p0_y1_json': json.dumps(p0_y1_json),
                                                     'file_name_no_postfix': file_name_no_postfix,
                                                     'file_list': get_file_list()})

