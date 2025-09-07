# to Do list
import sqlite3
connection=sqlite3.connect('to_do.db') # make a connection betwenn database abd python 
cursor=connection.cursor()# establish a cursor for connection it will execute the sql query
cursor.execute('''
    CREATE TABLE IF NOT EXISTS todo(
               todo_id INTEGER PRIMARY KEY AUTOINCREMENT,
               content TEXT NOT NULL,
               time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
               status BOOLEAN NOT NULL)
''')# created a table

def display_to_do():#display the table
    cursor.execute('''
    Select * from todo
''')
    for each in cursor.fetchall():
        print(each)

def insert_to_do(content , status):# insert the value inside the table
    cursor.execute('''
    INSERT INTO todo (content , status ) values(
                   ?,?)
''',(content,status))
    connection.commit()


def update_to_do( newStatus, id_todo):# updating value inside the table
    cursor.execute('''
    UPDATE todo set status=? where todo_id =?
''',(newStatus,id_todo))
    connection.commit()


def delete_to_do(id_todo):# delecting row from the table
    cursor.execute('''
    DELETE FROM todo where todo_id=?
                   ''',(id_todo,))
    connection.commit()

def main():
    while True:
        # user interface
        print('Press 1 for View of your To-Do List')
        print('Press 2 for Insert event into To-Do List')
        print('Press 3 for Update the To-Do List')
        print('Press 4 for Delete event from To-Do List')
        print('Press 5 for Exit the application')
        print('')

        choise=input("Choose an operation for your To-Do list : ")# intput from user for opr choise
        match choise:
            case '1':
                display_to_do()
            case '2':
                content=input('Entre your Todo thing')
                status=input('Entre the status of your todo 1 OR 0')
                status=True if status=='1' else False
                insert_to_do(content,status)
            case '3':
                status=input('Entre the status of your todo 1 OR 0')
                status=True if status=='1' else False
                id_todo=int(input('Enter the To-Do ID'))
                update_to_do(status,id_todo)
            case '4':
                id_todo=int(input('Enter the To-Do ID to be deleted'))
                delete_to_do(id_todo)
            case '5':
                break

if __name__ == '__main__': # main function call
    main()