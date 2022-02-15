import io
import re

bookList = []

# Have had encoding issues with something in the text file, so double encoding!
with io.open("readingList.txt", "a", encoding="utf8") as f:
    # Get only the two fields we care about
    for line in open("export.txt", encoding="utf8").readlines():
        if re.search("^AUTHOR", line) is not None:
            author = line.replace(", author.", "")
            bookList.append(author)
            f.write(author)
        elif re.search("^TITLE", line) is not None:
            title = line
            bookList.append(title)
            f.write(title)

for i in bookList:
    print(i)

f.close()
