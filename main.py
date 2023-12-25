from flask import Flask, redirect, url_for, render_template, request
import sudoku

#Init flask and our sudoku board
app = Flask(__name__)
board = sudoku.Board()

@app.route("/")
def index():
    return render_template('index.html', board=board.getAllSquares())
    
@app.route("/gen", methods=['GET','POST'])
def gen():
    #Generates a new board using the inputed difficulty
    diff = request.form['difficulty']
    board.setDifficulty(int(diff))
    board.refreshBoard()
    return redirect(url_for('index'))

@app.route("/solve", methods=['GET','POST'])
def solve():
    #Solves the board
    board.genBoard()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)