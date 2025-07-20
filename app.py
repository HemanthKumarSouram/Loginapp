from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "admin":
            return redirect("/order")
        else:
            return "Invalid credentials"
    return render_template("login.html")

@app.route("/order", methods=["GET", "POST"])
def order():
    if request.method == "POST":
        shirt = request.form["shirt"]
        quantity = request.form["quantity"]
        name = request.form["name"]
        address = request.form["address"]
        return render_template("success.html", shirt=shirt, quantity=quantity, name=name)
    return render_template("order.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
