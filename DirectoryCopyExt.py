import os;
import sys;
import shutil;

def DirectoryCopyExt(source,destination,ext):
	if not os.path.isdir(destination):
		os.mkdir(destination);
	for folder,subfolder,files in os.walk(source):
		for fname in files:
			fname=os.path.join(folder,fname);
			fullname=os.path.splitext(fname);
			#print(fullname);
			if ext==fullname[1]:
				shutil.copy(fname,destination);


def main():
	if len(sys.argv)<2:
		print("Invalid number of arguments\nUse -h or -u");
		return ;
	if sys.argv[1]=="-h" or sys.argv[1]=="-H":
		print("This application copies files of particular extension from source directory to destination directory");
		return ;
	if sys.argv[1]=="-u" or sys.argv[1]=="-U":
		print("python filename.py foldername1 foldername2 extension");
		return ;
	if len(sys.argv)!=4:
		print("Invalid number of arguments\nUse -h or -u");
		return ;

	try:
		DirectoryCopyExt(sys.argv[1],sys.argv[2],sys.argv[3]);
	except Exception as A:
		print("Exception occured ",A);

if __name__=="__main__":
	main();