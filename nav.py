from bson import ObjectId
from flask import Flask
from flask import render_template
from db import collection, collection_contracts, collection_partners

app = Flask(__name__)


@app.route('/')
def index():
    # Получение данных из базы данных
    users = collection.find()

    # Передача данных в шаблон для отображения
    return render_template('employees.html', users=users)

# Страница "Сотрудники"
@app.route('/employees')
def employees():
    users = collection.find()

    # Передача данных в шаблон для отображения
    return render_template('employees.html', users=users)


# Страница "Договора"
@app.route('/contracts')
def contracts():
    contracts = collection_contracts.find()

    return render_template('contracts.html', contracts=contracts)


# Страница "Партнёры"
@app.route('/partners')
def partners():
    partners = collection_partners.find()

    return render_template('partners.html', partners=partners)


# Страница "Торги"
@app.route('/trading')
def trading():
    # Дополнительная логика для страницы "Торги"
    # ...

    return render_template('trading.html')


# Страница "Данные на изменения"
@app.route('/data_for_changes')
def data_for_changes():
    # Дополнительная логика для страницы "Данные на изменения"
    # ...

    return render_template('data_for_changes.html')
