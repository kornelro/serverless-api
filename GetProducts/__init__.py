# import logging
import json

import azure.functions as func
from ..Utils.DbManager import DbManager
from ..Utils.ExceptionWithStatusCode import ExceptionWithStatusCode


def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        dbManager = DbManager()
        products = dbManager.getProducts()
        products = list(map(lambda product: product.getDict(), products))
        return func.HttpResponse(json.dumps(products))
    except ExceptionWithStatusCode as e:
        return func.HttpResponse(str(e), status_code=e.status_code)
    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
