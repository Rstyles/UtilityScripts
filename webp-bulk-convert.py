import os;

input_dir = os.getcwd();

dir_list = os.listdir(input_dir);

for i in dir_list:
	os.system("cwebp -q 80 " + i + " -o " + i + "converted.webp" );
	os.remove(i);