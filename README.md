# genius-tui
Access lyrics from genius via the command line

This will only work Linux and MacOS (and WSL I guess).

## Installation
### Clone the repository
```bash
git clone https://github.com/z80z80z80/genius-tui.git
cd genius-tui
```

### Install dependencies
```bash
pip install --user lyricsgenius
```

### Access Token
Before using this, you'll need an access token for the Genius API. Follow this guide: https://github.com/johnwmillr/LyricsGenius#setup

After getting your token, replace YOUR\_TOKEN\_GOES\_HERE with your token in line 4 of genius.py.

### Optional: Generate alias for easy access
- bash
```bash
echo 'alias genius-tui="python '$PWD'/genius.py"' >> ~/.bashrc
source ~/.bashrc
```
- zsh
```bash
echo 'alias genius-tui="python '$PWD'/genius.py"' >> ~/.zshrc
source ~/.zshrc
```
- fish
```bash
echo 'alias genius-tui="python '$PWD'/genius.py"' >> ~/.config/fish/config.fish
source ~/.config/fish/config.fish
```

## Usage
### With alias
```bash
genius-tui
```
### Without alias
```bash
python genius.py
```

