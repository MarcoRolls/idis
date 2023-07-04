from nav import *
from db import collection, collection_contracts, collection_partners
from flask import request, redirect, json, render_template
from functions import employee_functions


############################## <!----! Пользователи  !----!>

@app.route('/user/<user_id>')
def user(user_id):
    # Поиск пользователя по object _id
    user = collection.find_one({'_id': ObjectId(user_id)})

    if user:
        return render_template('employee.html', user=user)
    else:
        return 'Пользователь не найден'


@app.route('/user/<user_id>/remove', methods=['POST'])
def remove_employee(user_id):
    # Преобразуем строковый user_id в ObjectId
    employee_id = ObjectId(user_id)
    # Удаляем пользователя
    collection.delete_one({'_id': employee_id})
    users = collection.find()
    return render_template('employees.html', users=users)


@app.route('/add_employee', methods=['POST'])
def add_employee():
    data = request.form  # Получение данных из POST-запроса
    # Кидаем в базу
    collection.insert_one(employee_functions.add_employee(data)).inserted_id
    users = collection.find()
    return render_template('employees.html', users=users)


@app.route('/user/<user_id>/edit', methods=['POST'])
def edit_user_save(user_id):

    name = request.form['name']
    surname = request.form['surname']
    telephone = request.form['telephone']
    mail = request.form['mail']

    # Получение данных о новых документах
    new_documents = request.form.getlist('new_documents')
    # Декодирование JSON и обработка каждого документа
    decoded_documents = []
    for document_str in new_documents:
        document_data = json.loads(document_str)
        for document in document_data:
            decoded_documents.append(document)

    # Получение данных о существующих документах
    existing_documents = request.form.getlist('existing_documents')
    for existing_documents_str in existing_documents:
        document_data = json.loads(existing_documents_str)
        for document in document_data:
            decoded_documents.append(document)

    # Обновляем пользователя
    collection.update_one(
        {'_id': ObjectId(user_id)},
        {'$set': {
            'name': name,
            'surname': surname,
            'telephone': telephone,
            'mail': mail,
            'documents': decoded_documents
        }}
    )

    return redirect('/user/' + user_id)


############################## <!----! Договора  !----!>

@app.route('/contract/<contract_id>')
def contract(contract_id):
    contract = collection_contracts.find_one({'_id': ObjectId(contract_id)})

    if contract:
        return render_template('contract.html', contract=contract)
    else:
        return 'Договор не найден'


@app.route('/add_contract', methods=['POST'])
def add_contract():
    data = request.form  # Получение данных из POST-запроса

    contractNumber = data.get('contractNumber')
    date = data.get('date')
    amount = data.get('amount')
    customer = data.get('customer')
    workType = data.get('workType')
    workTypeName = data.get('workTypeName')

    # Создание объекта сотрудника
    contract = {
        "contractNumber": contractNumber,
        "date": date,
        "amount": amount,
        "customer": customer,
        "workType": workType,
        "workTypeName": workTypeName
    }

    collection_contracts.insert_one(contract).inserted_id
    contracts = collection_contracts.find()

    return render_template('contracts.html', contracts=contracts)


@app.route('/contract/<contract_id>/remove', methods=['POST'])
def remove_contract(contract_id):
    # Преобразуем строковый user_id в ObjectId
    contract_id = ObjectId(contract_id)
    # Удаляем пользователя
    collection_contracts.delete_one({'_id': contract_id})

    contracts = collection_contracts.find()
    return render_template('contracts.html', contracts=contracts)


@app.route('/contract/<contract_id>/edit', methods=['POST'])
def edit_contract_save(contract_id):

    contractNumber = request.form['contractNumber']
    date = request.form['date']
    amount = request.form['amount']
    customer = request.form['customer']
    workType = request.form['workType']
    workTypeName = request.form['workTypeName']


    # Обновляем пользователя
    collection_contracts.update_one(
        {'_id': ObjectId(contract_id)},
        {'$set': {
            'contractNumber': contractNumber,
            'date': date,
            'amount': amount,
            'customer': customer,
            'workType': workType,
            'workTypeName': workTypeName
        }}
    )

    return redirect('/contract/' + contract_id)


############################## <!----! Партнёры  !----!>

@app.route('/partner/<partner_id>')
def partner(partner_id):
    partner = collection_partners.find_one({'_id': ObjectId(partner_id)})

    if partner:
        return render_template('partner.html', partner=partner)
    else:
        return 'Договор не найден'


@app.route('/add_partner', methods=['POST'])
def add_partner():
    data = request.form  # Получение данных из POST-запроса

    company = data.get('company')
    name = data.get('name')
    surname = data.get('surname')
    telephone = data.get('telephone')


    # Создание объекта сотрудника
    partner = {
        "company": company,
        'name': name,
        "surname": surname,
        "telephone": telephone,
    }

    collection_partners.insert_one(partner).inserted_id
    partners = collection_partners.find()

    return render_template('partners.html', partners=partners)


@app.route('/partner/<partner_id>/remove', methods=['POST'])
def remove_partner(partner_id):
    partner_id = ObjectId(partner_id)
    collection_partners.delete_one({'_id': partner_id})

    partners = collection_partners.find()
    return render_template('partners.html', partners=partners)


@app.route('/partner/<partner_id>/edit', methods=['POST'])
def edit_partner_save(partner_id):

    company = request.form['company']
    surname = request.form['surname']
    name = request.form['name']
    telephone = request.form['telephone']


    collection_partners.update_one(
        {'_id': ObjectId(partner_id)},
        {'$set': {
            'company': company,
            'surname': surname,
            'name': name,
            'telephone': telephone,
        }}
    )

    return redirect('/partner/' + partner_id)


