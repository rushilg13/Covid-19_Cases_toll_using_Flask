import requests
from flask import Flask, render_template, url_for

app = Flask(__name__)

api='https://api.covid19api.com/summary'

@app.route('/', methods=['GET', 'POST'])
def home():
    dataset=[]
    
    r=requests.get(api.format()).json()
    print(r)

    world = {
        'TotalConfirmed': r['Global']['TotalConfirmed'],
        'TotalDeaths': r['Global']['TotalDeaths'],
        'TotalRecovered': r['Global']['TotalRecovered']
            }
    for i in range(0,186):
        data ={
            'Country':r['Countries'][i]['Country'],
            'TotalConfirmed': r['Countries'][i]['TotalConfirmed'],
            'TotalDeaths': r['Countries'][i]['TotalDeaths'],
            'TotalRecovered': r['Countries'][i]['TotalRecovered']
            }
        dataset.append(data)

    return render_template('toll.html', world=world, dataset=dataset)

if __name__ == "__main__":
    app.run(debug=True)