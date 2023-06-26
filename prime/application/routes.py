from flask import Flask, jsonify, Response 
from flask import jsonify
import sys
from flask import jsonify
import json
from flask import json

app = Flask(__name__)

@app.route('/date/<ageInMonths>', methods=['GET', 'POST'])
def prime(ageInMonths):
    try: 
        ageMonths = int(float(ageInMonths))
    except TypeError:
        return "ValueError: enter a number"
    
    ageMonths = int(float(ageInMonths))
    factorCounter = 0 
    ageMonths = int(ageMonths)
    if ageMonths > 1:
        while ageMonths > 0:    
            if ageInMonths % ageMonths == 0:
                factorCounter = factorCounter + 1
            ageMonths = ageMonths - 1
    else:
        return "You do not appear to exist"
    # print(str(prime), file=sys.stderr)
    # print(str(prime), file=sys.stdout)
    if factorCounter > 2:
        return "composite"
    else:
        return "prime"    