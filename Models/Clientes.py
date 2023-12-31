from peewee import Model, IntegerField, TextField
from Database.connection import Data


class Clientes(Model):
    id = IntegerField()
    nombre = TextField()
    apellido = TextField()
    direccion = TextField()
    telefono = IntegerField()

    class Meta:
        database = Data().db_connection
