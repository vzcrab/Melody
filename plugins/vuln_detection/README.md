# Vuln detection

漏洞行为为检测

方法说明

| 方法名称       | 参数           | 输出类型 |
| -------------- | -------------- | -------- |
| decompile      | NULL           | List     |
| status         | NULL           | string   |
| __init __      | path，out_path | NULL     |
| match_url      | NULL           | List     |
| match_vuln_all | NULL           | List     |

### match_vuln_all字段说明
    待补充
### match_url字段说明
    待补充
## Usage
 ```python
    from plugins.vuln_detection.matching import MATCH
    
    out_path = r"/Users/ios/Downloads/out"
    file_path = r"/Users/ios/Downloads/wifi.apk"
    base_path = r"/Users/ios/Desktop/DLU/Melody"
    match = MATCH(base_path, file_path, out_path)

    #match_result = match.match_url()
    #match_result = match.match_vuln_all()
    #print(match_result)
    print(match.status())
```
