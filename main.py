from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class SuccessForm(FlaskForm):
    submit = SubmitField('На главную')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'muzo-rztvs'
user = ''


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница',
                           username=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        s = form.username.data
        global user
        user = s
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/play')
def play():
    return render_template('play.html')


@app.route('/success', methods=['GET', 'POST'])
def success():
    form = SuccessForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('success.html', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')