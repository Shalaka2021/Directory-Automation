import os;
import sys;

def ChangeExtension(dirpath,before_ext,after_ext):
	if not os.path.isdir(dirpath):
		print("Sorry it is not a directory Or directory not found");
		return;

	for folder,subfolders,files in os.walk(dirpath):
		for fname in files:
			fname=os.path.join(folder,fname);
			real=os.path.splitext(fname);
			
			if before_ext==real[1]:
				name=real[0];
				os.rename(fname,name+after_ext);

def main():
	if len(sys.argv)<2:
		print("Invalid number of arguments\nUse -h or -u");
		return ;
	if sys.argv[1]=="-h" or sys.argv[1]=="-H":
		print("This application changes file extension");
		return ;
	if sys.argv[1]=="-u" or sys.argv[1]=="-U":
		print("python filename.py foldername .extension_before .extension_after");
		return ;
	if len(sys.argv)!=4:
		print("Invalid number of arguments\nUse -h or -u");
		return ;
	

	try:
		ChangeExtension(sys.argv[1],sys.argv[2],sys.argv[3]);
	except Exception as A:
		print("Exception occured ",A);

if __name__=="__main__":
	main();