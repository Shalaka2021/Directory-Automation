import sys;
import os;
import shutil;

def DirectoryCopy(source,destination):
	if not os.path.isdir(destination):
		os.mkdir(destination);

	for folder,subfolders,files in os.walk(source):
		for fname in files:
			fname=os.path.join(folder,fname);
			newpath=shutil.copy(fname,destination);

def main():
	if len(sys.argv)<2:
		print("Invalid number of arguments\nUse -h or -u");
		return ;
	if sys.argv[1]=="-h" or sys.argv[1]=="-H":
		print("This application copies files from source directory to destination directory");
		return ;
	if sys.argv[1]=="-u" or sys.argv[1]=="-U":
		print("python filename.py foldername1 foldername2");
		return ;
	if len(sys.argv)!=3:
		print("Invalid number of arguments\nUse -h or -u");
		return ;

	try:
		DirectoryCopy(sys.argv[1],sys.argv[2]);
	except Exception as A:
		print("Exception occured ",A);

if __name__=="__main__":
	main();