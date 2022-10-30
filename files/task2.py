import os

with open("ans.txt", "w") as w:
    for current_dir, dirs, files in os.walk("main"):
        for i in files:
            if i[-3:] == '.py':  # if i.endswith(".py"):
                w.write(current_dir + "\n")
                break
