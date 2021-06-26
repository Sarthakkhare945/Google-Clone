from flask import Flask,render_template,request
import requests
import json

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
 

    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        inputText = request.form.get('inputText')

        # save api limit for now
        res = requests.get('https://www.googleapis.com/customsearch/v1?key=%20AIzaSyCLomAsGtfKfWffRGInBqOZL1w5EgIwRYc&cx=c480eccdbc9592403' + '&q' + '=' + inputText)
        print(res)
        data = json.loads(res.content)
        
        # print(data)
     
        return render_template('SearchResult.html',inputText=inputText, data = data)

        # return render_template('SearchResult.html',inputText=inputText)
     

@app.route('/SearchresultsAll',methods=['GET','POST'])
def SearchresultsAll():
    # if request.method == 'POST':
    #     return 'I am SearchresultsAll'

    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        # return 'I am post method'
        msg = request.form.get('msg')

        # save api limit for now
        res = requests.get('https://www.googleapis.com/customsearch/v1?key=%20AIzaSyCLomAsGtfKfWffRGInBqOZL1w5EgIwRYc&cx=c480eccdbc9592403' + '&q' + '=' + msg)
        print(res)
        data = json.loads(res.content)
        
        # print(data)
     

        return render_template('SearchResult.html',msg=msg, data = data)
















  
    











# @app.route('/Search')
# def searchResult():
    
#     return render_template('SearchResult.html')