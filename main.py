from flask import Flask, request, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      
@app.route("/register", methods=['POST'])
def register():
    username = cgi.escape(request.form['username'])
    password = cgi.escape(request.form['password'])
    password2 = cgi.escape(request.form['password2'])
    email = cgi.escape(request.form['email'])

    usernameError =""
    passwordError = ""
    password2Error =""
    emailError=""

    if not username:
        print("no username")
        usernameError = "Username is required"
    if not password:
        passwordError = "Password is required"
    if not email :
        emailError = "email is required"
    if len(email)<=3 or len(email) >= 20:
        emailError = "email must be at  between 3 and 20 characters long"
    counter=0
    for char in email:
        if char==".":
            counter = counter+1
    if counter != 1:
        emailError = "email must include one '.'"
    counter=0
    for char in email:
        if char=="@":
            counter = counter+1
    if counter != 1:
        emailError = "email must include one '@'"
    else:
        hasSpace = False
        for char in email:
            if char==" ":
                emailError = "email can't contain spaces"
    if len(password) < 8:
        passwordError = "Password must be at least 8 characters long"
    elif len(password) > 20:
        passwordError = "Password must be shorter then 20 characters"
    else:
        hasSpace = False
        for char in password:
            if char==" ":
                passwordError = "Password can't contain spaces"
    if password  != password2:
        password2Error = "Password 2 must match password" 

    if usernameError or passwordError or password2Error or emailError:
        return render_template("form.html", username=username, usernameError=usernameError, password=password,passwordError=passwordError,
password2=password2,password2Error=password2Error,email=email,emailError=emailError)

    return render_template("welcome.html", username=username)


@app.route("/")
def index():
    return render_template("form.html", username="", usernameError="", password="",passwordError="",
password2="",password2Error="",email="",emailError="") 


@app.route("/register", methods=['GET'])
def register_page():
   return render_template("form.html", username="", usernameError="", password="",passwordError="",
password2="",password2Error="",email="",emailError="")

app.run()