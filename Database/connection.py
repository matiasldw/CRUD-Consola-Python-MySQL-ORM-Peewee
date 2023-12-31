from peewee import MySQLDatabase
from dotenv import load_dotenv
import os

load_dotenv()


class Data:
    def __init__(self):
        self.user = os.getenv('DB_USERNAME')
        self.host = os.getenv('DB_HOST')
        self.passw = os.getenv('DB_PASSWORD')
        self.db = os.getenv('DB_DATABASE')
        try:
            self.db_connection = MySQLDatabase(self.db, user=self.user, password=self.passw)
            self.db_connection.connect()
        except:
            print('Error de conexion....')

    #
    # def getClientes(self):
    #     if self.db_connection.is_connected():
    #         try:
    #             with self.db_connection.cursor() as cursor:
    #                 # cursor.execute('SELECT * FROM clientes')
    #                 cursor.callproc('SP_Listar')
    #                 result = cursor.stored_results()
    #                 return next(result).fetchall()
    #         except Error as ex:
    #             print(f'Error al intentar la conexion... ({ex})')
    #
    # def createClient(self, client: tuple):
    #     if self.db_connection.is_connected():
    #         try:
    #             with self.db_connection.cursor() as cursor:
    #                 cursor.callproc('SP_Guardar', client)
    #                 self.db_connection.commit()
    #                 print('¡¡¡ Cliente Registrado Ok !!!')
    #         except Error as ex:
    #             print(f'Error al intentar la conexion... ({ex})')
    #
    # def updateClient(self, client: list):
    #     if self.db_connection.is_connected():
    #         try:
    #             with self.db_connection.cursor() as cursor:
    #                 cursor.callproc('SP_Editar', client)
    #                 self.db_connection.commit()
    #                 print('¡¡¡ Cliente Actualizado Ok !!!')
    #         except Error as ex:
    #             print(f'Error al intentar la conexion... ({ex})')
    #
    # def deleteClient(self, id_Cliente: int):
    #     if self.db_connection.is_connected():
    #         try:
    #             with self.db_connection.cursor() as cursor:
    #                 cursor.callproc('SP_Eliminar', (id_Cliente,))
    #                 self.db_connection.commit()
    #                 print('¡¡¡ Cliente Borrado Ok !!!')
    #         except Error as ex:
    #             print(f'Error al intentar la conexion... ({ex})')
