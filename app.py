from flask import Flask,request,render_template,jsonify
import json


app=Flask(__name__ )

@app.route('/')
def welcome():
    return "Welcome to Flask"


@app.route('/cal',methods=['GET'])
def math_operator():
    operation = request.json["operation"]
    Number1 = request.json["number1"]
    Number2 = request.json["number2"]

    if operation == "add":
        result = int(Number1)+int(Number2)
    elif operation == "multiply":   
        result = int(Number1)*int(Number2)
    elif operation == "division":   
        result = int(Number1)/int(Number2)
    else:
        result = int(Number1)-int(Number2)
    # return jsonify(result)       
    return "The operation is {} and the result is {}".format(operation,result)


if __name__ == "__main__":
    app.run(port=1100)

