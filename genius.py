import lyricsgenius
import os, sys

TOKEN = "YOUR_TOKEN_GOES_HERE"
genius = lyricsgenius.Genius(TOKEN, verbose=False)

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def render_tui(name, choices=[], data=None):
    while True:
        os.system("clear")
        print(color.GREEN + color.BOLD + name + color.END)

        for c in choices:        
            print(f"{color.BLUE}[{c['num']}]{color.END} {c['choice']}")

        user_choice = input("Select Number: ")

        for c in choices:
            if user_choice == str(c['num'])[-1*(len(color.END + color.BLUE)+1):][0]:
                c['func']((data, c['num']))
                return

def start(data=None):
    choices = [{"choice": "Search by Title", "num":1, "func":search_title},
                {"choice": "Search by Artist", "num":2, "func":search_artist},
                {"choice": "Exit", "num":f"{color.RED}{color.BOLD}q{color.END}{color.BLUE}", "func":exit}]
    render_tui("Genius TUI", choices)

def search_title(data=None):
    choices = [{"choice":"Enter Song Title", "num":1, "func":input_title},
                {"choice":"Back", "num":f"{color.BOLD}b{color.END}{color.BLUE}", "func":start}]
    render_tui("Search for Title", choices)

def input_title(data=None):
    user_input = input("Enter Song Title: ")
    song = genius.search_song(user_input)
    if song == None:
        print("\nCouldn't find anything.\n")
    else:
        os.system("clear")
        print(f"{color.BOLD}{color.GREEN}{song.artist} - {song.title} - {song.album} ({song.year}){color.END}\n")
        print(song.lyrics)
        
    input(f"\n{color.GREEN}Hit [Enter] to go back. {color.END}")
    search_title()

def search_artist(data=None):
    choices = [{"choice":"Enter Artist Name", "num":1, "func":input_artist},
            {"choice":"Back", "num":f"{color.BOLD}b{color.END}{color.BLUE}", "func":start}]
    render_tui("Search for Artist", choices)

def input_artist(data=None):
    user_input = input("Enter Artist: ")
    print("Searching...")
    artist = genius.search_artist(user_input, max_songs = 5, get_full_info=False)
    (artist.songs) # [('song 1', 'artist'), ('song2', 'artist')]
    choices = []
    i = 0
    for song in artist.songs:
        i += 1
        choices.append({"choice":f"{song.title}",  "num":i, "func":choose_song})
    
    choices.append({"choice":f"Search for other Song by {artist.name}" , "num":f"{color.BOLD}s{color.END}{color.BLUE}", "func":search_title_by_artist})
    choices.append({"choice":"Back", "num":f"{color.BOLD}b{color.END}{color.BLUE}", "func":search_artist})

    render_tui(f"[{artist.name}] - Choose Song", choices, data = artist)

def choose_song(data):
    os.system("clear")
    artist = data[0]
    num = data[1]-1
    song = artist.songs[num]
    print(f"{song.artist} - {song.title} - {song.album} ({song.year})\n")
    print(song.lyrics)

    input(f"\n{color.GREEN}Hit [Enter] to go back. {color.END}")
    search_artist()

def search_title_by_artist(data):
    artist = data[0]
    os.system("clear")
    user_input = input(f"{color.BOLD}{color.GREEN}[{artist.name}] - Search for Song: {color.END}")
    song = genius.search_song(user_input, artist=artist.name)
    if song == None:
        print("\nCouldn't find anything.\n")
    else:
        os.system("clear")
        print(f"{song.artist} - {song.title} - {song.album} ({song.year})\n")
        print(song.lyrics)
        
    input(f"\n{color.GREEN}Hit [Enter] to go back. {color.END}")
    search_artist(1)

def exit(num):
    sys.exit()

if __name__ == "__main__":
    start()
