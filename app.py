from flask import *
import adapter

"""
TODO: сделать сохранение данных в формате csv, json
TODO: сделать генерацию скрипта для sql

TODO: оптимизация верстки
TODO: предупреждение о несовпадении имен и фамилии при выборе полей  по отдельности
"""
app = Flask(__name__)
columns = list(adapter.columns_person.keys()) + list(adapter.columns_address.keys())

@app.route('/')
def route_main():    
    return render_template('index.html', columns=columns, name=None, gen_cols=['first', 'second', 'third'])

@app.route('/generate', methods=['POST'])
def generate():
    gen_cols = request.form.getlist('to_generate')
    amount = int(request.form.get('records_amount'))
    gender = request.form.get('gender')
    values = adapter.get_generated_info(gen_cols, amount, gender)
    return render_template('index.html', columns=columns, name=None, gen_cols=gen_cols, values=values)