import re

bookList = []

bookRecord = re.compile(r"^TITLE(.*\n.*\.)$\n^\w+", re.MULTILINE)
history = open("export.txt", encoding="utf8").read()
records = open("readingList.txt", "w", encoding="utf8")

with records as r:
    for match in bookRecord.finditer(history):
        title = match.group(0)
        bookList.append(title)
        r.write(title + "\n")
r.close()

for i in bookList:
    print(i)
print("You have checked out " + str(len(bookList)) + " books or videos.")
