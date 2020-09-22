import sqlite3


class DBConnect:

    def __init__(self):
        self._db = sqlite3.connect(
            "Account_database.db")  # extension for sqlite database
        self._db.row_factory = sqlite3.Row
        self._db.execute("create table if not exists Admin(ID integer primary "
                         "key autoincrement, Username text,NumericPassword int)")
        self._db.commit()

    def Add(self, Username, NumericPassword):
        self._db.execute("insert into Admin(Username, NumericPassword) values (?,?)""",
                         (Username, NumericPassword))
        self._db.commit()
        print("Record is added")

    def ListAdmins(self):
        cursor = self._db.execute("select * from Admin")
        for row in cursor:
            print("ID {}: , Username: {}, Password: {}".format(row["ID"], row["Username"],
                                                      row["NumericPassword"]))

    def DeleteRecord(self, ID):
        self._db.execute("delete from admin where ID='{}'".format(ID))
        self._db.commit()
        print("Record is deleted")

    def UpdateRecord(self, ID, NumericPassword):
        self._db.execute("update  Admin set NumericPassword=? where ID=?", (NumericPassword, ID))
        self._db.commit()
        print("Record is added")
