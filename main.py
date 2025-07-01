from flask import Flask, render_template, request, jsonify
from hangman import Hangman

# Tell Flask: 嘿 Flask，這是我網站的主程式，幫我建立一個應用程式物件叫 app，以後我就會用它來做網站啦！
app = Flask(__name__)

game_names = ["Hangman", "Guess Number"]

game = Hangman()

@app.route('/')
def home():
   return render_template("index.html", buttons=game_names)

@app.route('/hangman')
def hangman():
    game = Hangman()
    return render_template("hangman.html", **game.get_context())

@app.route('/hangman/start', methods=['POST'])
def startHangman():
    global game
    level = int(request.json.get('level'))
    guess_time = game.set_guess_times(level)

    init_variables = game.start_guess()

    return jsonify({
        "guessTimes": guess_time,
        "result": init_variables['result'],
        "question": init_variables['question'],
        "letters": init_variables['letters']
    })

@app.route('/hangman/guess', methods=['POST'])
def guess():
    global game
    guess_letter = str(request.json.get('letter')).upper()
    guess_result = game.guess_letter(guess_letter)

    return jsonify(guess_result)

if __name__ == "__main__":
    app.run(debug=True)
    # debug=True: 程式碼改了會自動重新啟動（方便開發）、發生錯誤時會顯示詳細錯誤畫面（開發時超有用）