from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='E-Commerce App')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
