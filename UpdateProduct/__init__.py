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
        dbManager.updateProduct(product)
        return func.HttpResponse("Updated", status_code=200)
    except ExceptionWithStatusCode as e:
        return func.HttpResponse(str(e), status_code=e.status_code)
    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
