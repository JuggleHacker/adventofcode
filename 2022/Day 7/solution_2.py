# from functools import cache
#
# @cache
#
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(10000)

cache = {}
def size(directory_name, contents_dictionary):
    if directory_name in cache:
        return cache[directory_name]
    else:
        directory_size = 0
        subdirs = []
        for item in contents_dictionary[directory_name]:
            path = item.split('|')
            short_item = path[-1]
            if short_item[:4] == 'dir ':
                path_start = '|'.join(path[:-1])
                foo = path_start + '|' + short_item[4:]
                subdirs.append(foo)
            else:
                directory_size += int(short_item.split(' ')[0])
        for subdir in subdirs:
                directory_size += size(subdir, contents_dictionary)
        cache[directory_name] = directory_size
        return directory_size

# with open('my_example_input.txt') as f:
# with open('example_input.txt') as f:
with open('input.txt') as f:
    data = f.readlines()
    contents = {}
    i = 0
    path = []
    while i < len(data):
        if data[i] == "$ cd ..\n":
            path = path[:-1]
            i += 1
        elif data[i][:4] == "$ cd":
            to_add = data[i][5:-1]
            path.append(to_add)
            i += 1
        elif data[i][:4] == "$ ls":
            directory = '|'.join(path)
            found = 1
            while data[i+found][0] != "$":
                to_add = directory + '|' + data[i + found][:-1]
                contents[directory] = contents.get(directory, []) + [to_add]
                found += 1
                if i + found >= len(data):
                    break
            i += found

    dirs_to_delete = []
    print(contents)
    unused_space = 70000000 - size('/', contents)
    for dir in contents:
        dir_size = size(dir, contents)
        if dir_size + unused_space> 30000000:
            dirs_to_delete.append(dir_size)
    dirs_to_delete.sort()
    print(dirs_to_delete[0])
