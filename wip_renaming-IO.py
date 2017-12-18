import os
import re

Output_dir = r'C:\TEMP\Pouldard\Output_dir'

def get_pdf_paths(folder):
    return(os.path.join(folder, file)
        for file in os.listdir(folder))

fullpaths =[]
with open('Input_as_coming_list.txt', 'r') as f:

    for item in f:
        fullpaths.append(item)

    print(len(fullpaths))
    print(fullpaths)

basenames = []
for path in fullpaths:
    basenames.append(os.path.basename(path))

newlist = []
for str in basenames:

    new_str = re.sub('input(\d+)(\.pdf)','output\g<1>.txt', str)
    newlist.append(new_str.strip())
Paths_joined=[]
print(newlist)
for file in newlist :
    new_path = os.path.join(Output_dir, file)
    Paths_joined.append(new_path)
print(Paths_joined)




for a,b in zip (get_pdf_paths(Output_dir), Paths_joined):
    os.rename(a, b)



