import requests
import ConnectToDb as db
import json

def get_table():
    data=db.get_All()
    return data

def insert(id_to_insert):
    db.insert_In_Db(id_to_insert)

def delete(id_to_delete):
    db.delete_In_Db(id_to_delete)

def convert_to_json(python_object):
    json_object=json.dumps(python_object)
    return json_object

def convert_from_json(json_object):
    python_object=json_object.loads(json_object)
    return python_object