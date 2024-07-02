from flask import Flask, render_template, request, jsonify
from googletrans import Translator
import webbrowser
from threading import Timer

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text')
    dest_lang = data.get('dest_lang', 'en')

    if text:
        try:
            translation = translator.translate(text, dest=dest_lang)
            return jsonify({'translated_text': translation.text})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Please provide text to translate'}), 400

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True)
