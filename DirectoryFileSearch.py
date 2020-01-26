import os;
import sys;

def DirectoryWalk(dirpath,ext):
	if not os.path.isdir(dirpath):
		print("Sorry it is not a directory Or directory not found");
		return;

	for folders,subfolders,files in os.walk(dirpath):
		for fname in files:
			extension=os.path.splitext(fname);
			if ext==extension[1]:
				print("File is",fname);


def main():
	if len(sys.argv)<2:
		print("Invalid number of arguments\nUse -h or -u");
		return ;
	if sys.argv[1]=="-h" or sys.argv[1]=="-H":
		print("This application displays files of input extxension");
		return ;
	if sys.argv[1]=="-u" or sys.argv[1]=="-U":
		print("python filename.py foldername extension");
		return ;
	if len(sys.argv)!=3:
		print("Invalid number of arguments\nUse -h or -u");
		return ;

	try:
		DirectoryWalk(sys.argv[1],sys.argv[2]);
	except Exception as A:
		print("Exception occured ",A);

if __name__=="__main__":
	main();