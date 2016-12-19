from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/', methods=['POST'])
def process():
    return render_template('index.html')
    # return render_template('result.html', name=name, location=location, language=language, message=message)
@app.route('/result', methods=['POST'])
def process():
    return render_template('result.html')

@app.route('/users', methods=['POST'])
def create_user():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    message = request.form['message']
    if len(request.form['name']) < 1:
        message = flash("Name cannot be empty!") # just pass a string to the flash function
    else:
        return render_template('result.html')
    if len(request.form['message']) > 120:
        message = flash("Comment in under 120 characters!") # just pass a string to the flash function
    else:
        return render_template('result.html')


    return render_template('result.html', name=name, location=location, language=language, message=message)
app.run(debug=True) # run our server
