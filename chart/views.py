# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from ChartDjango.settings import CSV_PATH
import os, re

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

    # 判断是OHLC或是Line
    if 'highp' and 'lowp' in df.columns.tolist():
        df_json = df.to_json(orient="values")
        return render(request, 'csv_OHLC.html', {'df_json': df_json, 'file_name_no_postfix':file_name_no_postfix, 'file_list': get_file_list()})

    elif 'dates' and 'closep' in df.columns.tolist():
        df_json = df.to_json(orient="values")
        return render(request, 'csv_line.html', {'df_json': df_json, 'file_name_no_postfix':file_name_no_postfix, 'file_list': get_file_list()})

    else:
        return HttpResponse("Wrong Data")
