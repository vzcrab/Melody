from subprocess import call
from pathlib import Path
import platform
import os
import json


def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path, x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
    return d


def decompile(path, out_path):
    system = platform.system()
    file_output = open("result", "w")
    if system == "Windows":
        call("lib/jadx.bat --log-level error --deobf --deobf-parse-kotlin-metadata -d " + out_path + " " + path,
             shell=True,
             stdout=file_output)
    else:
        call("lib/jadx --log-level error --deobf --deobf-parse-kotlin-metadata -d " + out_path + " " + path, shell=True,
             stdout=file_output)
    file_output.close()
    # check decompile status
    with open("result", "r", encoding="utf-8") as f:
        res = f.read()
        if "done" in res:
            dict = path_to_dict(out_path)
            return dict
        else:
            err = res.split("\n")
            return err


if __name__ == '__main__':
    out_path = r"/Users/ios/Downloads/out"
    file_path = r"/Users/ios/Downloads/ReflectMaster-3.5.3.apk1"
    result = decompile(file_path, out_path)
    print(result)
