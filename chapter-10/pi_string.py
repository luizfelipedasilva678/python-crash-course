from pathlib import Path

path = Path("pi_milion_digits.txt")
contents = path.read_text()
lines = contents.splitlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
