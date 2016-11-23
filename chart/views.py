from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from ChartDjango.settings import CSV_PATH
import os


def index(request):
    CSV_FILES = os.listdir(CSV_PATH)
    return render(request, 'csv_OHLC.html', {'csv_files': CSV_FILES})


def show_csv_item(request):
    CSV_FILES = os.listdir(CSV_PATH)

    csv_file_name = request.path[5:]

    if csv_file_name:
        try:
            df = pd.read_csv(CSV_PATH + csv_file_name)
        except IOError:
            return HttpResponse("The File does not exist!")
    else:
        return HttpResponse("Please select a File!")

    if 'highp' and 'lowp' in df.columns.tolist():
        df_json = df.to_json(orient="values")
        return render(request, 'csv_OHLC.html', {'df_json': df_json, 'csv_files': CSV_FILES})

    elif 'dates' and 'closep' in df.columns.tolist():
        df_json = df.to_json(orient="values")
        return render(request, 'csv_line.html', {'df_json': df_json, 'csv_files': CSV_FILES})

    else:
        return HttpResponse("Wrong Data")


# df_json = df.to_json(orient="values")
# return HttpResponse(df_json)
