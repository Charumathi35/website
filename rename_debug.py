import os
import re
import sys

log_file = open("rename_log.txt", "w")
sys.stdout = log_file
sys.stderr = log_file

print("Starting script...")

dir_path = r'd:\websites\Design1\images\logistics scroll'
try:
    files = os.listdir(dir_path)
    print(f"Listed {len(files)} files in {dir_path}")
except Exception as e:
    print(f"Error listing directory: {e}")
    sys.exit(1)

pattern = re.compile(r'frame_(\d+)_(\d+)_(\d+)f')
parsed_files = []

for f in files:
    if not (f.lower().endswith('.jpeg') or f.lower().endswith('.jpg')):
        continue
    if '(1)' in f:
        continue
        
    match = pattern.search(f)
    if match:
        sort_key = (int(match.group(1)), int(match.group(2)), int(match.group(3)))
        parsed_files.append((sort_key, f))
    else:
        print(f"No match for {f}")

parsed_files.sort()
print(f"Sorted {len(parsed_files)} files.")

for i, (key, filename) in enumerate(parsed_files):
    new_name = f"logistics_{str(i+1).zfill(3)}.jpg"
    old_full = os.path.join(dir_path, filename)
    new_full = os.path.join(dir_path, new_name)
    
    print(f"Renaming {filename} to {new_name}")
    try:
        os.rename(old_full, new_full)
    except Exception as e:
        print(f"Failed to rename {filename}: {e}")

print("Done.")
log_file.close()
