# YouTube Transcript Summarizer

This project is a Chrome Extension that summarizes the transcript of a YouTube video using Natural Language Processing (NLP). It includes two different summarization models and allows users to customize the parameters of the summarization process. The project consists of a Python API that retrieves the transcript, an NLP model that performs text summarization, and a Flask backend REST API that exposes the summarization service to the client.

## Features

- **Two Summarization Models**: The extension offers two different models for summarizing video transcripts: a Transformer-based model (BART) and a Latent Semantic Analysis (LSA) model.

- **Customizable Parameters**: Through the extension's options page, users can customize the parameters of the summarization process, including the minimum and maximum length of the summary.

- **Real-Time Summarization**: The extension provides summaries in real-time as users watch videos.

- **Error Handling**: The extension includes robust error handling to ensure a smooth user experience.

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
3. Choose either "NLP Summarize" or "LSA Summarize" to generate a summary of the video transcript.
4. The summary will be displayed in a pop-up window.
5. To adjust the summarization parameters, right-click on the extension icon and select "Options".

## References

- [YouTube Transcript API Documentation](https://developers.google.com/youtube/v3/docs/captions)
- [Read, Write and Parse JSON using Python](https://realpython.com/python-json/)
- [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/abs/1910.13461)
- [Latent Semantic Analysis](https://en.wikipedia.org/wiki/Latent_semantic_analysis)

Note: This project is currently locally hosted, so it can only be used on your own machine.
