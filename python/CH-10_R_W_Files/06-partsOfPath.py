from pathlib import Path

p = Path(__file__).resolve()
print(f"\nAbsolute path: {p}\n")
# /home/student/Projects/automate-boring-stuff/CH-10/06-partsOfPath.py

print(f"Segments of path:\
      \nanchor: {p.anchor}\
      \nparent: {p.parent}\
      \nname: {p.name}\
      \nstem: {p.stem}\
      \nsuffix: {p.suffix}\
      \ndrive: {p.drive} no drive letter on linux.")

# tuple of parts of path
print(f"\nParts values in tuple:\n{p.parts}")
print(f"part-0: {p.parts[0]}\
      \npart-1: {p.parts[1]}\
      \npart-2: {p.parts[2]}\
      \npart-3: {p.parts[3]}\
      \npart-4: {p.parts[4]}\
      \npart-5: {p.parts[5]}\
      \npart-6: {p.parts[6]}\n")

print(f"part 2 till 4: {p.parts[2:5]}\n")

# Parents
print(f"Parents:\
      \n{Path.cwd()}\
      \nparent-0: {Path.cwd().parents[0]}\
      \nparent-1: {Path.cwd().parents[1]}\
      \nparent-2: {Path.cwd().parents[2]}\
      \nparent-3: {Path.cwd().parents[3]}\n")
