"""
Global configuration settings for the Guitar Tab Generator.

All magic numbers, file paths, and configurable parameters are defined here.
"""

from pathlib import Path

# ============================================================================
# PROJECT PATHS
# ============================================================================

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"
MODELS_DIR = DATA_DIR / "models"

# Create directories if they don't exist
INPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
MODELS_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================================
# AUDIO PROCESSING
# ============================================================================

# Standard sample rate for all processing (44.1kHz CD quality)
TARGET_SAMPLE_RATE = 44100

# Supported audio formats
SUPPORTED_AUDIO_FORMATS = {'.mp3', '.wav', '.flac', '.ogg', '.m4a'}

# Audio validation thresholds
MIN_DURATION_SECONDS = 10.0  # Minimum track length
MAX_DURATION_SECONDS = 600.0  # 10 minutes maximum for demo

# Audio processing
CONVERT_TO_MONO = True  # Convert stereo to mono for simplicity
NORMALIZE_AUDIO = True  # Normalize audio levels

# ============================================================================
# AUDIO DOWNLOADING
# ============================================================================

# yt-dlp settings
YOUTUBE_AUDIO_FORMAT = 'mp3'
YOUTUBE_AUDIO_QUALITY = '320'  # kbps

# URL patterns
YOUTUBE_URL_PATTERNS = [
    r'youtube\.com/watch',
    r'youtu\.be/',
    r'youtube\.com/shorts/'
]

SPOTIFY_URL_PATTERNS = [
    r'open\.spotify\.com/track'
]

# ============================================================================
# SOURCE SEPARATION (Demucs)
# ============================================================================

# Model selection
DEMUCS_MODEL = "htdemucs_ft"  # Demucs v4 fine-tuned model

# Processing
DEMUCS_DEVICE = "cuda"  # Use "cpu" if no GPU available
DEMUCS_SHIFTS = 1  # Number of random shifts for better separation (higher = slower but better)
DEMUCS_OVERLAP = 0.25  # Overlap between chunks

# Output stems
STEM_NAMES = ["vocals", "drums", "bass", "other"]
GUITAR_STEM_NAME = "other"  # Guitar typically in "other" category

# ============================================================================
# PITCH DETECTION (CREPE)
# ============================================================================

# CREPE model size: tiny, small, medium, large, full
CREPE_MODEL_CAPACITY = "medium"  # Balance between speed and accuracy

# Hop length for pitch detection (in milliseconds)
CREPE_HOP_LENGTH_MS = 10  # 10ms = 100 fps

# Confidence threshold for valid pitch detection (0.0 to 1.0)
PITCH_CONFIDENCE_THRESHOLD = 0.5

# ============================================================================
# TAB GENERATION
# ============================================================================

# Guitar tuning (standard EADGBE)
STANDARD_TUNING = ["E2", "A2", "D3", "G3", "B3", "E4"]

# Fret range
MIN_FRET = 0
MAX_FRET = 24

# Rhythm quantization
QUANTIZE_TO_16TH_NOTES = True  # Snap timings to 16th note grid

# Tab output format
TAB_WIDTH = 80  # Characters per line in ASCII tab

# ============================================================================
# BACKING TRACK
# ============================================================================

# Volume levels (0.0 to 1.0)
BACKING_TRACK_VOLUME = 0.8
STEM_VOLUMES = {
    "vocals": 0.8,
    "drums": 0.9,
    "bass": 0.9,
    "other": 0.0  # Guitar excluded
}

# Output format
BACKING_TRACK_FORMAT = "wav"  # High quality for practice
BACKING_TRACK_BITRATE = "320k"

# ============================================================================
# LOGGING
# ============================================================================

LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = PROJECT_ROOT / "app.log"

# ============================================================================
# TESTING
# ============================================================================

TEST_DATA_DIR = PROJECT_ROOT / "tests" / "test_data"
TEST_AUDIO_FILE = TEST_DATA_DIR / "sample.mp3"