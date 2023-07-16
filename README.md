# YouTube Video Transcriber

This Python script downloads a YouTube video, extracts its audio, transcribes the audio using OpenAI's Whisper Automatic Speech Recognition (ASR) model, and saves the transcript to a text file. 

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.6 or later.
- You have installed [FFmpeg](https://ffmpeg.org/download.html). FFmpeg is a free and open-source software project that produces libraries and programs for handling multimedia data. This project uses FFmpeg for extracting audio from video files.

  After installing FFmpeg, make sure it's added to your system's PATH. Here's how you do it on different operating systems:

  - On Windows, see this [StackOverflow answer](https://stackoverflow.com/a/48556892).
  
  - On Linux, FFmpeg is usually added to the PATH during installation, but if it's not, you can add it by editing your `~/.bashrc` or `~/.bash_profile` file to include `export PATH=/path/to/ffmpeg/bin:$PATH`, where `/path/to/ffmpeg/bin` is the path to the directory containing the FFmpeg executable.
  
  - On macOS, if you install FFmpeg using Homebrew (`brew install ffmpeg`), it should be added to the PATH automatically.

## Installation

To install the dependencies for this project, follow these steps:

1. Clone or download this repository to your local machine.

2. Navigate to the project directory in your terminal.

3. Run the following command to install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

To use this script, provide the YouTube URL as a command line argument:

```bash
python video_transcribe.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

This script will create an output directory in the current directory named `youtube-{video_id}`, download the video to that directory, extract the audio to the same directory, and save the transcript in the same directory. The video ID is extracted from the YouTube URL, and is the unique identifier for the video on YouTube.

---

Please replace `https://www.youtube.com/watch?v=dQw4w9WgXcQ` with the actual URL of the YouTube video you want to transcribe.