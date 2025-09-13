import os
import shutil
from datetime import datetime

# Folders (you can change these)
source_folder = r"C:\Users\Tina\Downloads"
destination_folder = r"C:\Users\Tina\Downloads"

# Create destination folders if they don't exist
folders = {
	"images": [".jpg", ".jpeg", ".png", ".gif"],
	"documents": [".pdf", ".docx", ".txt", ".xlsx"],
	"others": []
}
for folder in folders:
	os.makedirs(os.path.join(destination_folder, folder), exist_ok=True)

# Go through files in source
for filename in os.listdir(source_folder):
	filepath = os.path.join(source_folder, filename)

	if os.path.isfile(filepath):
		name, ext = os.path.splitext(filename)
		ext = ext.lower()

	# Add date prefix to filename
	date_prefix = datetime.now().strftime("%Y%m%d")
	new_name = f"{date_prefix}_{name}{ext}"

	# Decide where to move the file
	moved = False
	for folder, extensions in folder.items():
		if ext in extensions:
			shutil.move(filepath, os.path.join(destination_folder, folder, new_name))
			moved = True
			break
	if not moved:
		shutil.move(filepath, os.path.join(destination_folder, "others", new_name))
	print(f"Moved and renamed: {filename} -> {new_name}")
