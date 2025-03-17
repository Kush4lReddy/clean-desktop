import os
import shutil
from datetime import datetime
import time 
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def organize_files():

    today = datetime.today()

    day = today.day
    month = today.month
    year = today.year


    desktop_path = os.path.join(os.environ['HOME'], 'Desktop')
    # images = os.path.join(desktop_path, 'Images')
    other = os.path.join(desktop_path, 'Other')
    audio = os.path.join(desktop_path, 'Audio')
    code = os.path.join(desktop_path, 'code')

    print(desktop_path)
    
    image_extensions = {'.jpg', '.jpeg', '.png', '.pdf', '.gif', '.bmp', '.tiff', '.webp'}

    audio_extensions = {'.aif', '.aiff', '.aifc', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.oga', '.wav', '.wma', '.wpl', '.m3u', '.flac', '.aac', '.opus', '.amr', '.ra', '.rm'}
    
    programming_extensions = {'.html', '.htm', '.css', '.js', '.jsx', '.ts', '.tsx', '.py', '.java', '.class', '.jar', '.c', '.h', '.cpp', '.cc', '.cxx', '.hpp', '.cs', '.php', '.php3', '.php4', '.php5', '.phtml', '.rb', '.erb', '.swift', '.kt', '.kts', '.go', '.rs', '.sh', '.bash', '.zsh', '.pl', '.pm', '.lua', '.r', '.R', '.dart', '.sql', '.yaml', '.yml', '.json', '.md', '.rst', '.makefile', '.mk', '.cmake', '.bat', '.cmd', '.ps1', '.psm1', '.asm', '.s', '.lisp', '.cl', '.scm', '.hs', '.lhs', '.jl', '.fs', '.fsi', '.fsx', '.ex', '.exs', '.ts', '.tsx', '.m', '.mm', '.vb', '.vbs', '.f', '.f90', '.f95', '.f03', '.f08', '.pro', '.groovy', '.gvy', '.gy', '.gsh'}

    image_folder_name = f'Images before {day}-{month}-{year}'
    imagePath = os.path.join(desktop_path, image_folder_name)
    os.makedirs(imagePath, exist_ok=True)

    with os.scandir(desktop_path) as desktopFiles:
        for file in desktopFiles:
            if file.is_file():
                print("file aint a file")
                if file.name.lower().endswith(tuple(image_extensions)):
                    shutil.move(file.path, imagePath)

                elif file.name.lower().endswith(tuple(programming_extensions)):
                    shutil.move(file.path, os.path.join(audio, file.name))

                elif file.name.lower().endswith(tuple(audio_extensions)):
                    shutil.move(file.path, os.path.join(code, file.name))

                else:
                    shutil.move(file.path, os.path.join(other, file.name))

if __name__ == "__main__":
    organize_files()

