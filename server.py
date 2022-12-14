from flask import Flask, render_template
app = Flask(__name__)

@app.route('/checkerboard/<int:x>')
def singlerow(x):
    return render_template('single.html',x=x,color1='black',color2='red')

@app.route('/checkerboard/<int:x>/<int:y>')
def doublerow(x,y):
    return render_template('double.html',x=x,y=y,color1='black',color2='red')

@app.route('/checkerboard/<int:x>/<int:y>/<string:color1>/<string:color2>')
def checkerboard(x,y,color1,color2):
    return render_template('index.html',x=x,y=y,color1=color1,color2=color2)

if __name__ == '__main__':
    app.run(debug=True)