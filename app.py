from flask import Flask, render_template, request , jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar_foto', methods=['POST'])
def processar_formulario():
    # Recebendo o arquivo
    arquivo = request.files['fotos']
    if arquivo :
        print("arquivo recebido")
    else:
        print("Não recebi arquivo")

    # Recebendo as caixas de seleção
    checkbox1 = request.form.get('GrayScale')
    checkbox2 = request.form.get('Sepia')
    checkbox3 = request.form.get('Blur')
    checkbox4 = request.form.get('EdgeDetection')
    checkbox5 = request.form.get('ContrastAdjust')
    checkbox6 = request.form.get('Sharpen')

    # Fazer o processamento das imagens aqui

    # Por exemplo, você pode imprimir os valores dos campos apenas para testar
    print("Arquivo:", arquivo.filename)
    print("Checkbox 1:", checkbox1)
    print("Checkbox 2:", checkbox2)
    print("Checkbox 3:", checkbox3)
    print("Checkbox 4:", checkbox4)
    print("Checkbox 5:", checkbox5)
    print("Checkbox 6:", checkbox6)

    return '', 200

if __name__ == '__main__':
    app.run(debug=True)