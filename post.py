from flask import Flask, request,render_template

app=Flask(__name__)


@app.route("/form",methods=['GET','POST'])
def test():
    if request.method=='POST':
        name=request.form.get("n1")
        address=request.form.get("n2")

    return "<h1>Data Received from customer by POST method<br>name: {} address: {}</h1>".format(name,address)

@app.route("/")
def entry():
    return render_template('homepost.html')


if __name__=='__main__':
    app.run(debug=True)