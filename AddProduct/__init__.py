# import logging


import azure.functions as func
from ..Utils.ReqManager import ReqManager
from ..Utils.DbManager import DbManager
from ..Utils.ExceptionWithStatusCode import ExceptionWithStatusCode


def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        reqManager = ReqManager()
        product = reqManager.getProduct(req)
        dbManager = DbManager()
        dbManager.addProduct(product)
        return func.HttpResponse("Created", status_code=201)
    except ExceptionWithStatusCode as e:
        return func.HttpResponse(str(e), status_code=e.status_code)
    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
