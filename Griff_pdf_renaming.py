import os
import regex as re
import Pouldard.Griff_wip_REGEX as griff
Pdf_to_rename_dir = r"C:\TEMP\Pouldard\pdf_to_rename_dir"

def get_pdf_paths(folder):
    return(os.path.join(folder, file)
        for file in os.listdir(folder))

new_re_list = []
for item in griff.re_list:
       new_item = re.sub(r"\n"," ", item).strip() +".pdf"
       new_re_list.append(new_item)

print(new_re_list)



Paths_joined=[]

for file in new_re_list :
    new_path = os.path.join(Pdf_to_rename_dir, file)
    Paths_joined.append(new_path)
print(Paths_joined)


for a,b in zip (get_pdf_paths(Pdf_to_rename_dir), Paths_joined):
    os.rename(a, b)






