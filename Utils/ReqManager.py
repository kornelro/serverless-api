from ..Model.Product import Product
import azure.functions as func
from .ExceptionWithStatusCode import ExceptionWithStatusCode


class ReqManager():

    def getProduct(self, req: func.HttpRequest) -> Product:
        req_body = req.form

        # get id
        try:
            id = req_body['id']
        except KeyError:
            id = None

        # get name
        try:
            name = req_body['name']
        except KeyError:
            raise ExceptionWithStatusCode(
                'Value name is required.',
                status_code=400
            )
        if len(name) == 0:
            raise ExceptionWithStatusCode(
                'Value name cannot be empty.',
                status_code=400
            )

        # get description
        try:
            description = req_body['description']
        except KeyError:
            description = ""

        # get quantity
        try:
            quantity = int(req_body['quantity'])
        except KeyError:
            raise ExceptionWithStatusCode(
                'Value quantity is required.',
                status_code=400
            )
        except ValueError:
            raise ExceptionWithStatusCode(
                'Value quantity must be integer.',
                status_code=400
            )
        if quantity < 0:
            raise ExceptionWithStatusCode(
                'Value quantity cannot be lower than zero.',
                status_code=400
            )

        # get price
        try:
            price = float(req_body['price'])
        except KeyError:
            raise ExceptionWithStatusCode(
                'Value price is required.',
                status_code=400
            )
        except ValueError:
            raise ExceptionWithStatusCode(
                'Value price must be float.',
                status_code=400
            )
        if price < 0:
            raise ExceptionWithStatusCode(
                'Value priced cannot lower than zero.',
                status_code=400
            )

        return Product(name, description, quantity, price, id)

    def getProductId(self, req: func.HttpRequest) -> int:
        id = req.params.get('id')
        if not id:
            raise ExceptionWithStatusCode('Param id is required.', 400)
        else:
            try:
                id = int(id)
            except ValueError:
                raise ExceptionWithStatusCode('Param id must be int.', 400)
        return id
