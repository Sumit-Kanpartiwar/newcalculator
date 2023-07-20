
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
from calculator_class import calculator
from logging import exception
#from loguru import logger


app = Flask(__name__) # initializing a flask app
# Configure loguru to log to a file
#logger.add("app.log", rotation="500 MB", format="{time} | {level} | {message}", level="DEBUG")

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")
 #   logger.info("Received a request to the home page")

@app.route('/predict',methods=['POST']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            objname = calculator(num1, num2)
            is_operation = request.form['operation']
            if (is_operation=='addition'):
                result = objname.add()

            elif (is_operation == 'subtraction'):
                result = objname.sub()

            elif (is_operation == 'multiplication'):
                result = objname.prod()

            elif (is_operation == 'division'):
                result = objname.div()

            print(f'result for {is_operation} of {num1} and {num2} is', result)
            # showing the results in a UI
            return render_template('results.html',result= result, is_operation= is_operation, num1=num1, num2=num2)
        except Exception as e:
            print('The Exception message is: ',e)
  #          logger.error(f"An error occurred,{e}")
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app