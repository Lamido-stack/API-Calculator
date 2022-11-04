from flask import Flask, request, jsonify
import re

app = Flask(__name__)


@app.route('/', methods=['POST'])  #  -> {"slackUsername": "Lamido", "operation_type" : Enum. value, “result”: Integer }
def api():
    data = request.get_json()
    if "operation_type" in data:
        operation = str(data['operation_type']).lower()

        if operation == "addition":

            return jsonify({'slackUsername': 'Lamido', 'operation_type': 'addition', 'result': int(data["x"]) + int(data["y"])})

        elif operation == "subtraction":

            return jsonify({'slackUsername': 'Lamido', 'operation_type': 'subtraction', 'result': int(data["x"]) - int(data["y"])})

        elif operation == "multiplication":

            return jsonify({'slackUsername': 'Lamido', 'operation_type': 'multiplication', 'result': int(data["x"]) * int(data["y"])})
    
        elif "add" or "subtract" or "minus" or "multiply" in operation:

            if "add" in operation:
                result = 0
                for i in re.finditer(r'\d+', operation):
                    result += int(i.group())
                return jsonify({'slackUsername': 'Lamido', 'operation_type': 'addition', 'result': result})

            elif "subtract" or "minus" in operation:
                result = 0
                for i in re.finditer(r'\d+', operation):
                    result = int(i.group()) - result
                return jsonify({'slackUsername': 'Lamido', 'operation_type': 'subtraction', 'result': result})

            if "multiply" in operation:
                result = []
                for i in re.finditer(r'\d+', operation):
                    result.append(int(i.group()))
                return jsonify({'slackUsername': 'Lamido', 'operation_type': 'multiplication', 'result': result[0] - result[1]})

    else:
        return "sorry invalid request: please confirm and try again"



#  Task Description
# Using the same server setup from stage one
# Create an (POST) api endoint that takes the following sample json:
# { “operation_type”: Enum <addition | subtraction | multiplication> , “x”: Integer, “y”: Integer }
# Operation can either be addition, subtraction or mutiplication
# x can be a number and Integer datatype
# y can be a number and Integer datatype
# Based on the operation sent, perform a simple arithmetic operation on x and y
# Return a response with the result of the operation and your slack username
# { “slackUsername”: String, "operation_type" : Enum. value, “result”: Integer }
# Push to GitHub
# Sample Input { “operation_type”: Enum <addition | subtraction | multiplication> , “x”: Integer, “y”: Integer }
# Sample Response Format { “slackUsername”: String, “result”: Integer, “operation_type”: Enum.value }