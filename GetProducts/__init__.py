import datetime
import logging
import os
import pyodbc

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:

    server = os.environ['SERVER']
    database = os.environ['DATABASE']
    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']
    driver = os.environ['DRIVER']

    try:
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT TOP 20 * FROM Products")
                rows = cursor.fetchall()
        return func.HttpResponse(str(rows))
    except Exception as e:
        return func.HttpResponse(str(e))
