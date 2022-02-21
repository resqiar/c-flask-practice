from flask import Flask, render_template, request
from dotenv import load_dotenv
import math
from libs.changeScoreToLetter import changeScoreToLetter
from libs.countHypotenuse import countHypotenuse

app = Flask(__name__)
load_dotenv()

@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/square')
def squarePage():
    return render_template('square.html')

@app.route('/hypotenuse')
def hypotenusePage():
    return render_template('hypotenuse.html')

@app.route('/score', methods=['POST'])
def convertScore():
    data = request.get_json()

    if data.get('score'):
        return changeScoreToLetter(int(data.get('score')))
    else:
        return {
            "status": 400,
            "result": "Please input score"
        }

@app.route('/squareroot', methods=['POST'])
def squareroot():
    data = request.get_json()

    if data.get('number'):
        number = int(data.get('number'))
        return {
            "status": 200,
            "result": math.sqrt(number)
        }
    else:
        return {
            "status": 400,
            "result": "Please input number"
        }
        
@app.route('/hypotenuse', methods=['POST'])
def hypotenuse():
    data = request.get_json()

    if data.get('inputA') and data.get('inputB'):
        return countHypotenuse(int(data.get('inputA')), int(data.get('inputB')))
    else:
        return {
            "status": 400,
            "result": "Please input score"
        }
        