from flask import Flask
import openpyxl as px
import pandas as pd
import itertools as it
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    data = getData()
    return data.to_json()

def getData():
    wb = px.load_workbook('EARS_sample_index_dataset.xlsx')
    ws = wb['payout_monitoring_2016']
    data = ws.values
    cols = next(data)[1:]
    data = list(data)
    idx = [r[0] for r in data]
    data = (it.islice(r, 1, None) for r in data)
    df = pd.DataFrame(data, index=idx, columns=cols)
    output = df.PAYOUT
    return output

if __name__ == "__main__":
    getData()
    app.run()

