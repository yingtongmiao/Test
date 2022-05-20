from atomicwrites import atomic_write
def checker(func):
    def new_func(a, b):
        if not isinstance(a,str):
            return "File name is not string."
        if not isinstance(b,str):
            return "Writing contents are not string."
        if not a:
            return "File name is empty."
        if not b:
            return "Writing contents are empty."
        return func(a, b)
    return new_func

@checker
def atomicwriting(filename, content):
    try:
        with atomic_write(filename, overwrite=True) as f:
            f.write(content)
            return content
    except:
        return "File name or file path error"



def main():
    print(atomicwriting("writingfile.txt", "Yingtong Miao\nTammy"))
 
if __name__ == '__main__':
    main()
