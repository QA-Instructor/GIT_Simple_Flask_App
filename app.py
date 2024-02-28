from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_from_flask():
    return "Hello from Flask!"


@app.route('/bye')
def goodbye_from_flask():
    return "Goodbye from Flask!"


if __name__ == "__main__":
    app.run(debug=True)

