from flask import Flask, request, jsonify, send_file, send_from_directory
from gtts import gTTS
import speech_recognition as sr
import pymongo
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['tts_stt_db']
collection = db['user_data']

# Serve the index.html file from the static folder
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Endpoint for text-to-speech
@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    text = request.json.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    tts = gTTS(text)
    file_path = 'output.mp3'
    tts.save(file_path)
    
    # Save interaction to MongoDB
    collection.insert_one({'type': 'text-to-speech', 'text': text})

    return send_file(file_path, as_attachment=True)

# Endpoint for speech-to-text
@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(file) as source:
        audio = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return jsonify({'error': 'Speech recognition could not understand audio'}), 500
    except sr.RequestError:
        return jsonify({'error': 'Could not request results from Google Speech Recognition service'}), 500
    
    # Save interaction to MongoDB
    collection.insert_one({'type': 'speech-to-text', 'text': text})

    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)
