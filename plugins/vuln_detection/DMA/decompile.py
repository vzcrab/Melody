from subprocess import call
from pathlib import Path
import platform
import os
import json


def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            list_name.append(file_path)


def decompile(base_path, path, out_path):
    system = platform.system()
    file_output = open("result", "w")
    if system == "Windows":
        call(base_path+"\\plugins\\vuln_detection\\DMA\\lib\\jadx.bat --log-level error --deobf --deobf-parse-kotlin-metadata -d " + out_path + " " + path,
             shell=True,
             stdout=file_output)
    else:
        call(base_path+"/plugins/vuln_detection/DMA/lib/jadx --log-level error --deobf --deobf-parse-kotlin-metadata -d " + out_path + " " + path,
             shell=True,
             stdout=file_output)
    file_output.close()
    # check decompile status
    with open("result", "r", encoding="utf-8") as f:
        res = f.read()
        if "done" in res:
            path_list = []
            listdir(out_path, path_list)
            return path_list
        else:
            err = res.split("\n")
            return err


if __name__ == '__main__':
    base_path = r"/Users/ios/Desktop/DLU/Melody"
    out_path = r"/Users/ios/Downloads/out"
    file_path = r"/Users/ios/Downloads/ReflectMaster-3.5.3.apk"
    result = decompile(base_path, file_path, out_path)
    print(result)
