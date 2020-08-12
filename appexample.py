from flask import Flask
app = Flask(__name__)
@app.route ('/')
def Hello_World():
    return 'Hello World'

## New Route
@app.route ('/Tendies')
def Chick_McPick():
    return 'Friday Tendies Just Hit Differently fam'
