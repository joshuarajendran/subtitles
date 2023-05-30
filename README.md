# YouTube Transcript Summarizer

This project is a Chrome Extension that summarizes the transcript of a YouTube video using Natural Language Processing (NLP). It consists of a Python API that retrieves the transcript, the BART (Bidirectional and Auto-Regressive Transformer) model that performs text summarization, and a Flask backend REST API that exposes the summarization service to the client.

## Installation

1. Clone this repository to your local machine.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Run the Flask server by executing `python app.py`.
4. Open Google Chrome and navigate to `chrome://extensions`.
5. Enable Developer mode by toggling the switch in the top right corner.
6. Click on "Load unpacked" and select the folder where you cloned this repository.
7. The extension should now be installed and ready to use.

## Usage

1. Navigate to a YouTube video you want to summarize.
2. Click on the extension icon in your browser toolbar.
3. Click on "Summarize" to generate a summary of the video transcript.
4. The summary will be displayed in a pop-up window.

Note: This project is currently locally hosted, so it can only be used on your own machine.
