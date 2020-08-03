import os
import pyodbc
from ..Model.Product import Product
from typing import List


SERVER = os.environ['SERVER']
DATABASE = os.environ['DATABASE']
USERNAME = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
DRIVER = os.environ['DRIVER']


class DbManager():
    def __init__(self):
        self.conn_string = 'DRIVER=' + DRIVER + \
            ';SERVER=' + SERVER + \
            ';PORT=1433;DATABASE=' + DATABASE + \
            ';UID='+USERNAME+';PWD='+PASSWORD

    def getProducts(self) -> List[Product]:
        with pyodbc.connect(self.conn_string) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Products")
                rows = cursor.fetchall()
        products = []
        for row in rows:
            products.append(self._rowToProduct(row))
        return products

    def getProduct(
        self,
        id: int
    ) -> Product:
        with pyodbc.connect(self.conn_string) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Products WHERE id=?", id)
                rows = cursor.fetchall()
        if len(rows) == 0:
            raise Exception(F'Product with id {id} not found!')
        return self._rowToProduct(rows[0])

    def _rowToProduct(self, row: List[str]):
        return Product(
            name=row[1],
            description=row[2],
            quantity=int(row[3]),
            price=float(row[4]),
            id=int(row[0])
        )

    def addProduct(
        self,
        product: Product
    ) -> None:
        with pyodbc.connect(self.conn_string) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO Products (name, description, quantity, price)
                    VALUES (?, ?, ?, ?)
                    """,
                    product.name, product.description,
                    product.quantity, product.price
                )

    def updateProduct(
        self,
        product: Product
    ) -> None:
        if not product.id:
            raise Exception('Cannot update product without id!')
        with pyodbc.connect(self.conn_string) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE Products SET name=?, description=?,
                    quantity=?, price=? WHERE id=?
                    """,
                    product.name, product.description,
                    product.quantity, product.price, product.id
                )

    def deleteProduct(
        self,
        id: int
    ) -> None:
        with pyodbc.connect(self.conn_string) as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM Products WHERE id=?", id)
