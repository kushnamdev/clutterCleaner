
'''

Author --> Kush Namdev ;
Gmail --> kushnamdev23@gmail.com ;

It is a script which can clear your clutter in seconds ,
you can add more functions to it . 
It is free to use and modify according to your preferences ..

you can add more file types .



'''

import os 


def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername, files):
    for file in files:
        os.replace(file,f"{foldername}/{file}")



        
files = os.listdir()
files.remove("main.py")

print(files)

createIfNotExists('Images')
createIfNotExists('Docs')
createIfNotExists('Media')
createIfNotExists('Others')
createIfNotExists('Zipfies')

imgExts = [".png", ".jpeg", ".jpg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]
print(images)

docExts = [".txt", ".doc", ".docx", ".odt", ".pdf"]
docs = [ file for file in files if os.path.splitext(file)[1].lower() in docExts]
print(docs)

mediaExts = [".3gp", ".mp3", ".flv", ".mp4"]
medias = [ file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

zipExts = [".zip", ".rar", ".7z", ".zipx", ".tar.gz", ".pkg", ".rpm"]
zipfiles = [file for file in files if os.path.splitext(file)[1].lower() in zipExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and (ext not in zipExts ) and os.path.isfile(file):
        others.append(file)

print(others)

move('Images', images)
move('Docs', docs)
move('Media', medias)
move('Others', others)
move('Zipfiles', zipfiles)


