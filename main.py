from flask import Flask
from flask import request, jsonify, render_template, send_file, send_from_directory


"""Flask Implementation"""

app = Flask(__name__)
@app.route("/")
def home():
    return '<h1>Welcome to the R Shiny Server</h1>'

#To use the predict button in our web-app
@app.route('/get_data', methods=['GET', 'POST'])
def predict():
    '''
    For sending the train stats files
    '''
    model_handle = request.args.get('fname')
    if model_handle == "Files/train_stats.json":
      return send_file("train_stats.json", as_attachment=True)
    if model_handle == "Files/train_set.csv.gz":
      return send_file("train_set.csv.gz", as_attachment=True)
    
app.run()
