from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/4')
def index2():
    return render_template("specialIndex.html")

@app.route('/(<int:x>)(<int:y>)')
def index3(x, y):
    return render_template("customIndex.html", x =x, y = y)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  