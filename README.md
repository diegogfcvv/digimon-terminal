# Digimon Terminal Viewer

Display Digimon sprites directly in your terminal!

Quite based in [pokemon-colorscripts](https://gitlab.com/phoneybadger/pokemon-colorscripts) and with the sprites of [Tortoiseshel](https://withthewill.net/threads/full-color-digimon-dot-sprites.25843/).

## Installation

### Prerequisites
- Python 3.6+ (check with `python3 --version`)
- Terminal with UTF-8 support (your terminal is probably supported if it's modern enough, you shouldn't have to worry about this)
- [pipx](https://pipx.pypa.io/stable/installation/) (will install Python packages in isolated environments, make sure to follow the "ensurepath" command too!)

Restart your terminal after this!

# Then install digimon-terminal
```bash
pipx install git+https://github.com/diegogfcvv/digimon-terminal.git


## Usage
```bash

# Show random Digimon
digimon -r

# Show random Digimon with metadata
digimon -r -m

# Show specific Digimon without description (Agumon, in this case)
digimon -n agumon

# Show specific Digimon with description (Gabumon, in this case)
digimon -n gabumon -m

# List all available Digimon (there are quite a lot, expect much scrolling, useful for (un)localised names)
digimon -l
```

## Features
- Pixel art display
- 835 Digimon available
- Random selection mode
- Optional metadata with random mode (name + description)

## Issues?
- This is my first repo, so expect some bugs
- The naming with Digimon is a bit weird because all of changes between versions, so some of them could have a different name as Name and another one as Description. Also, this could make search a bit finicky.

## Changelog

### v1.1
- Fixed transparency in sprites

### v1.0
- Initial release