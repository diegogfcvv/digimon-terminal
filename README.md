# Digimon Terminal Viewer

Display Digimon sprites directly in your terminal! Quite based in [pokemon-colorscripts](https://gitlab.com/phoneybadger/pokemon-colorscripts) and with the sprites of [Tortoiseshel](https://withthewill.net/threads/full-color-digimon-dot-sprites.25843/).

## Installation

### Prerequisites
- Python 3.6+ (check with `python3 --version`)
- Terminal with UTF-8 support

```bash
git clone https://github.com/diegogfcvv/digimon-terminal.git
cd digimon-terminal
```

## Usage
```bash
# Show random Digimon with metadata
python digimon.py -r -m

# Show specific Digimon without description
python digimon.py -n Agumon

# List all available Digimon
python digimon.py -l
```

## Features
- 835 Digimon available
- Random selection mode
- Pixel art display
- Optional metadata (name + description)

## Issues?
- This is my first repo, so expect some of them
- The naming with Digimon is a bit weird, so some of them could have a different name as Name and another one as Description. This is because all of changes between versions.