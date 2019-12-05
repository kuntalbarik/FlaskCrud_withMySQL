####CRUD operations using Mysql+Flask
###C===Create(Create Database,Create Table,Insert)
###R===Read  (Select)
###U===Update(Update)
###D===Delete (Delete)

import mysql.connector
from mysql.connector import Error

class MySqlConnector:

    def ConnectDB(self,host:str,user:str,password:str,database:str):
        self.__host=host
        self.__user=user
        self.__password=password
        self.__database=database
        try:
            self.__mydb = mysql.connector.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database
            )
            if self.__mydb.is_connected():
                    return self.__mydb

        except Error as e:
            print("Not able to connect {} database or database does not exists\n".format(self.__dbName),e)
            return False


    def DMF(self,dbConnectionObj,operation:str,sqlQuery:str,values:tuple=None):
        try:
            self.__operation=operation.lower()
            if(self.__operation in ('insert','update','delete')):
                #self.__mysqlconnector = MySqlConnector()
                self.__sqlQuery = sqlQuery
                self.__values =values
                self.__dbConnection =dbConnectionObj
                #if self.__dbConnection != False:
                self.__mycursor = self.__dbConnection.cursor()
                self.__mycursor.execute(self.__sqlQuery, self.__values)
                self.__dbConnection.commit()
                self.__dbConnection.close()
                print("{} record(s) {}ed.".format(self.__mycursor.rowcount, self.__operation.lower()))
            else:
                print("No valid operation selected,Please select a valid operation among Insert,Update,Delete")
        except Error as e:
            print("No valid operation selected,Please select a valid operation among Insert,Update,Delete")

    def SelectData(self,dbConnectionObj,sqlQuery:str,values:tuple=None):
        self.__dbConnectionObj = dbConnectionObj
        self.__sqlQuery = sqlQuery
        self.__values = values
        if(self.__dbConnectionObj!=False):
            self.__mycursor = self.__dbConnectionObj.cursor()
            self.__mycursor.execute(self.__sqlQuery,self.__values)
            self.__myresult =self.__mycursor.fetchall()
            for x in self.__myresult:
                print("ID :-",x[0],end=" | ")
                print("Name :-", x[1],end=" | ")
                print("Email :-", x[2],end=" | ")
                print("Mobile :-", x[3],end="\n")
            self.__dbConnectionObj.close()
            return self.__myresult
        else:
            print("Not able to connect {} database or database does not exists".format(self.__dbName))
            self.__dbConnection.close()

