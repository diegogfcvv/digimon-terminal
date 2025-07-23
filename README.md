# Digimon Terminal Viewer

# (It's not working right now, I'm trying to fix it)

Display Digimon sprites directly in your terminal!

Quite based in [pokemon-colorscripts](https://gitlab.com/phoneybadger/pokemon-colorscripts) and with the sprites of [Tortoiseshel](https://withthewill.net/threads/full-color-digimon-dot-sprites.25843/).

## Installation

### Prerequisites
- Python 3.6+ (check with `python3 --version`)
- Terminal with UTF-8 support

```bash
# First install pipx if you don't have it
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Then install digimon-terminal
pipx install git+https://github.com/diegogfcvv/digimon-terminal.git

## Usage
```bash
# Show random Digimon with metadata
digimon -r -m

# Show specific Digimon without description
digimon -n Agumon

# List all available Digimon
digimon -l
```

## Features
- 835 Digimon available
- Random selection mode
- Pixel art display
- Optional metadata (name + description)

## Issues?
- This is my first repo, so expect some of them
- The naming with Digimon is a bit weird, so some of them could have a different name as Name and another one as Description. This is because all of changes between versions.