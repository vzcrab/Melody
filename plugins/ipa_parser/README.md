# ipa Parser
## Install
未测试
```bash
  python setup.py install
```

## Usage
```python
from ipa_parser import *
# load ipa path
ipa_path = r'test/FlappyBird_v1.2.ipa'
# init
ipa = IosIpa(ipa_path=ipa_path)
# dump json for ipa
print_info(ipa)
# dump all icon apth
# print(ipa.iconsArray)

# if want to remove parser_tmp_file ,you can
#ipa.delete_tmp()
```

# Method


| 字段           | 含义                | 方法/属性                         | 返回类型(Python) |
| -------------- | ------------------- | --------------------------------- | ---------------- |
| ipa_name        | 当前ipa的文件名      | ipa.name                          | str              |
| bundle_id       | BundleId(应用id)    | ipa.buildInfo.bundleId            | str              |
| version_num     | 应用版本             | ipa.buildInfo.versionNumber       | str              |
| build_num      | 应用内部版本           | ipa.buildInfo.buildNumber        | str              |
| icon_path       | 应用图标路径          | ipa.get_icon_files()              | list             |
|                  | 删除临时文件（包含图片路径）| ipa.delete_tmp()            | None              |
| tmp_path         | 获取tmp文件路径          | ipa.tmp_dir                   | str             |
| infoplist_filepath  | 获取info.list文件路径 |ipa.infoplist_filepath         | str            |
|               | json输出基本数据  | print_info(ipa)                     | dict             |