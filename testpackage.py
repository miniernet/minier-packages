import os
import sys

print("Hello world!")

defapath = sys.argv[1] # First arg is always the defapath
lastpath = os.getcwd()

# Installation
os.chdir(defapath + "/app/modules") # Files in /app/modules are executed if their name is typed.

with open("testpkg.py", "w") as f:
    f.write("print('You just executed the test app!')\n")
    f.close()

os.chdir(lastpath)

print("Installation done!")
