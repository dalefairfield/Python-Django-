from flask import Flask, render_template, request, redirect, session
import unirest
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/name_card', methods=['GET'])
def create_user():
    name = request.args['name']
    url = "https://omgvamp-hearthstone-v1.p.mashape.com/cards/search/" + name
    response = unirest.get(url,
    headers={"X-Mashape-Key": "zGqd0yg6Tqmshj5jb9f5tufn5fWap1sekWcjsnFJypkLX6VxcL"})
    card= response.body
    return render_template('index.html', card=card)
app.run(debug=True) # run our server
