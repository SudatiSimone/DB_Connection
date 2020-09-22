from class_DBConnect import DBConnect
def main():
    print("Benvenuto")
    dbConnect = DBConnect()
    while 1:
        IndexOp = int(input(
            "\n\n=========Select Operation,\n1-add:\n2-list Admins:\n3-delete by name:\n4-update\n0- exit:\n===============\n\n"))
        if (IndexOp == 0):
            break;
        elif (IndexOp == 1):
            Name = input("Enter name: ")
            Age = int(input("Enter age: "))
            dbConnect.Add(Name, Age)
        elif (IndexOp == 2):
            dbConnect.ListAdmins()
        elif (IndexOp == 3):
            ID = input("ID to delete: ")
            dbConnect.DeleteRecord(ID)
        elif (IndexOp == 4):
            ID = input("Enter ID: ")
            Age = int(input("Enter age: "))
            dbConnect.UpdateRecord(ID, Age)


if __name__ == '__main__': main()
