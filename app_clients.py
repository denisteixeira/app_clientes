from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector as sql

app=Flask(__name__)

@app.route("/")
@app.route("/index")

def index ():
    con = sql.connect("db_users")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("Select * from clients")
    data=cur.fetchall()
    return render_template("index.html", datas=data)

@app.route("/add_user", methods=["POST", "GET"])
def add_user():
    if request.method=="POST":
        username=request.form["username"]
        email=request.form["email"]
        password=request.form["password"]
        create_time=request.form["create_time"]
        cpf=request.form["cpf"]
        con=sql.connect("db_users")
        cur=con.cursor()
        cur.execute("insert into clientes(USERNAME, EMAIL, PASSWORD, CREATE_TIME, CPF) values (?,?,?,?,?,?)", (username, email, password, create_time, cpf))
        con.commit()
        flash("Dados cadastrados", "success")
        return redirect (url_for("index"))
    return render_template("add_user.html")

@app.route("/.edit_user/<string:id>", methods=["POST", "GET"])
def edit_user(id)
    if request.method=="POST":
        username=request.form["username"]
        email=request.form["email"]
        password=request.form["password"]
        create_time=request.form["create_time"]
        cpf=request.form["cpf"]
        con=sql.connect("db_users")
        cur=con.cursor()
        cur.execute("update clients set USERNAME=?, EMAIL=?, PASSWORD=?, CREATE_TIME=?, CPF=? where ID=?", (username, email, password, create_time, cpf,id))
        con.commit()
        flash("Dados atualizados", "success")
        return redirect(url_for("index"))
    con=sql.connect("db_users")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from users where ID =?", (id,))
    data=cur.fetchone()
    return render_template("edit_user.html", datas=data)

@app.route("/delete_user/<string:id>", methods=["GET"])
def delete_user(id):
    con=sql.connect("db_users")
    cur=con.cursor()
    cur.execute("delete from clients where ID=?", (id))
    con.commit()
    flash("Dados deletados", "warning")
    return redirect(url_for("index"))

if __name__=='__main__':
    app.secret_key="admin123"
    app.run(debug=True)
