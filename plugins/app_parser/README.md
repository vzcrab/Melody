# app_parser

## Build

第一步
```
git clone https://github.com/iosmosis/app_parser
```

第二步
```
go build

```
接着会生成对应架构的可执行文件app_parser

## Usage

```
./app_parser app_path [icon_save_path]
```
## Example

```
./app_parser ~/Downloads/XposedInstaller_3.1.5.apk
{"Name":"Xposed Installer","BundleID":"de.robv.android.xposed.installer","Version":"3.1.5","SdkVersion":"43","Size":"3105672","Icon":"de.robv.android.xposed.installer/icon.png"}
# or
 ./app_parser ~/Downloads/XposedInstaller_3.1.5.apk ~/Downloads/a 
 {"Name":"Xposed Installer","BundleID":"de.robv.android.xposed.installer","Version":"3.1.5","SdkVersion":"43","Size":"3105672","Icon":"/Users/ios/Downloads/a/icon.png"}
```

结果呈现方式：json{应用名称，应用id，应用版本,安卓SDK版本，应用大小，应用图片保存路径}

## Bug
目前还未解决获取到ipa文件的icon图标
