# Directory-Automation
It contains scripts for directory automation tasks like

1-automation script which accept directory name and file extension from user and displays all
files with that extension.
Usage : DirectoryFileSearch.py “Demo” “.txt”
Demo is name of directory and .txt is the extension that we want to search.

2-automation script which accept directory name and two file extensions from user and
renames all files with first file extension with the second file extenntion.
Usage : DirectoryRename.py “Demo” “.txt” “.doc”
Demo is name of directory and .txt is the extension that we want to search and rename
with .doc.
After execution this script each .txt file gets renamed as .doc.

3-automation script which accept two directory names and copies all files from first directory
into second directory. Second directory should be created at run time.
Usage : DirectoryCopy.py “Demo” “Temp”
Demo is name of directory which is existing and contains files in it. We have to create new
Directory as Temp and copy all files from Demo to Temp.

4-automation script which accept two directory names and one file extension and copies all
files with the specified extension from first directory into second directory. Second directory
should be created at run time.
Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe”
Demo is name of directory which is existing and contains files in it. We have to create new
Directory as Temp and copy all files with extension .exe from Demo to Temp.
