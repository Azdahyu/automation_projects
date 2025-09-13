# **File Sorting and Renaming Automation**
This Python script automates the process of renaming and organizing files. It scans a source folder, renames each file with a data prefix, and sorts them into destination folders based on file type.

## **Features**
- Renames files with today's date (e.g., 20250913_report.pdf)
- Sorts files into categories: images, documents, and others.
- Automatically creates destination folders if they don't exist.
- Easily customizable to add more file types and categories.

## **Requirements**
- Python 3.6+ (f-strings are used)
- Works on Windows, macOS, and Linux.

## **How to Use**
1. Clone/download this repo or copy the script.
2. Update the folder paths in the script.
```
python

source_folder = r"C:\Users\Tina\Downloads"
destination_folder = r"C:\Users\Tina\Downloads"
```
  
3. Run the script:
```
bash
python sort_files.py
```
  
4. Your files will be renamed and moved into:
- Sorted/images/
- Sorted/documents/
- Sorted/others/

## **Customization**
- To add new categories, edit the *folders* dictionary:
```
python

folders = {
	"images": [".jpg",".jpeg",".png",".gif"]
	"documents": [".pdf",".docx",".txt",".xlsx"]
	"videos": [".mp4",".mov",".avi"]
	"others": []
}
```

- Any file type not listed will be placed into *others*.

## **Example**
Before:
```
markdown
Downloads/
	report.pdf
	photo.png
	notes.txt
```
  
After running:
```
markdown

Sorted/
	documents/
		20250913_report.pdf
		20250913_notes.txt
	images/
		20250913_photo.png
```
  

