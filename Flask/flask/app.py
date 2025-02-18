from flask import Flask,render_template
"""
It creates an instance of the Flask class,
which will act as your WSGI (Web Server Gateway Interface) Application.
"""
#WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
     return "<html><h1>Welcome to the flask course</h1></html>"

@app.route("/index")
def index():
     return render_template('index.html') 

@app.route("/aboutus")
def aboutus():
     return render_template('aboutus.html')


if __name__=="__main__": #Entry point of any .py file
     app.run(debug=True)