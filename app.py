from flask import Flask
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import transformers
from transformers import BartTokenizer, BartForConditionalGeneration
from flask import request

app = Flask(__name__)
CORS(app)  # chrome auto blocks client side

@app.route('/api/summarize', methods=['GET'])
@app.route('/api/summarize', methods=['GET'])
def get_nlp_summary():
    try:
        youtube_url = request.args.get('youtube_url')
        min_length = int(request.args.get('min_length', 120))
        max_length = int(request.args.get('max_length', 160))
        video_id = extract_video_id(youtube_url)
        transcript_text = get_transcript(video_id)
        summary_text = summarize_nlp(transcript_text, min_length, max_length)
        return summary_text, 200
    except Exception as e:
        return str(e), 500


@app.route('/api/summarize-lsa', methods=['GET'])
def get_lsa_summary():
    try:
        youtube_url = request.args.get('youtube_url')
        video_id = extract_video_id(youtube_url)
        transcript_text = get_transcript(video_id)
        summary_text = summarize_lsa(transcript_text)
        return summary_text, 200
    except Exception as e:
        return str(e), 500
    
def extract_video_id(youtube_url):
    start_index = youtube_url.find("v=") + 2
    end_index = youtube_url.find("&", start_index)
    if end_index == -1:
        video_id = youtube_url[start_index:]
    else:
        video_id = youtube_url[start_index:end_index]
    return video_id

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
    transcript_text = " ".join([dict['text'] for dict in transcript])
    return transcript_text

def summarize_nlp(transcript_text, min_length, max_length):
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    input_ids = tokenizer.encode(transcript_text, return_tensors='pt')
    summary_ids = model.generate(input_ids, max_length=max_length, min_length=min_length, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary_text

def summarize_sentences(sentence_vectors, sentences):
    lsa_model = TruncatedSVD(n_components=1)
    sentence_scores = lsa_model.fit_transform(sentence_vectors)
    
    ranked_sentences = [(score, sentence) for score, sentence in zip(sentence_scores, sentences)]
    ranked_sentences.sort(reverse=True)
    
    return ranked_sentences[:3]

def summarize_lsa(transcript_text):
    sentences = transcript_text.split(". ")
    
    vectorizer = TfidfVectorizer()
    sentence_vectors = vectorizer.fit_transform(sentences)
    
    lsa_model = TruncatedSVD(n_components=1)
    sentence_scores = lsa_model.fit_transform(sentence_vectors)
    
    ranked_sentences = [(score, sentence) for score, sentence in zip(sentence_scores, sentences)]
    ranked_sentences.sort(reverse=True)
    
    summary_sentences = ranked_sentences[:3]
    
    summary_text = ". ".join([sentence for _, sentence in summary_sentences])
    
    return summary_text

if __name__ == '__main__':
    app.run(debug=True)
