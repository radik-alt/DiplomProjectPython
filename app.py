from flask import Flask, render_template, request, flash

app = Flask(__name__)
menu = [{"name": "Главное", "url": "/index"},
        {"name": "Регистрация", "url": "/register"},
        {"name": "О языке", "url": "/"},
        {"name": "С чего начать", "url": "/"}]


@app.route('/index')
@app.route('/')
def home():
    return render_template('index.html', title="Дипломная работ!", menu=menu)


@app.route("/lesson")
def lesson():
    return render_template("page/Lesson.html", title="Уроки!", menu=menu)


@app.route("/auth")
def auth():
    return render_template("page/LogIn.html", title="Авторизаиця", menu=menu)


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        try:
            name = request.form.get("name")
            email = request.form.get("email")
            password = request.form.get("password")

            if len(name) < 5:
                flash("Пиздец! Звоните фиксикам!")
            else:
                flash("Все нормально! Ты умница!")

        except Exception as err:
            print(err)
    return render_template('page/Registration.html', title="Регистрация", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page/Page404.html", title="Страница не найдена!")


if __name__ == '__main__':
    app.run()
