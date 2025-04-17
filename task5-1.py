import random
import pathlib
import string

def randomfiles(length=8):
    znachenia = string.ascii_letters + string.digits
    return ''.join(random.choice(znachenia) for x in range(length))

def createrandomfiles(directory, count=10):
    dir_path = pathlib.Path(directory)
    dir_path.mkdir(parents=True, exist_ok=True)
    
    createdfiles = []
    for x in range(count):
        filename = randomfiles()
        file_path = dir_path / filename
        file_path.touch()
        createdfiles.append(file_path)
    
    return createdfiles

target_directory = "Вывод"
files = createrandomfiles(target_directory)
for file in files:
    print(f"Путь к созданному файлу ->{file.absolute()}")