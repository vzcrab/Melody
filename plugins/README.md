# 插件

MASAP系统中位于功能层.

## apk_parse3

[原仓库](https://github.com/itomsu/apk_parse3)

安装
```
python setup.py install
```

具体用法参见 [apk_parse3/README](https://github.com/itomsu/apk_parse3)

选取字段信息

| 字段           | 含义                | 方法/属性                         | 返回类型(Python) |
| -------------- | ------------------- | --------------------------------- | ---------------- |
| package        | BundleId(应用id)    | apkf.package / apkf.get_package() | str              |
| file_md5       | 应用md5             | apkf.file_md5                     | str              |
| cert_md5       | 证书md5             | apkf.cert_md5                     | str              |
| file_size      | 应用大小            | apkf.file_size                    | int              |
| androidversion | 安卓版本            | apkf.androidversion               | dict             |
| sdk_version    | SDK版本             | apkf.get_target_sdk_version()     | int              |
| libraries      | 应用依赖库          | apkf.get_libraries()              | list             |
| files          | 所有文件名称        | apkf.get_files()                  | list             |
| files_types    | 文件名称及对应类型  | apkf.get_files_types()            | dict             |
| main_activity  | 获取mainActivity    | apkf.get_main_activity()          | str              |
| activities     | 获取所有activity    | apkf.get_activities()             | list             |
| services       | 获取所有servers     | apkf.get_services()               | list             |
| receivers      | 获取所有receivers   | apkf.get_receivers()              | list             |
| providers      | 获取所有providers   | apkf.get_providers()              | list             |
| permissions    | 获取所有permissions | apkf.get_permissions()            | list             |
| icon           | 应用图标            | apkf.parse_icon(icon_path='/tmp') | 存入指定目录     |
| cert_text      | 获取证书内容        | apkf.cert_text                    |                  |
