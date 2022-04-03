from flask import Flask, request, render_template, url_for, redirect, flash
import flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'superdupersecretkey'   
logined = False
User = ''

@app.route('/')
def index():
    return render_template('base.html', text='Добро пожаловать', signed = logined, user = User)

@app.route('/LoginPage')
def loginForm():
    return render_template('LoginPage/login.html')



@app.route('/LoginPage', methods=('GET', 'POST'))
def Login():
    global logined
    global User
    logined = False
    if request.method == 'POST':
        log = request.form['Login']
        psswrd = request.form['Password']
        if(log == 'login') and (psswrd == 'password'):   
            User = log
            logined = True        
            return redirect(url_for('profile', username = log)) # ВНЕШНИЙ ДИНАМИЧЕСКИЙ РОУТИНГ
        else:
            
            return redirect(url_for('Login'))
    return redirect(url_for('Login'))


@app.route('/User/<username>')
def profile(username):
    if not logined:
        return redirect(url_for('index'))
    return render_template('/User/profile.html', user = username)








if __name__ == '__main__':
    app.run()