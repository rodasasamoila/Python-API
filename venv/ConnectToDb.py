import psycopg2

try:
        connection = psycopg2.connect(user="postgres",  # used pgadmin, I will leave the table collumns in the readme
                                      password="!",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="Test")
        cursor = connection.cursor()
except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)


def get_All():
    get_all_entries = 'SELECT * FROM "TestTable"'
    cursor.execute(get_all_entries)
    return  cursor.fetchall()

def insert_In_Db(data_to_insert):
    add_to_table_query = 'INSERT INTO "TestTable" ("Id","Name")VALUES (5,\'test\')'
    cursor.execute(add_to_table_query)
    connection.commit()

def update_In_Db(id_to_update):
    update_row_in_db= 'UPDATE "TestTable" SET "Status"= WHERE Id = ' + str(id_to_update)
    cursor.execute(update_row_in_db)
    connection.commit()

def delete_In_Db(id_to_delete):
    delete_row_in_db= 'DELETE FROM "TestTable" WHERE "Id" =' + str(id_to_delete)
    cursor.execute(delete_row_in_db)
    connection.commit()



