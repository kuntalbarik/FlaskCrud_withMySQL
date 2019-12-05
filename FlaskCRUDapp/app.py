from flask import Flask,render_template,url_for,request,redirect,flash
import MySqlConnect
import os,json

path="CONFIG/DB_Connection.json"
absfilepath = os.path.abspath(__file__)
fileDir = os.path.dirname(absfilepath)
filename = os.path.join(fileDir, path)
filename = os.path.abspath(os.path.realpath(filename))
readJson = open(filename, "r")
data = json.load(readJson)

mysqlConnect=MySqlConnect.MySqlConnector()

app=Flask(__name__)
app.secret_key="flash message"

@app.route("/")
@app.route("/home")
def Home():
    dbconnectionObj=mysqlConnect.ConnectDB(data["host"],data["user"],data["password"],data["database"])
    if dbconnectionObj!=False:
        sqlQuery="SELECT * FROM flask_crud_students.student_details"
        students=mysqlConnect.SelectData(dbconnectionObj,sqlQuery)
        return render_template('index.html',students=students)

@app.route("/insert",methods=["POST"])
def insert():
    ###connecting to mysql db, password, username are getting from config file
    dbconnectionObj=mysqlConnect.ConnectDB(data["host"],data["user"],data["password"],data["database"])
    if dbconnectionObj!=False:
        name = request.form['name']
        emailId = request.form['emailId']
        mobileNo = request.form['mobileNo']
        ####creating insert query
        sqlQuery = "insert into flask_crud_students.student_details (name,email_id,mobile_no) values (%s,%s,%s)"
        values = (name, emailId, mobileNo)
        mysqlConnect.DMF(dbconnectionObj,'insert',sqlQuery,values)
        flash("Data inserted successfully!")
        dbconnectionObj = mysqlConnect.ConnectDB(data["host"], data["user"], data["password"], data["database"])
        if dbconnectionObj != False:
            sqlQuery = "SELECT * FROM flask_crud_students.student_details"
            students = mysqlConnect.SelectData(dbconnectionObj, sqlQuery)
            return render_template('index.html', students=students)

@app.errorhandler(404)
def NotFound(error):
    return render_template("routing/404.html"),404

if __name__=="__main__":
    app.run(debug=True)
