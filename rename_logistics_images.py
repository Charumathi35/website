import os
import re

dir_path = r'd:\websites\Design1\images\logistics scroll'
files = os.listdir(dir_path)

# Pattern: frame_0_00_1f.jpeg
pattern = re.compile(r'frame_(\d+)_(\d+)_(\d+)f')

parsed_files = []

print(f"Scanning {dir_path}...")

for f in files:
    if not (f.endswith('.jpeg') or f.endswith('.jpg')):
        continue
    # Skip potential duplicates like 'frame... (1).jpeg' if the original exists
    # But if it's a unique frame, maybe keep it? 
    # The size check suggested exact duplicates. 
    # I will stick to skipping '(1)' to be safe and clean.
    if '(1)' in f:
        print(f"Skipping duplicate: {f}")
        continue
        
    match = pattern.search(f)
    if match:
        sort_key = (int(match.group(1)), int(match.group(2)), int(match.group(3)))
        parsed_files.append((sort_key, f))
    else:
        print(f"Pattern mismatch: {f}")

# Sort by time/frame
parsed_files.sort()

print(f"Found {len(parsed_files)} frames.")

# Rename
for i, (key, filename) in enumerate(parsed_files):
    # Change extension to .jpg for consistency if needed, or keep .jpeg
    # User example code used .jpg. I'll convert alignment to .jpg for simplicity in code
    new_name = f"logistics_{str(i+1).zfill(3)}.jpg"
    
    old_full = os.path.join(dir_path, filename)
    new_full = os.path.join(dir_path, new_name)
    
    # Handle overlap? Rename to temp first? 
    # Since new names look very different from old names, direct rename should be safe
    # UNLESS we are re-running on already renamed files.
    # The pattern matches "frame_", so already renamed "logistics_" won't be touched.
    
    try:
        os.rename(old_full, new_full)
        print(f"Renamed {filename} -> {new_name}")
    except Exception as e:
        print(f"Error renaming {filename}: {e}")

print("Done.")
