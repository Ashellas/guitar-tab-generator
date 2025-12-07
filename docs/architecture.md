# System Architecture

## Overview

The Guitar Tab Generator follows a modular pipeline architecture where each stage processes audio data and passes it to the next stage. The system is designed for clarity, testability, and future extensibility.

## Architecture Diagram
```
┌─────────────────┐
│  Audio Input    │ ← YouTube/Spotify/Local File
└────────┬────────┘
         │ AudioData
         ▼
┌─────────────────┐
│ Source          │ ← Demucs ML Model
│ Separation      │
└────────┬────────┘
         │ SeparatedStems
         ├──────────┬─────────────┐
         ▼          ▼             ▼
    ┌────────┐ ┌────────┐   ┌──────────┐
    │Guitar  │ │Vocals  │...│  Other   │
    │Stem    │ │Stem    │   │  Stems   │
    └───┬────┘ └───┬────┘   └────┬─────┘
        │          │              │
        │          └──────┬───────┘
        │                 ▼
        │          ┌─────────────┐
        │          │  Backing    │
        │          │  Track      │
        │          │  Mixer      │
        │          └─────────────┘
        │                 │
        ▼                 ▼
┌──────────────┐   ┌─────────────┐
│   Pitch      │   │  Output:    │
│  Detection   │   │  Backing    │
└──────┬───────┘   │  Track      │
       │           └─────────────┘
       ▼
┌──────────────┐
│     Tab      │
│  Generation  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Output:     │
│  Tablature   │
└──────────────┘
```

## Module Specifications

### 1. Audio Input Module

**Responsibility**: Acquire and standardize audio data from various sources.

**Components**:
- `AudioFileLoader`: Load local audio files
- `AudioDownloader`: Download from YouTube/Spotify
- `AudioData`: Standardized audio data structure

**Input**: File path or URL (string)
**Output**: `AudioData` object (numpy array + metadata)

**Dependencies**: librosa, soundfile, yt-dlp

**Validation Rules**:
- Supported formats: mp3, wav, flac, ogg, m4a
- Duration: 10-600 seconds
- Automatic resampling to 44.1kHz
- Automatic conversion to mono

---

### 2. Source Separation Module

**Responsibility**: Separate mixed audio into individual instrument stems.

**Components**:
- `Separator`: Interface to Demucs model
- `StemManager`: Manage and organize separated stems
- `SeparatedStems`: Data structure for stem collection

**Input**: `AudioData` object
**Output**: `SeparatedStems` object (dict of stem_name → AudioData)

**Dependencies**: demucs, torch

**Model**: Demucs v4 (htdemucs_ft)
- Separates into: vocals, drums, bass, other (guitar/keys/etc)
- GPU-accelerated when available
- Model auto-downloads on first run (~300MB)

---

### 3. Pitch Detection Module

**Responsibility**: Extract pitch information from guitar audio.

**Components**:
- `PitchDetector`: Extract fundamental frequency over time
- `NoteConverter`: Convert Hz to musical notes

**Input**: Guitar stem (`AudioData`)
**Output**: Time-series pitch data (timestamps, frequencies, confidences)

**Dependencies**: crepe, librosa

**Algorithm**: CREPE model
- 10ms hop length for temporal resolution
- Confidence threshold for note detection
- Polyphonic handling (future enhancement)

---

### 4. Tab Generation Module

**Responsibility**: Convert pitch data to guitar tablature.

**Components**:
- `TabGenerator`: Core tablature logic
- `Tablature`: Data structure for tab representation
- `StringPositionSolver`: Determine optimal string/fret positions

**Input**: Pitch time-series data
**Output**: `Tablature` object (string/fret positions over time)

**Dependencies**: music21, numpy

**Challenges**:
- String/fret position ambiguity (same note, multiple positions)
- Rhythm quantization (converting continuous audio to discrete notes)
- Polyphonic detection (chords)

---

### 5. Backing Track Module

**Responsibility**: Mix non-guitar stems into practice track.

**Components**:
- `BackingTrackMixer`: Combine stems with volume control

**Input**: `SeparatedStems` (excluding guitar)
**Output**: Mixed audio file

**Dependencies**: soundfile, numpy

---

### 6. User Interface Module

**Responsibility**: Provide user interaction layer.

**Components** (Phase 1):
- `CLI`: Command-line interface for demo

**Input**: User commands
**Output**: Status messages, file paths

**Future** (Phase 2):
- Desktop GUI (Electron + Python backend)
- Web interface (React + FastAPI)

---

## Data Flow

1. **Acquisition**: User provides audio source → Input module validates and standardizes
2. **Separation**: Standardized audio → Demucs separates into stems
3. **Branching**:
   - Guitar stem → Pitch detection → Tab generation
   - Other stems → Backing track mixer
4. **Output**: Tablature file + Backing track audio file

## Design Principles

### Single Responsibility
Each module has ONE clear job. No module performs tasks outside its domain.

### Dependency Injection
Modules receive dependencies through constructors, not global imports. Enables testing and modularity.

### Immutability
Data structures are immutable where possible. AudioData, Tablature, etc. are read-only after creation.

### Error Boundaries
Each module validates inputs and raises specific exceptions. Errors don't cascade.

### Type Safety
All functions use type hints. Runtime validation where necessary.

## Testing Strategy

- **Unit Tests**: Each class/function tested in isolation
- **Integration Tests**: Module-to-module data flow
- **End-to-End Tests**: Full pipeline with sample audio files
- **Performance Tests**: Processing time benchmarks

## Configuration Management

All magic numbers, file paths, and parameters live in `config/settings.py`:
- Model parameters
- Audio processing settings
- File path conventions
- Validation thresholds

## Future Enhancements

- [ ] GPU acceleration toggle
- [ ] Multiple tab notation formats (ASCII, MusicXML)
- [ ] Polyphonic chord detection
- [ ] Real-time processing mode
- [ ] Bass/ukulele support
- [ ] MIDI export