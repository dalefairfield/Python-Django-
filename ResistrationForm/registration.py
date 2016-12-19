from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/', methods=['POST'])
def process():
    return render_template('index.html')
    # return render_template('result.html', name=name, location=location, language=language, message=message)

# @app.route('/result', methods=['POST'])
# def process():
#     return render_template('result.html')

@app.route('/users', methods=['POST'])
def create_user():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    message = request.form['message']
    if len(request.form['email'], request.form['first_name'], request.form['last_name'], request.form['password'], request.form['confirm_password']) < 1:
        flash("No field cannot be empty!") # just pass a string to the flash function
    else:
        return render_template('index.html')

    NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
    if not NAME_REGEX.match(request.form['first_name'],request.form['last_name'])   :
        flash("Names can only contain letters.")
    else:
        return render_template('index.html')

    if len(request.form['password']) < 8:
        flash("Password must contain at least 8 characters")
    else:
        return render_template('index.html')

    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(request.form['email']) :
        flash("Password must contain at least 8 characters")
    else:
        return render_template('index.html')

    if request.form['password'] != request.form['confirm_password']:
        flash("Password must match confirm password")
    else:
        return render_template('index.html')

    return render_template('result.html', name=name, location=location, language=language, message=message)
