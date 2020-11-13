import os
import sys

import eyed3
import fnmatch

# https://eyed3.readthedocs.io/en/latest/eyed3.html

rootPath = "./"

pattern = '*.mp3' # TODO: will miss all other types: .4a, ...

f = open("books.csv", "w")
err = open("errors.txt", "w")
f.write("Moved,Dir,Artist,Title,Album\n")
 
for root, dirs, files in os.walk(rootPath):
    print(root)
    #print(dirs)
    #print(files)
    
    # no books, just subdirs
    if not files:
        continue
    
    # if i wanted all books
    # for filename in fnmatch.filter(files, pattern):
    
    # only need to look at one book
    books = fnmatch.filter(files, pattern)
    
    err.write("{}\n".format(root))
    
    # either a directory with only sub dirs, or non mp3 files
    if not books:
        print("\tNo valid files found.")
        err.write("\t No valid files found.\n")
        continue
        
    #print(root, books)
    filename = books[0]
    filepath = os.path.join(root, filename)
    #print(filepath)
    try:
        audioFile = eyed3.load(filepath)
        #print(audioFile)
        if audioFile != None and audioFile.tag != None:      
            #print(audioFile.tag.artist)
            #print(audioFile.tag.title)
            #print(audioFile.tag.album)
            dirName = root.split('/')[-1]
            f.write(",\"{}\",\"{}\",\"{}\",\"{}\"\n".format(dirName, audioFile.tag.artist, audioFile.tag.title, audioFile.tag.album))
            
            #f.write("\t{}\n".format(audioFile.tag.artist))
            #f.write("\t{}\n".format(audioFile.tag.title))
            #f.write("\t{}\n".format(audioFile.tag.album))
        else:
            print("No Tag Found")
            err.write("\tNo Tag Found\n")
    except IOError as error:
        print("IOError: {0}".format(error))
    except:
        print("Unexpected error:", sys.exc_info()[0])

f.close()
        
   
