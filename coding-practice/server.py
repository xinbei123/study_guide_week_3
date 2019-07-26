from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################
@app.route('/save-name')
def save_name():

    name = request.args.get("fullname")

    session['name'] = name

    return render_template('homepage.html')


@app.route('/form')
def show_form():
    return render_template('form.html')


@app.route('/results')
def show_results():

    cheery = request.args.get('cheery')
    honest = request.args.get('honest')
    dreary = request.args.get('dreary')

    # app.logger.info("message: %s", message)

    if cheery:
        message = "hello!"
    elif honest:
        message = "world!"
    elif dreary:
        message = "yahhh"

    return render_template('results.html', message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
