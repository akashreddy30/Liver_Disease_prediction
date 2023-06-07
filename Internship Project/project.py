from flask import Flask,render_template,request
import pickle
from pdb import set_trace as bp


app=Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/render')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    # bp()
    age=request.form.get('age')
    gender=request.form.get('gender')
    tb=request.form.get('tb')
    db=request.form.get('db')
    ap=request.form.get('ap')
    aa1=request.form.get('aa1')
    aa2=request.form.get('aa2')
    tp=request.form.get('tp')
    a=request.form.get('a')
    agr=request.form.get('agr')
    data=[[float(age),float(gender),float(tb),float(db),float(ap),float(aa1),float(aa2),float(tp),float(a),float(agr)]]
    model=pickle.load(open('liver_analysis_svm.pkl','rb'))
    prediction=model.predict(data)[0]
    print(prediction)
    if(prediction==1):
        return render_template('chance.html',prediction='You have a liver desease problem, You must consult a doctor')
    else:
        return render_template('chance.html',prediction='You dont have a liver desease problem')
if __name__ == '__main__':
    app.run()