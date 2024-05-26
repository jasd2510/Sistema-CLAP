import sqlite3
from flet import *
import pathlib

rutaactual = pathlib.Path(__file__).parent.absolute()

datoUser = []

dbname = rutaBD = f"{rutaactual}\dbclap.db"
#dbname = "dbclap.db"
#dbname = "SistemaClapFlet\dbclap.db"
conexion = sqlite3.connect(dbname, check_same_thread=False)

def consulta(query, parametros=()):
    query = query
    parametros = parametros

    cursor = conexion.cursor()
    cursor.execute(query, parametros)
    resultado = cursor.fetchall()

    cursor.close()
    conexion.commit()

    return resultado

def enrutamiento(pages, ruta):
    pages = pages
    ruta = ruta
    
    pages.go(ruta)

def validarNumeros(campo, pagee):
    campo = campo
    pagee = pagee

    digitos = campo.value

    if digitos.isdigit():
        pass
    else:
        for i in digitos:
            if i not in "0123456789":
                digitos = digitos.replace(i, "", 1)

        campo.value = digitos
        pagee.update()

def validarAlfanumeros(campo, pagee):
    campo = campo
    pagee = pagee

    digitos = campo.value

    if digitos.isdigit():
        pass
    else:
        for i in digitos:
            if i not in "0123456789 qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNMÑ":
                digitos = digitos.replace(i, "", 1)

        campo.value = digitos
        pagee.update()

def validarNombres(campo, pagee):
    campo = campo
    pagee = pagee

    digitos = campo.value

    if digitos.isalpha():
        pass
    else:
        for i in digitos:
            if i not in "qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNMÑ,":
                digitos = digitos.replace(i, "", 1)

        campo.value = digitos
        pagee.update()

def validarCorreo(campo, pagee):
    campo = campo
    pagee = pagee

    digitos = campo.value

    if digitos.isspace():
        for i in digitos:
            if i in " @!#$%^&*()_-=+][}{\|';:<>/?`~":
                digitos = digitos.replace(i, "", 1)

                campo.value = digitos
                pagee.update()
    else:
        for i in digitos:
            if i in " @!#$%^&*()_-=+][}{\|';:<>/?`~":
                digitos = digitos.replace(i, "", 1)

                campo.value = digitos
                pagee.update()

def validarEspacio(campo, pagee):
    campo = campo
    pagee = pagee

    digitos = campo.value

    if digitos.isspace():
        for i in digitos:
            if i in " ":
                digitos = digitos.replace(i, "", 1)

                campo.value = digitos
                pagee.update()
    else:
        for i in digitos:
            if i in " ":
                digitos = digitos.replace(i, "", 1)

                campo.value = digitos
                pagee.update()

def capturar(dato, fecha):
    dato = dato
    fecha = fecha

    respuesta = consulta("SELECT lideres.id, lideres.nombre, lideres.apellido, lideres.ubicacion, usuarios.id FROM usuarios JOIN lideres ON lideres_id = lideres.id WHERE usuarios.usuario = ?", [dato])
    
    for ids, nom, ape, ubi, userId in respuesta:
        

        datoUser.append([ids, nom, ape, ubi, userId, fecha])
    
    