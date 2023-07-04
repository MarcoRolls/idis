import json
from urllib import request


def add_employee(data):

    # Извлечение данных о сотруднике
    surname = data.get('surname')
    name = data.get('name')
    telephone = data.get('telephone')
    mail = data.get('mail')
    documents = []

    employeer = {
        "surname": surname,
        "name": name,
        "telephone": telephone,
        "mail": mail,
        "documents": documents
    }

    return employeer

