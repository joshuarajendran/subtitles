from flask import Flask
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi
import transformers
from transformers import BartTokenizer, BartForConditionalGeneration
from flask import request

app = Flask(__name__)
CORS(app)  # chrome auto blocks client side 

@app.route('/api/summarize', methods=['GET'])
def get_summary():
    youtube_url = request.args.get('youtube_url')
    video_id = extract_video_id(youtube_url)
    transcript_text = get_transcript(video_id)
    summary_text = summarize(transcript_text)
    return summary_text, 200

def extract_video_id(youtube_url):
    start_index = youtube_url.find("v=") + 2
    end_index = youtube_url.find("&", start_index)
    if end_index == -1:
        video_id = youtube_url[start_index:]
    else:
        video_id = youtube_url[start_index:end_index]
    return video_id

# function that accepts youtube video id as input parameter
def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
    transcript_text = " ".join([dict['text'] for dict in transcript])
    return transcript_text

def summarize(transcript_text):
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    input_ids = tokenizer.encode(transcript_text, return_tensors='pt')
    summary_ids = model.generate(input_ids, max_length=160, min_length=120, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary_text

# server the app when this file is run
if __name__ == '__main__':
    app.run(debug=True)

