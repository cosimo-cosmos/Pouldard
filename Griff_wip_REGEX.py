import os
import regex as re




Output_dir = r"C:\TEMP\Pouldard\Output_dir"

### with www.it-ebooks.info CURRENT BEST MATCH!!!

#pattern = re.compile (r"(?P<info>www.it-ebooks.info)(?P<title>([A-Z]\w+\s)+)")

#with a lookbehind Warning: <= = "< + "=" its a ligature

pattern = re.compile (r"(?<=www.it-ebooks.info)(?P<title>([A-Z]\w+\s)+)")




#1)old pattern
#pattern = re.compile (r"(([A-Z]\w+)\s?)+(.?|.+)\s[Cc]opyright")

####
#pattern = re.compile(r"(?P<title>(\b[A-Z].+?\b)+?\s??)(?P<cop>[Cc]opyright)")


#pattern with 'Python' keyword
#pattern = re.compile(r'(\b[A-Z].+?\b)+?\s??Python|[Cc]opyright')
#pattern = re.compile(r'(\b[A-Z].+?\b)+?\s??Python')


os.chdir(Output_dir)
logging = 'C:\TEMP\Pouldard\log_file.txt'
if os.path.isfile(logging):
    os.remove(logging)
for i, output in enumerate(sorted(os.listdir('.'), key=lambda x: (int(re.sub('\D','',x)),x))):
    try:
        with open(str(output),'r',encoding='utf-8')as f:
            contents = f.read()
            match = pattern.search(contents)



            with open(logging, 'a', encoding='utf8') as log:
                log_file = log.write('{} --> {}'.format(match.group(), i) + '\n')


            print('{} --> {}'.format(match.group(), i))


    except AttributeError:
        print('{} --> where hide the error'.format(i))

print('THE END')





