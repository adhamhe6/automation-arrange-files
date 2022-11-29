import imp
import os
import shutil
import pathlib
import glob
import magic
import schedule
import time

path = "downloads"

os.chdir(path)      #Go inside path

#List files in path
extensions = []
for file in os.listdir('.'):
    filename, file_extension = os.path.splitext(file)
    #print(filename, '    ', file_extension)
    if file_extension not in extensions:
        extensions.append(file_extension)
print(extensions)


#to show extension of every file
#magic.from_file(file)

['.jpg', '.jfif', '.txt', '.png', '.mp4']


folders = ['Images', 'Files', 'Videos']
for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)

for file in os.listdir('.'):
    filename, file_extension = os.path.splitext(file)
    #print(filename, '    ', file_extension)
    
    if file_extension in ['.jpg', '.jfif', '.png']:
        shutil.move(file, 'Images')
        print(f'Moving File: {file}')

    elif file_extension in ['.txt']:
        shutil.move(file, 'TxtFiles')
        print(f'Moving File: {file}')

    elif file_extension in ['.mp4']:
        shutil.move(file, 'Videos')
        print(f'Moving File: {file}')


def arranged():
    folders = ['Images', 'Files', 'Videos']
    for folder in folders:
        if not os.path.exists(folder):
            os.mkdir(folder)

    mydict = {
        'Files': ['.doc','.docx','.pdf','.xls','.txt', '.rar'],
        'Images': ['.jpg','.png','.gif','.jfif'],
        'Videos': ['.mp4']
    }

    for destination, extensions in mydict.items():
        for ext in extensions:
            for file in os.listdir('.'):
                if any(file.endswith(s) for s in extensions):
                    print(file)
                    shutil.move(file, destination)

schedule.every().day.at('00:00').do(arranged)

while 1:
    schedule.run_pending()
    time.sleep(1)


#to output all extensions 
for file in os.listdir('.'):
    ext = pathlib.Path(file).suffix
    #print("File Extension: ", file_extension)

#/d/automation/downloads
source = '.'
mydict = {
    'Images': ['jpg','png','gif','.jfif'],
    'Files': ['doc','docx','pdf','xls','.txt'],
    'Videos': ['.mp4']
}

for destination, extensions in mydict.items():
    for ext in extensions:
        for file in glob.glob(source + '*.' + ext):
            print(file)
            shutil.move(file, destination)   
