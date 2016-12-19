from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

# our index route will handle rendering our form
@app.route('/')
def index():
    if not 'gold' in session.keys():
        session['gold']=0
    if not 'building' in session.keys():
        session['building']=''
    return render_template('index.html', gold=session['gold'], building=session['building'])
# notice how we defined which HTTP methods are allowed by this route

@app.route('/process_money', methods=['POST'])
def create_user():
    building = request.form['building']
    if building=='farm':
        g = random.randrange(10, 21)
        session['gold'] += g
        session['building']='farm'
        session['activity']="Earned", session['gold'], "gold at", session['building']
    elif building=='cave':
        g=random.randrange(5, 11)
        session['gold'] += g
        session['building']='cave'
        session['activity']="Earned", session['gold'], "gold at", session['building']
    elif building=='house':
        g=random.randrange(2, 6)
        session['gold'] += g
        session['building']='house'
        session['activity']="Earned", session['gold'], "gold at", session['building']
    elif building=='casino':
        g=random.randrange(-50, 51)
        session['gold'] += g
        session['building']='casino'
        session['activity']="Earned", session['gold'], "gold at", session['building']
    return render_template('index.html', activity=session['activity'])

app.run(debug=True) # run our server
