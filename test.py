import os
import subprocess


def test1():
    files = os.listdir("test")
    ifiles = [file for file in files if "wc" in file and file.endswith(".in")]
    ofiles = [file for file in files if "wc" in file and file.endswith(".out")]
    i=0
    for i in range(0,len(ifiles)):
        path = os.path.join("test", ifiles[i])
        output = subprocess.check_output(['python', os.path.join('prog','wc.py'), path], universal_newlines=True)
        
        expfile = os.path.join("test", ofiles[i])
        with open(expfile) as f:
            expected_output = f.read()
        
        if expected_output.strip() == output.strip():
            # print(f"{expected_output}\n-----------------------\n{output}")
            print("Success!!")

def test2():
    files = os.listdir("test")
    ifiles = [file for file in files if "gron" in file and file.endswith(".in")]
    print(ifiles)
    ofiles = [file for file in files if "gron" in file and file.endswith(".out")]
    for i in range(0,len(ifiles)):
        path = os.path.join("test", ifiles[i])
        output = subprocess.check_output(['python', os.path.join('prog','gron.py'), path], universal_newlines=True)
        
        expfile = os.path.join("test", ofiles[i])
        with open(expfile) as f:
            expected_output = f.read()
        
        if expected_output.strip() == output.strip():
            # print(f"{expected_output}\n-----------------------\n{output}")
            print("Success!!")
        else:
            print(f"{expected_output}\n-----------------------\n{output}")


if __name__ == "__main__":
    test2()