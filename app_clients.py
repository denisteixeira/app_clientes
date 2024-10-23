from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector as sql
from app_clients_db import connect_to_db # to import connection function from app_clients_db.py

app=Flask(__name__)

@app.route("/")
@app.route("/index")

def index ():
    con = connect_to_db()
#    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("Select * from clientes")
    data=cur.fetchall()
    return render_template("index.html", datas=data)

@app.route("/add_client", methods=["POST", "GET"])
def add_user():
    if request.method=="POST":
        nome=request.form["nome"]
        email=request.form["email"]
        idade=request.form["idade"]
        cidade=request.form["cidade"]
        cpf=request.form["cpf"]
        con=sql.connect("db_users")
        cur=con.cursor()
        cur.execute("insert into clientes(NOME, EMAIL, IDADE, CIDADE, CPF) values (?,?,?,?,?,?)", (nome, email, idade, cidade, cpf))
        con.commit()
        flash("Dados cadastrados", "success")
        return redirect (url_for("index"))
    return render_template("add_user.html")

@app.route("/.edit_client/<string:id>", methods=["POST", "GET"])
def edit_user(id):
    if request.method=="POST":
        nome=request.form["nome"]
        email=request.form["email"]
        idade=request.form["idade"]
        cidade=request.form["cidade"]
        cpf=request.form["cpf"]
        con=sql.connect("db_users")
        cur=con.cursor()
        cur.execute("update clients set NOME=?, EMAIL=?, IDADE=?, CIDADE=?, CPF=? where ID=?", (nome, email, idade, ccidade, cpf,id))
        con.commit()
        flash("Dados atualizados", "success")
        return redirect(url_for("index"))
    con=sql.connect("db_users")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from users where ID =?", (id,))
    data=cur.fetchone()
    return render_template("edit_user.html", datas=data)

@app.route("/delete_client/<string:id>", methods=["GET"])
def delete_user(id):
    con=sql.connect("db_users")
    cur=con.cursor()
    cur.execute("delete from clients where ID=?", (id))
    con.commit()
    flash("Dados deletados", "warning")
    return redirect(url_for("index"))

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
    app.secret_key="admin123"
    app.run(debug=True)