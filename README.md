# Advanced Speech Transcription App

## Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
 - [Prerequisites](#prerequisites)
 - [Installation](#installation)
- [How to Use](#how-to-use)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)
- [Support and Contact](#support-and-contact) 
## Introduction

The Advanced Speech Transcription App aims for precise yet fast speech recognition using multiple threads for each phrase recorded.
It uses OpenAI's Whisper model **locally**, so ***no API key required***.

## Key Features

- **State-of-the-Art Transcription**: Utilizes OpenAI's Whisper models to deliver exceptionally accurate transcriptions.
- **Real-Time Recognition**: Immediate transcription with real-time voice processing capabilities.
- **Adaptive Noise Reduction**: Reduces background noise and enhances speech clarity.
- **Multi-Threaded Background Processing**: Splits speech recognition into as many threads as needed depending on the speaker's type of speech.
- **Custom Stop Commands**: Easily terminate transcription sessions with user-defined phrases.
- **Persistent Output**: Automatically saves the transcribed text to your chosen destination.

## Getting Started

### Prerequisites

Before installing the Advanced Speech Transcription App, you'll need:
- **Python 3.9** or above
- **Pip package manager** (usually included with Python)
- **Microphone** (duh 😂)

### Installation

```bash
# Clone the project repository
git clone https://github.com/AlexYelisieiev/advanced-speech-transcription.git

# Navigate to the project directory
cd advanced-speech-transcription-app

# Create and activate a virtual environment
python3 -m venv venv
venv/bin/activate

# Install all dependencies
pip install -r requirements.txt

# Launch the application
python main.py
```

> [!NOTE]
> Once launched for the first time, it will install the Whisper model to use locally.

## How to Use

Initiate the app and expose it to the speech source once it says "Listening:" (until then, it's adjusting the microphone to the environment). The real-time transcription will appear on your screen. To end the transcription, simply utter a predefined stop phrase, and the session will conclude, saving the transcription to the designated file.

## Customization

Personalize your experience by editing the `SpeechRecognizer` class parameters:
- `whisper_model`: Select from [various Whisper model options](https://github.com/openai/whisper#available-models-and-languages) to match your transcription accuracy needs.
- `output_file_path`: Designate your desired file path for storing transcripts.
- `STOP_PHRASES`: Customize the stop phrases for an intuitive way to end transcription sessions.

## Contributing

New PRs, feedback, etc. are always welcome.
Also, if you want to chat or something, DMs are open 😉

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Support and Contact

For support, feature requests, or to report a bug, please submit an issue on the GitHub repository. Create PRs if you want to add something yourself 🤝


<p style="margin-top: 50px;" align="center"><b>Made with 💙 by <a href="https://alexyelisieiev.github.io">Alex Yelisieiev</a></b></p>
