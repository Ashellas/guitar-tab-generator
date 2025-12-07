# Guitar Tab Generator

An AI-powered application that separates guitar from mixed audio tracks and generates accurate tablature notation, providing a backing track for practice.

## Features

- **Multi-source Input**: Load audio from local files (MP3, WAV, FLAC) or download from YouTube/Spotify
- **AI Source Separation**: Isolate guitar, vocals, drums, bass, and other instruments
- **Automatic Tab Generation**: Convert isolated guitar audio to guitar tablature notation
- **Backing Track Generation**: Create practice tracks with all instruments except guitar

## Project Status

🚧 **In Development** - Initial scaffolding complete

### Completed
- [x] Project structure
- [x] Documentation framework
- [ ] Audio input module
- [ ] Source separation
- [ ] Pitch detection
- [ ] Tab generation
- [ ] UI/CLI interface

## Technical Stack

### Core Libraries
- **Demucs**: Music source separation (Meta Research)
- **librosa**: Audio analysis and processing
- **crepe**: Pitch detection
- **yt-dlp**: YouTube audio downloading
- **soundfile**: Audio I/O

### Language & Framework
- **Python 3.9+**: Core implementation
- **NumPy**: Numerical computing
- **pytest**: Testing framework

## Installation

### Prerequisites
- Python 3.11 or higher
- pip package manager
- (Recommended) CUDA-capable GPU for faster processing

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/guitar-tab-generator.git
cd guitar-tab-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/
```

## Usage

*Coming soon - CLI interface under development*

## Project Structure
```
guitar-tab-generator/
├── src/              # Source code
├── tests/            # Unit and integration tests
├── config/           # Configuration files
├── data/             # Data directories (gitignored)
├── docs/             # Documentation
└── requirements.txt  # Python dependencies
```

## Development

See [docs/architecture.md](docs/architecture.md) for system design details.

See [docs/development_log.md](docs/development_log.md) for development progress.

## License

MIT License - This is a non-commercial educational project.

## Acknowledgments

- **Demucs** by Meta AI Research
- **librosa** audio processing library
- **CREPE** pitch detection model