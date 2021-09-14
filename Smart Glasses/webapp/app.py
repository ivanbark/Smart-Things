from flask import Flask, render_template

image_path = "test"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True, host='10.80.17.1')