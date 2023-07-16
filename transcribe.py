import logging
import sys
import os
from pytube import YouTube
from moviepy.editor import AudioFileClip
import whisper

# Set up logging
logging.basicConfig(level=logging.INFO)

# Download YouTube Video
def download_video(youtube_url, output_path):
    logging.info("Downloading video...")
    yt = YouTube(youtube_url)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video.download(output_path)
    logging.info("Download complete.")
    return video.default_filename

# Extract audio from the video file
def extract_audio(video_path, audio_path):
    logging.info("Extracting audio...")
    video = AudioFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    logging.info("Audio extraction complete.")

# Transcribe audio using Whisper ASR
def transcribe_audio(audio_path):
    logging.info("Transcribing audio...")
    model = whisper.load_model("tiny")
    result = model.transcribe(audio_path)
    logging.info("Transcription complete.")
    return result["text"]

# Save the transcript to a file
def save_transcript(transcript, filename):
    logging.info("Saving transcript...")
    with open(filename, "w") as file:
        file.write(transcript)
    logging.info("Transcript saved.")

if __name__ == "__main__":
    youtube_url = sys.argv[1]  # get YouTube URL from command line argument
    video_id = YouTube(youtube_url).video_id
    output_path = os.path.join(os.getcwd(), f"youtube-{video_id}")  # output dir in current directory
    os.makedirs(output_path, exist_ok=True)  # create output dir if it doesn't exist
    audio_path = os.path.join(output_path, "audio.mp3")
    transcript_filename = os.path.join(output_path, "transcript.txt")

    # Download video
    video_filename = download_video(youtube_url, output_path)
    video_path = os.path.join(output_path, video_filename)

    # Extract audio from the video
    extract_audio(video_path, audio_path)

    # Transcribe the audio using Whisper ASR
    transcript = transcribe_audio(audio_path)

    # Save the transcript to a file
    save_transcript(transcript, transcript_filename)