from flask import Flask

test_app = Flask(__name__)

@test_app.route('/')
def hello():
    return 'Hey Flask'


if __name__ == '__main__':
    test_app.run(debug=True)
