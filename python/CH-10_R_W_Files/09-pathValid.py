from pathlib import Path
homeDir = Path('/home/student/')
notExistDir = Path('/home/who/where/when')
realFile = Path(__file__).resolve()

print(f"home dir exists?\n{homeDir.exists()}\
      \nhome dir is dir?\n{homeDir.is_dir()}\
      \nnotExistDir exists?\n{notExistDir.exists()}\
      \nreal file path is file?\n{realFile.is_file()}\
      \nreal file path is dir?\n{realFile.is_dir()}")

# os.path module works also:
# functions:
# os.path.exists(path)
# os.path.isfile(path)
# os.path.isdir(path)

