from flask import Flask, render_template
import db as conec
base=conec.conexion()
app = Flask(__name__)
@app.route('/')
def home():
    b = []
    print("Pronósticos del Tiempo ")
    for bc in base.list_collection_names():
        a = base[bc]
        b.append(f"LIBROS DE {bc.upper()}")
        for j in a.find({}):
            print(j['name'])
            libro = {
                "_id ": j['_id'],
                "name": j['name'],
                "author": j['author'],
                "magazine": j['magazine']
            }
            b.append(libro)
    return render_template('inicio.html', listadb=b)
if __name__ == '__main__':
    app.run(debug=True, port=4000)