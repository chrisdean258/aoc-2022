#!/usr/bin/env python3

class directory:
    def __init__(self, name, parent=None):
        self.parent = parent
        self.name = name
        self.subdirs = {}
        self.files = {}
        self.size = 0
        self.full_size = 0

    def calc_full_size(self):
        self.full_size = self.size
        for d in self.subdirs.values():
            d.calc_full_size()
            self.full_size += d.full_size

    def inspect(self, dirs):
        if self.full_size <= 100000:
            print(self.name, self.full_size)
            dirs.append(self)
        for d in self.subdirs.values():
            d.inspect(dirs)


class command:
    def __init__(self, com):
        self.com = com
        self.output = []


commands = []
with open(0) as f:
    for line in f:
        line = line.strip()
        if line.startswith("$"):
            commands.append(command(line))
        else:
            commands[-1].output.append(line)

cur_dir = None
main_dir = None
for com in commands:
    if com.com == "$ cd ..":
        cur_dir = cur_dir.parent
    elif com.com.startswith("$ cd "):
        name = com.com[5:]
        new_dir = directory(name, cur_dir)
        if cur_dir is None:
            cur_dir = main_dir = new_dir
        else:
            cur_dir = cur_dir.subdirs.setdefault(name, new_dir)
    elif com.com == "$ ls":
        for line in com.output:
            if line.startswith("dir "):
                pass
            else:
                size, _, fn = line.partition(" ")
                size = int(size)
                if fn not in cur_dir.files:
                    cur_dir.size += size
                    cur_dir.files[fn] = size
    else:
        print("error")

smalldirs = []
main_dir.calc_full_size()
main_dir.inspect(smalldirs)
print(sum(d.full_size for d in smalldirs))
