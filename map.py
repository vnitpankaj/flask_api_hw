# import falsk 
from flask import Flask 

# initialize the Falsk with __name__
app = Flask(__name__)

# craeet url if you dont want to have spesific url then use "/" where defalt url will disply msg
# if you want spesif url the "/hello" then once we run this file then will need toadd '/hello' at 
# the end of terminal url we get after runing this code 
@app.route("/hello", methods=["GET"])
 
# funtion to run the api work 
def foo():
    return "<H3> Hellow world"

# run the api with app.run()
if __name__ == "__main__":
    app.run() # add port here if needed 