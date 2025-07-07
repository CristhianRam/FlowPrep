from flask import Flask
from services.preprocessing import *
from flask import request, render_template, send_file
import pandas as pd
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")  # Renderiza tu HTML desde /templates/

@app.route('/api/process', methods=["POST"])
def process():
    print("→ Recibiendo petición /api/process")
    # Obtener datos del formulario
    file = request.files.get("file")
    null_action = request.form.get("null_action")

    if not file:
        return "No se recibió archivo", 400

    csv_text = file.read().decode("utf-8")

    # Generar DataFrame
    df = load_data(csv_text)

    # Manejo de nulos
    if (null_action != "none"):
        if (null_action == "rm-0"  or null_action == "rm-1"):
             remove_nulls(df, null_action)
        else:
            replace_nulls(df, null_action)

    # Crear CSV en memoria
    output = io.StringIO()
    df.to_csv(output, index=False)
    output.seek(0)

    # Enviar como archivo descargable
    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype='text/csv',
        as_attachment=True,
        download_name='processed_data.csv'
    )


if __name__== "__main__":
    app.run(debug=True)