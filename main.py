   
from flask import Flask
from flask import request
from markupsafe import escape
from flask import render_template
from flask import make_response
from flask import session
from flask import jsonify
import random

#http://localhost:5000/

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


# @app.route('/addInvestor',methods = ['GET','POST'])
# def addInvestor():
#     if request.method == "POST":
#         dataResult = request.get_json(force=True)
#         print('data',dataResult)
#         return jsonify(dataResult)


# @app.route('/addCrypto',methods = ['GET','POST'])
# def addCrypto():
#     if request.method == "POST":
#         dataResult = request.get_json(force=True)
#         print('data',dataResult)
#         return jsonify(dataResult)



if __name__ == "__main__":
    app.run(debug=True)