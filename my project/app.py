from flask import Flask,redirect, url_for
app=Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome"
@app.route('/success/<int:score>')
def success(score):
    return "the person is passed with marks"+ str(score)


@app.route('/failed/<int:score>')
def failed(score):
    return "the person is failed with marks"+ str(score)

@app.route('/result/<int:marks>')
def result(marks):
    result=""
    if marks<50:
        result='failed'
    else:
        result='success'
    return redirect(url_for(result,score=marks))
    
        

if __name__=='__main__':
    app.run(debug =True)