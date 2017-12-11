import os
import textract
# PART I : Convert a bunch of pdf files to text
test_dir = r"/mnt/c/TEMP/test/"

for j, file in enumerate(os.listdir(test_dir)):
    pdf = textract.process(str(os.path.join(os.path.abspath(test_dir), file)))  #

    with open("input{}.txt".format(j), 'w') as f:
        f.write(str(pdf,'utf8'))

print('this is done well')


#PART II : extract title with regex &Copyright

"""
pattern = re.compile ('(([A-Z]\w+)\s?)+(.?|.+)\sCopyright')
for input in os.listdir('.'):
    with open(str(input),'r',encoding='utf-8')as f:
        contents = f.read()
        match = pattern.search(contents)

        print(match.group(0))
"""
#TODO USE GLOB FOR IMPORT AND CHANGE LOOK UP FOLDER WARNING PRESENTLY ITS SET TO CURRENT ('.') ligne 19

#PART III Rename and glue first part of this script

