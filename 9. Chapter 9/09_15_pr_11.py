#renaming file name

import os

oldname = "sample4.txt"
newname = "renamed_by_python.txt"
with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:               #contents of sample4.txt wull be copies in new file. before renaming.
    f.write(content)

os.remove(oldname)     #removes the old file.