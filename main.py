from class_DBConnect import DBConnect


def main():
    print("\nBenvenuto nella gestione degli account")
    dbConnect = DBConnect()
    while 1:
        IndexOp = int(input(
            "\n=============\nSelect Operation,\n1-add account\n2-list "
            "account\n3-delete account "
            "by ID\n4-update account\n0- exit\n=============\nChoice: "))
        if IndexOp == 0:
            break;
        elif IndexOp == 1:
            Username = input("Enter Username: ")
            NumericPassword = int(input("Enter numeric password: "))
            dbConnect.Add(Username, NumericPassword)
        elif IndexOp == 2:
            dbConnect.ListAdmins()
        elif IndexOp == 3:
            ID = input("ID to delete: ")
            dbConnect.DeleteRecord(ID)
        elif IndexOp == 4:
            ID = input("Enter ID: ")
            NumericPassword = int(input("Enter numeric Password: "))
            dbConnect.UpdateRecord(ID, NumericPassword)


if __name__ == '__main__': main()
