# DMA

Decompile Mobile Analyze

## Usage
设置好 保存路径和apk文件路径 进行反编译 并返回结果
```python
from decompile import *

if __name__ == '__main__':
    out_path = r"/Users/ios/Downloads/out"
    file_path = r"/Users/ios/Downloads/ReflectMaster-3.5.3.apk"
    result = decompile(file_path, out_path)
    print(result)
```
### result 
if success to decompile, then return reverse's file tree,else return Error dict.

成功返回文件树说明:
- resources 资源文件
  - assets
  - META-INF
  - 等其他资源文件，与基础解析生成文件相同  
- sources  反编译后的源代码文件
  - com 一级包名
    - qingyu 二级包名
    - p000rm 三级包名  等包名
      - xx.JAVA 类：源码文件1
      - Main.JAVA 类：主函数源文件
    
  - xx 依赖包名
    - xxx 依赖 二级包名
     - xxxx.java 依赖源码文件
    
错误示例:
``` json
['ERROR - Incorrect arguments: File not found /Users/ios/Downloads/ReflectMaster-3.5.3.apk1', '']
```
