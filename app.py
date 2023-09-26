from flask import *

import adapter

import os

"""
TODO: сделать генерацию скрипта для sql

TODO: оптимизация верстки
TODO: предупреждение о несовпадении имен и фамилии при выборе полей  по отдельности
"""
app = Flask(__name__)
columns = list(adapter.columns_person.keys()) + list(adapter.columns_address.keys())
gen_values = []

@app.route('/')
def route_main():    
    return render_template('index.html', columns=columns, name=None, gen_cols=['first', 'second', 'third'])

@app.route('/generate', methods=['POST'])
def generate():
    global gen_values
    gen_cols = request.form.getlist('to_generate')
    amount = int(request.form.get('records_amount'))
    gender = request.form.get('gender')
    values = adapter.get_generated_info(gen_cols, amount, gender)
    gen_values = values
    return render_template('index.html', columns=columns, name=None, gen_cols=gen_cols, values=values)

@app.route('/download', methods=['GET'])
def download():
    filename = adapter.save_csv(gen_values)
    
    @after_this_request
    def delete_file(response):
        os.remove(os.path.join('download', filename))
        return response
    
    return send_from_directory(
        'download', filename, as_attachment=True
    )
    
@app.route('/download_json', methods=['GET'])
def download_json():
    filename = adapter.save_json(gen_values)
    
    @after_this_request
    def delete_file(response):
        os.remove(os.path.join('download', filename))
        return response
    
    return send_from_directory(
        'download', filename, as_attachment=True
    )