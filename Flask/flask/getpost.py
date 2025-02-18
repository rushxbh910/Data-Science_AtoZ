from flask import Flask,render_template,request
"""
It creates an instance of the Flask class,
which will act as your WSGI (Web Server Gateway Interface) Application.
"""
#WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
     return "<html><h1>Welcome to the flask course</h1></html>"

@app.route("/index",methods=['GET'])
def index():
     return render_template('index.html') 

@app.route("/aboutus")
def aboutus():
     return render_template('aboutus.html')

@app.route('/form',methods=['GET','POST'])
def form():
     if request.method=='POST':
          name=request.form['name']
          return f'Hello {name}!'
     return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
     if request.method=='POST':
          name=request.form['name']
          return f'Hello {name}!'
     return render_template('form.html')


if __name__=="__main__": #Entry point of any .py file
     app.run(debug=True)