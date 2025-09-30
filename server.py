"""
Emotion Detection Server

This script defines a Flask-based server for performing emotion detection on user-provided text.

"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Function to detect the emotion for an input text
    """
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']
    return (
        f"For the given statement, the system response is 'anger': {anger_score} "
        f"'disgust': {disgust_score}, 'fear': {fear_score}, "
        f"'joy': {joy_score} and 'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the index.html
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
