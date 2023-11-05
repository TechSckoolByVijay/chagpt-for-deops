from flask import Flask, render_template


app = Flask(__name__)

# Existing routes
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='E-Commerce App')


@app.route('/products')
def products():
    return "Check out our latest products."


@app.route('/about')
def about():
    return "Stay Awesome....!"

# New route for calculation, This is just for fun  : http://127.0.0.1/calculate/10/20
@app.route('/calculate/<int:num1>/<int:num2>')
def calculate(num1, num2):
    result = num1 + num2  # You can replace this with your own calculation
    return f"The result of {num1} + {num2} is {result}."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
