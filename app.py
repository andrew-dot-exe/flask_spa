from flask import *
import adapter

"""
TODO: сделать вывод доступных столбцов для генерации
TODO: сделать вывод заголовка таблицы с выбранными столбцами  
TODO: сделать вывод сгенерированных данных в таблицу

"""
app = Flask(__name__)

@app.route('/')
def route_main():
    columns = list(adapter.columns_person.keys())
    return render_template('index.html', columns=columns, name=None)