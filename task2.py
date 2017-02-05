import re
import string
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def find(filenames, paragraph):
    for files in filenames:
        with open(files) as textfile:
                content = textfile.read()

                content = re.sub('\xef\xbf\xbds?','', content)
                content = content.split('\n\n')
                results = process.extractOne(paragraph, content)
                if results[1] <= 90:
                    print 'This paragraph is not from', files
                else:
                    print 'This paragraph is from' ,files
                    return files
                print files, results[1], results

def get_author(text):
    with open(text) as textfile:
            content = textfile.read()
            authorList = []
            authorLine = re.search(r'\bAuthor(.*)', content).group()
            print authorLine
            authorList = authorLine.split(':')
            author = authorList[1]
            author = author.strip()
            return author


if __name__ == '__main__':
    print fuzz.ratio("this is a test", "this is a test!")
    text = find(['alice.txt','tomsawyer.txt', 'frank.txt',  'dracula.txt'], 'At this the whole pack rose up into the air, and came flying down upon yo yo yo i know her: she gave a little scream, half of fright and half of anger, and tried to beat them off, and found herself lying on the bank, with her head in the lap of her sister, who was gently bru')
    print text
    print get_author(text)
