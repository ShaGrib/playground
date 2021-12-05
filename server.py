from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def base_page():
    return 'This is the base page'

@app.route('/play')
def play_page():
    return render_template('index.html', num = 3, color = "blue")

@app.route('/play/<int:num>')
def multi_page(num):
    return render_template('index.html', num = num, color = "blue")

@app.route('/play/<int:num>/<string:color>')
def multi_color__page(num, color):
    return render_template('index.html', num = num, color = color)

if __name__ == '__main__':
    app.run(debug=True)