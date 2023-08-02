from flask import Flask,request,rerunnder_template


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
        result = Number1+Number2
    elif operation == "multiply":   
        result = Number1*Number2
    elif operation == "division":   
        result = Number1/Number2
    else:
        result = Number1-Number2
    return result       
   


if __name__ == "__main__":
    app.run()

