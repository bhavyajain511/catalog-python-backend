from flask import Flask, jsonify
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def scrape_olx():
    url = "https://www.olx.in/scooters_c1413"
    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')
    info = soup.find_all('span')
    img = soup.find_all('figure')
    info1 = soup.find_all('div')

    list_img = []
    price1 = []
    details1 = []
    title1 = []
    subtitle1 = []

    for j in img:
        if (j.get('data-aut-id') == 'itemImage'):
            for child in j.descendants:
                if child.name == 'img':
                    list_img.append(child.get('src'))

    for i in info:
        if (i.get('data-aut-id') == 'itemPrice'):
            price1.append(i.string)
        if (i.get('data-aut-id') == 'itemDetails'):
            details1.append(i.string)
        if (i.get('data-aut-id') == 'itemTitle'):
            title1.append(i.string)
        if (i.get('data-aut-id') == 'itemSubTitle'):
            subtitle1.append(i.string)

    for i in info1:
        if (i.get('data-aut-id') == 'itemPrice'):
            price1.append(i.string)
        if (i.get('data-aut-id') == 'itemDetails'):
            details1.append(i.string)
        if (i.get('data-aut-id') == 'itemTitle'):
            title1.append(i.string)
        if (i.get('data-aut-id') == 'itemSubTitle'):
            subtitle1.append(i.string)

    col = ['price', 'details', 'title', 'subtitle', 'img']
    df = pd.DataFrame(columns=col)
    count = 0
    for row in price1:
        entry = []
        if (len(price1) > count):
            entry.append(price1[count])
        else:
            entry.append("")
        if (len(details1) > count):
            entry.append(details1[count])
        else:
            entry.append("")
        if (len(title1) > count):
            entry.append(title1[count])
        else:
            entry.append("")
        if (len(subtitle1) > count):
            entry.append(subtitle1[count])
        else:
            entry.append("")
        if (len(list_img) > count):
            entry.append(list_img[count])
        else:
            entry.append("")
        count += 1
        df.loc[count] = entry
    return df.to_dict(orient='records')

# @app.route('/api/olx', methods=['GET'])
@app.route('/api/olx', methods=['GET'])
def get_data():
    data = scrape_olx()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

    # http://127.0.0.1:5000/api/olx
    # http://localhost:5000/api/olx
