from flask import Flask, request,render_template

app=Flask(__name__)


@app.route("/form")
def test():
    name=request.args.get("n1")
    address=request.args.get("n2")

    return "<h1>Data Received from customer by GET method<br>name: {} address: {}</h1>".format(name,address)

@app.route("/")
def entry():
    return render_template('home.html')


if __name__=='__main__':
    app.run(debug=True)