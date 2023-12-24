from flask import Flask, redirect, url_for, render_template, request
import sudoku

app = Flask(__name__)

board = sudoku.Board()

@app.route("/")
def index():
    return render_template('index.html', board=board.getAllSquares())
    
@app.route("/gen", methods=['GET','POST'])
def gen():
    diff = request.form['difficulty']
    board.setDifficulty(int(diff))
    board.refreshBoard()
    return redirect(url_for('index'))

@app.route("/solve", methods=['GET','POST'])
def solve():
    board.genBoard()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)