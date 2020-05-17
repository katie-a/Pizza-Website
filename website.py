from flask import Flask, redirect, url_for, render_template, request

app = Flask("__name__")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin")
def admin():
    return redirect(url_for("noentry"))

@app.route("/noentry")
def noentry():
    return render_template("noentry.html")


    
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        password = request.form["passw"]
        return redirect(url_for("user", usr=user, passwo=password))
    else:
        return render_template("login.html")
        
@app.route("/<usr><passwo>")
def user(usr, passwo):
    return "<h1>" + usr + passwo +  "</h1>"
    

    


if __name__ == "__main__":
    app.run(debug=True)
