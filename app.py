from flask import Flask, render_template
 
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello world, WWW!'

@app.route('/')
def homepage():
    return render_template('p1_homepage_withCSS.html')

@app.route('/exercise')
def homepage_exercise():
    return render_template('p2_homepage_withCSS.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)



