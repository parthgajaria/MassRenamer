import os

print "This script will rename files from one file extension to another"
from_ext = raw_input("Enter the file extension you wish to convert from (ie. jpg): ")
to_ext = raw_input("Enter the file extension you wish to convert to (ie. gif): ")
root_dir = raw_input("Enter the absolute path of the directory which contains the files (ie. D:\Comics): ")
from_ext_len = len(from_ext)
#Look through directory tree
for root, subFolders, files in os.walk(root_dir):
	for file in files:
		if file[-(from_ext_len + 1):] == "." + from_ext:
			os.rename(os.path.join(root,file), os.path.join(root,file[:-(from_ext_len + 1)] + "." + to_ext))
			print "Conversion Successful"