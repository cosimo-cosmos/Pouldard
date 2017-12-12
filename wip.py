import os
import glob
import shutil
import re

from tqdm import tqdm
#import textract
# PART I : Convert a bunch of pdf files to text
#test_dir = r"/mnt/c/TEMP/test/"
test_dir = r"C:\TEMP\test"
new_path = r"C:\TEMP\re_inputs"
base_path=os.path.abspath(test_dir)
#for j, file in enumerate(os.listdir(test_dir)):
    #print("file --> {} num: {}".format(file, j))
"""
    pdf = textract.process(str(os.path.join(os.path.abspath(test_dir), file)))  #

    with open("input{}.txt".format(j), 'w') as f:
        f.write(str(pdf,'utf8'))

print('this is done well')
"""


#PART II : extract title with regex &Copyright
if not os.path.exists(new_path):
    os.mkdir(new_path)
    for input in glob.glob('C:\TEMP\input*'):
        shutil.copy(input, new_path)
#print(os.listdir(new_path))



files_list = os.listdir(new_path)

ordered_files =  sorted(files_list, key=lambda x: (int(re.sub('\D','',x)),x))
print(ordered_files)










pattern = re.compile ('(([A-Z]\w+)\s?)+(.?|.+)\s[Cc]opyright')
#pattern = re.compile('[Cc]opyright')
os.chdir(new_path)
for i, input in tqdm(enumerate((os.listdir('.')))):
    try:
        with open(str(input),'r',encoding='utf-8')as f:
            contents = f.read()
            match = pattern.search(contents)

            print('{} --> {}'.format(match.group(0), i))
    except AttributeError:
        print('{} --> where hide the error'.format(i))
        continue


#TODO USE GLOB FOR IMPORT AND CHANGE LOOK UP FOLDER WARNING PRESENTLY ITS SET TO CURRENT ('.') ligne 19

#PART III Rename and glue first part of this script



