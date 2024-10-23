from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página principal que renderiza home.html
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
