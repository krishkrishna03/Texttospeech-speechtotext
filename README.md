# Text-to-Speech and Speech-to-Text Flask App

This Flask application provides endpoints for converting text to speech and speech to text. The application uses Google Text-to-Speech (gTTS) for text-to-speech conversion and Google's Speech Recognition for speech-to-text conversion. It also stores user interactions in MongoDB.

## Features

- **Text-to-Speech**: Convert text input into spoken audio using Google Text-to-Speech.
- **Speech-to-Text**: Convert spoken audio into text using Google's Speech Recognition API.
- **MongoDB Storage**: Save user interactions (both text-to-speech and speech-to-text) into a MongoDB database.

## Prerequisites

- Python 3.6 or later
- Flask
- gTTS (Google Text-to-Speech)
- SpeechRecognition (Google Speech Recognition)
- pymongo (MongoDB client)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/krishkrishna03/Texttospeech-speechtotext.git
    cd Texttospeech-speechtotext
    ```

2. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `requirements.txt` file** with the following content:

    ```txt
    Flask
    gtts
    SpeechRecognition
    pymongo
    ```

5. **Ensure MongoDB is installed and running** on your local machine.

## Running the Application

1. **Start the Flask application**:

    ```bash
    python app.py
    ```

2. **Open a web browser** and navigate to `http://127.0.0.1:5000/`.

3. **Use the web interface** to interact with the application.

## Endpoints

- **`GET /`**: Serve the `index.html` file from the static folder.
- **`POST /text-to-speech`**: Converts text to speech. Requires JSON with the key `text`.
    - Example Request:
      ```json
      {
          "text": "Hello, world!"
      }
      ```
    - Returns an MP3 file of the spoken text.
- **`POST /speech-to-text`**: Converts speech to text. Requires an audio file.
    - Example Request:
      ```bash
      curl -X POST -F "file=@path_to_audio_file" http://127.0.0.1:5000/speech-to-text
      ```
    - Returns JSON with the transcribed text.

## Code Explanation

- `app.py`: The main Flask application file that sets up the web server, handles text-to-speech and speech-to-text conversion, and interacts with MongoDB.
- `index.html`: HTML file in the `static` directory for the web interface.

## Example Usage

1. **Text-to-Speech**:
    - Send a POST request to `/text-to-speech` with JSON payload.
    - Download the resulting MP3 file.

2. **Speech-to-Text**:
    - Send a POST request to `/speech-to-text` with an audio file.
    - Receive the transcribed text in JSON format.

## Troubleshooting

- Ensure that all dependencies are installed correctly.
- Make sure MongoDB is running and accessible.
- Verify that the `index.html` file is located in the `static` folder.

## Contributing

Feel free to open issues or submit pull requests to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For questions or comments, please contact [your-email@example.com](mailto:your-email@example.com).
