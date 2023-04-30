from flask import Flask,request ,render_template , jsonify

app = Flask(__name__)

@app.route("/")
def show():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def mathoperation():
    if request.method == 'POST':
        ops=request.form['options']
        num1=int(request.form['firstno'])
        num2=int(request.form['secondno'])
        if ops=='Addition':
            result1 = num1+num2
            results='The sum of '+str(num1) +" and "+str(num2) + " is" +str(result1)
            return render_template('result.html',result=results)
        if ops=='Subtraction':
            result1=num1-num2
            results='The difference of '+str(num1) +" and "+str(num2) + " is" +str(result1)
            return render_template('result.html',result=results)
        if ops=='Multiplication':
            result1=num1*num2
            results='The multiplication of '+str(num1) +" and "+str(num2) + " is" +str(result1)
            return render_template('result.html',result=results)
        if ops=='Division':
            result1=num1/num2
            results='The division of '+str(num1) +" and "+str(num2) + " is" +str(result1)
            return render_template('result.html',result=results)



if __name__=="__main__":
    app.run(host="0.0.0.0")
