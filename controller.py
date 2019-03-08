import db


def main():
    while (1):
        # chosing option to do CRUD operations
        selection = input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')

        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            print('delete')
            delete()
        else:
            print('\n INVALID SELECTION \n')


# Function to insert data into mongo db
def insert():
    employeeId = input('Enter Employee id :')
    employeeName = input('Enter Name :')
    employeeAge = input('Enter age :')
    employeeCountry = input('Enter Country :')

    document = {
        "id": employeeId,
        "name": employeeName,
        "age": employeeAge,
        "country": employeeCountry
    }

    print(db.insert(document))


# Function to update record to mongo db
def update():
    try:
        id = input('\nEnter old id to update\n')
        newid = input('\nEnter new id to update\n')
        name = input('\nEnter name to update\n')
        age = input('\nEnter age to update\n')
        country = input('\nEnter country to update\n')

        x = db.update(
            {"id": id},
            {
                "$set": {
                    "id": newid,
                    "name": name,
                    "age": age,
                    "country": country
                }
            }
        )
        print(x)

    except Exception as e:
        print(str(e))


# function to read records from mongo db
def read():
    try:
        x = db.read()
        print("\n All data from collection \n")
        for emp in x:
            print(emp)

    except Exception as e:
        print(str(e))


# Function to delete record from mongo db
def delete():
    try:
        id = input('\nEnter employee id to delete\n')
        x = db.delete({"id": id})
        print(x)
    except Exception as e:
        print(str(e))


main()
