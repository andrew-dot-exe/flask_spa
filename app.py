from flask import *
"""
TODO: пристроить генератор
TODO: сделать коннектор для spa
TODO: сделать вывод доступных столбцов для генерации
TODO: сделать вывод заголовка таблицы с выбранными столбцами  
TODO: сделать вывод сгенерированных данных в таблицу

"""
app = Flask(__name__)

@app.route('/')
def route_main():
    return render_template('index.html', name=None)