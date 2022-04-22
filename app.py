#import teh Flask class from the flask module
from flask import Flask, render_template

#create the application object
app = Flask(__name__)

#use decorators to link the funciotn to a url
@app.route('/')
def homr():
	return "Hello, Wolrd!" #return a string

@app.route('/welcome')
def welcome():
	return render_template('welcome.html') #render a template

@app.route('/pigrupo')
def pigrupo():
	return render_template('pigrupo.html')


#start the server with the 'run()' method
if __name__ == '__main__':
	app.run(debug=True)