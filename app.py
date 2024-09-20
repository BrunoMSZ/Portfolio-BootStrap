from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/entrarContato')
def contact():
    return render_template("contato.html")

@app.route('/ProjetosPessoais')
def projects():
    return render_template("projetos.html")

if __name__ == '__main__':
    app.run()
