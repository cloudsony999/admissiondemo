from flask import Flask, request,render_template
import pandas as pd

app=Flask(__name__)
# Unpickle model 
model = pd.read_pickle('generate.pickle') 

@app.route("/project")
def test():
    gre=int(request.args.get("g"))
    toff=int(request.args.get("t"))
    cgpa=float(request.args.get("c"))
    result = model.predict([[gre,toff,cgpa]])
    
    print(result,result.__class__)
    return f"Chances are : { result[0] * 100:.2f}%"

@app.route("/")
def entry():
    return render_template('projectweb.html')


if __name__=='__main__':
    app.run(debug=True)