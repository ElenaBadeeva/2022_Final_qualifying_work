from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('test1.html', name='Kate')


def hello11():
    return "Hello " * 11


def processing():
    model = "Tmp model"
    # TODO: реализовать логику модели
    return model


@app.route('/hello')
def hello_world():
    model = processing()
    return model


@app.route('/text1/')
@app.route('/text2/')
def text1():
    return 'Text 1 or 2'


@app.route('/user/<name>/')
def user_profile(name):
    name = name * 10
    return f"Profile page of user {name}"


@app.route('/url_map/')
def url_map():
    return str(app.url_map)


@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')

        if username == 'root' and password == 'pass':
            message = "Correct username and password"
        else:
            message = "Wrong username or password"

    return render_template('login.html', message=message)


if __name__ == '__main__':
    app.run()
