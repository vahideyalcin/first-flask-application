from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators,EmailField
from passlib.hash import sha256_crypt

#Kullanıcı Kayıt Formu
class RegisterForm(Form):
    name = StringField("İsim Soyisim",validators=[validators.Length(min=4,max=25)])
    username = StringField("Kullanıcı Adı",validators=[validators.Length(min=5,max=35)])
    email = EmailField("Email Adresi",validators=[validators.Email(message="Lütfen Geçerli Bir Email Adresi Girin")])
    password = PasswordField("Parola:",validators=[
        validators.DataRequired(message = "Lütfen bir parola belirleyin"),
        validators.EqualTo(fieldname = "confirm",message="Parolanız Uyuşmuyor..")

    ])
    confirm = PasswordField("Parola Doğrula")


app=Flask(__name__,template_folder='template')
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "ybblog"
app.config["MYSQL_CURSORCLASS"]= "DictCursor"
mysql = MySQL(app)

@app.route("/")
def index():
  return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")

#Kayıt Olma
@app.route("/register")
def register():
  return render_template("register.html")



if __name__=="__main__":
    app.run(debug=True)