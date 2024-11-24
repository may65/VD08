from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
import random

app = Flask(__name__)

my_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global my_list
    my_list = get_news()
    return render_template("index.html", news=my_list)

@app.route('/data')
def data():
    # Получение случайного индекса
    i = random.randrange(len(my_list))
    # Вывод случайного индекса и соответствующего элемента
    return jsonify([i,my_list[i]])

def get_news():
    url = f"https://zenquotes.io/api/quotes"
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
   app.run(debug=True)