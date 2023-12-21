#this code is used to run in local machine the flask application and also on the VMSS

#produce by RYCH
from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

def numerical_integration(lower, upper, N):
   x = np.linspace(lower, upper, N)
   y = np.abs(np.sin(x))
   area = np.sum(y) * (upper - lower) / N
   return area

@app.route('/integrate', methods=['GET'])
def integrate():
   lower = float(request.args.get('lower'))
   upper = float(request.args.get('upper'))
   N_values = [10, 100, 1000, 10000, 100000, 1000000]
   results = [numerical_integration(lower, upper, N) for N in N_values]
   return jsonify(results)

if __name__ == '__main__':
   app.run(debug=True)
