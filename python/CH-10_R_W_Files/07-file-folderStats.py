from pathlib import Path
import time

file = Path(__file__).resolve()
print(file.name)

# file stat()
print(f"\nFile stats:\n{file.stat()}\
      \n\nSize: {file.stat().st_size} bytes\
      \nmodified (Unix epoch time): {file.stat().st_mtime}")

print(f"last modified (normal time):\
 {time.asctime(time.localtime(file.stat().st_mtime))}")

