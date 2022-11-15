
import json

def readDB():
    database_list = []

    with open("./db.json", encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
        for i in dados:
            database_list.append(i['name'])
    return database_list

def readQuery():
    dbQuery = []
    with open("./dbQuery.json", encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
        for i in dados:
            dbQuery.append(i['name']) 
    return dbQuery