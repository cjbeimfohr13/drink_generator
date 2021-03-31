from flask import Flask, render_template,jsonify
import json
import requests

app = Flask(__name__)

@app.route( '/', methods=['GET'])
def index():
    cocktail=requests.get("https://www.thecocktaildb.com/api/json/v1/1/random.php")
    data = json.loads(cocktail.content) 
    print(data)
    return render_template("index.html", data = data["drinks"][0])
   

if __name__ == "__main__":
    app.run(debug=True)
