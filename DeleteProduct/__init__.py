import logging

import azure.functions as func
from ..Utils.ReqManager import ReqManager
from ..Utils.DbManager import DbManager
from ..Utils.ExceptionWithStatusCode import ExceptionWithStatusCode


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        reqManager = ReqManager()
        id = reqManager.getProductId(req)
        dbManager = DbManager()
        dbManager.deleteProduct(id)
        return func.HttpResponse("Deleted", status_code=200)
    except ExceptionWithStatusCode as e:
        return func.HttpResponse(str(e), status_code=e.status_code)
    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
