import os
import random
from pytube import YouTube
import youtube_dl
import colorama
from colorama import Fore, Style
import pyfiglet
from tqdm import tqdm
import sys

# Initialize colorama
colorama.init()

class VideoDownloader:
    def __init__(self):
        self.banner_texts = [
            "Video Downloader",
            "Media Fetcher",
            "Quick Download"
        ]
        self.clear_screen()
        self.display_banner()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_banner(self):
        banner = pyfiglet.figlet_format(random.choice(self.banner_texts))
        print(Fore.CYAN + banner + Style.RESET_ALL)
        print(Fore.YELLOW + "Developed by Mohamed Fouad" + Style.RESET_ALL)

    def download_video(self, url, format_choice, quality=None):
        try:
            ydl_opts = {
                'format': 'bestaudio' if format_choice == 'MP3' else f'bestvideo[height<={quality}]+bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s',
                'progress_hooks': [self.show_progress]
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(Fore.GREEN + "Download completed!" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}" + Style.RESET_ALL)

    def show_progress(self, d):
        if d['status'] == 'downloading':
            total_size = d['total_bytes']
            downloaded_size = d['downloaded_bytes']
            progress = downloaded_size / total_size
            bar_length = 50
            arrow = '█' * int(round(bar_length * progress))
            spaces = ' ' * (bar_length - len(arrow))
            percent = round(progress * 100)
            remaining_time = d.get('eta', 0)
            speed = d.get('speed', 0) / (1024 * 1024)  # Speed in MB/s

            print(Fore.YELLOW + f"\r[{arrow}{spaces}] {percent}% | Speed: {speed:.2f} MB/s | Remaining time: {remaining_time:.0f} seconds" + Style.RESET_ALL, end='')

    def choose_format(self):
        while True:
            print(Fore.CYAN + "\nChoose the format to download:" + Style.RESET_ALL)
            print(Fore.GREEN + "1. Download as MP3" + Style.RESET_ALL)
            print(Fore.BLUE + "2. Download as MP4" + Style.RESET_ALL)
            print(Fore.YELLOW + "3. Back" + Style.RESET_ALL)
            print(Fore.RED + "4. Exit" + Style.RESET_ALL)

            choice = input(Fore.CYAN + "\nEnter your choice: " + Style.RESET_ALL)

            if choice == '1':
                return 'MP3'
            elif choice == '2':
                return 'MP4'
            elif choice == '3':
                return 'Back'
            elif choice == '4':
                print(Fore.RED + "Goodbye!" + Style.RESET_ALL)
                sys.exit()
            else:
                print(Fore.RED + "Invalid choice, please try again." + Style.RESET_ALL)

    def main_menu(self):
        while True:
            print(Fore.GREEN + "1. Download a single video" + Style.RESET_ALL)
            print(Fore.BLUE + "2. Download a playlist" + Style.RESET_ALL)
            print(Fore.YELLOW + "3. Show instructions" + Style.RESET_ALL)
            print(Fore.RED + "4. Exit" + Style.RESET_ALL)

            choice = input(Fore.CYAN + "\nEnter your choice: " + Style.RESET_ALL)

            if choice == '1':
                url = input(Fore.BLUE + "Enter the video URL: " + Style.RESET_ALL)
                format_choice = self.choose_format()
                if format_choice != 'Back':
                    quality = input(Fore.BLUE + "Choose quality (e.g., 720, 1080): " + Style.RESET_ALL)
                    self.download_video(url, format_choice, quality)
            elif choice == '2':
                url = input(Fore.BLUE + "Enter the playlist URL: " + Style.RESET_ALL)
                format_choice = self.choose_format()
                if format_choice != 'Back':
                    quality = input(Fore.BLUE + "Choose quality (e.g., 720, 1080): " + Style.RESET_ALL)
                    self.download_video(url, format_choice, quality)
            elif choice == '3':
                self.show_instructions()
            elif choice == '4':
                print(Fore.RED + "Goodbye!" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Invalid choice, please try again." + Style.RESET_ALL)

    def show_instructions(self):
        instructions = [
            "Instructions:",
            "1. Choose a video or playlist to download.",
            "2. Select the desired format (MP3 or MP4).",
            "3. Enter the video or playlist URL.",
            "4. Monitor the progress of your download."
        ]
        for line in instructions:
            print(Fore.CYAN + line + Style.RESET_ALL)
        input(Fore.YELLOW + "\nPress any key to return to the main menu..." + Style.RESET_ALL)

if __name__ == "__main__":
    downloader = VideoDownloader()
    downloader.main_menu()
