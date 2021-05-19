import inspect
import os
import re


class Regex:
    # 1001.文件名提取
    file_name_pattern = re.compile(r'apk_sources/(.*?\.apk)')
    # 1002.包名检测
    package_pattern = re.compile(r'package="(.*?)"')
    # 01003.主活动检测
    main_activity_pattern = re.compile(r'activity.*?android:name=\"(.*?)\".*intent-filter.*MAIN', re.S)
    # 01004.最小SDK检测
    min_sdk_pattern = re.compile(r'minSdkVersion: \'(\d*)\'')
    # 01005.目标SDK检测
    target_sdk_pattern = re.compile(r'targetSdkVersion: \'(\d*)\'')
    # 1006.权限信息检测
    permission_pattern = re.compile(r'android\.permission\.(\w*)', re.M)
    # 1007 - 1010.四大组件检测
    activity_pattern = re.compile(r'<activity.*?android:name="(.*?)"', re.S)
    service_pattern = re.compile(r'<service.*?android:name="(.*?)"', re.S)
    receiver_pattern = re.compile(r'<receiver.*?android:name="(.*?)"', re.S)
    provider_pattern = re.compile(r'<provider.*?android:name="(.*?)"', re.S)
    # 1011.权限组检测
    permission_group_pattern = re.compile(r'(<permission.*?android:permissionGroup="(.*?)".*?>)', re.S)
    # 1012.protectionLevel检测
    protection_level_pattern = re.compile(r'(<permission.*?android:protectionLevel="(.*?)".*?>)', re.S)
    # 1013.SharedUserId检测
    shared_user_id_pattern = re.compile(r'<manifest.*?android:sharedUserId="android.uid.system".*?>', re.S)
    # 1014.Allowbackup检测
    allowbackup_pattern = re.compile(r'<application.*android:allowBackup="true".*?>')
    # 1015.Debuggable检测
    debuggable_pattern = re.compile(r'<application.*android:debuggable="true".*?>')

    # 1016.Provider:grant-uri-permission属性检测
    provider_grant_uri_permission_pattern = re.compile(r'android:grantUriPermissions="true"', re.S)

    # 1017.Intent Scheme vuln_text漏洞攻击检测
    is_exist_intent_parseuri_pattern = re.compile(r'Intent +(\w+) *= *Intent\.parseUri', re.M)

    # 1018.Debug或Test敏感测试组件泄露检测
    debug_test_pattern = re.compile(r'debug|test', re.M | re.I)

    # 1019.WebView潜在XSS攻击检测
    webview_setjs_pattern = re.compile(r'\S+\.setJavaScriptEnabled\(true\)', re.M)
    # 1020.WebView File域同源策略绕过漏洞检测
    webview_setfile_pattern = re.compile(r'\S+\.setAllowFileAccess\(true\)', re.M)
    # 1021.webview密码明文存储漏洞检测
    webview_setpw_pattern = re.compile(r'\S+\.setSavePassword\(true\)', re.M)

    # 1022.主机名弱校验漏洞检测
    hostname_pattern = re.compile(
        r'HostnameVerifier.*?new.*?boolean\s+verify\s*?\(String.*?SSLSession \w+\)\s*?{\s*?return true;\s*?}.*?}', re.S)

    # 1023.中间人攻击漏洞检测
    allow_all_hostname_pattern = re.compile(r'(\S*ALLOW_ALL_HOSTNAME_VERIFIER\S*);', re.M)
    # 1024.WebView不校验证书漏洞检测
    webview_ignore_ssl_error_pattern = re.compile(r'new WebViewClient.*?onReceivedSslError.*?handler\.proceed', re.S)

    # 1025.WebView组件系统隐藏接口未移除漏洞
    webview_is_defined_pattern = re.compile(r'WebView (\w*)\b.*;', re.M)

    # 1026.SSL连接检测
    http_vuln_text_pattern = re.compile(r'"(http://.*?)"', re.M)

    # 1027.SSL不安全组件检测
    # SSLCertificateSocketFactory.getInsecure()是静态方法
    ssl_get_insecure_pattern = re.compile(r'^\s*(.*SSLCertificateSocketFactory\.getInsecure.*);', re.M)

    # 1028.HttpHost检测
    # java.lang.Object -> org.apache.hc.core5.http.HttpHost
    http_host_pattern = re.compile(r'^\s*(.*HttpHost.DEFAULT_SCHEME.*);', re.M)

    # 1029.DES弱加密风险检测
    des_pattern = re.compile(r'^\s*(.*DES/\w{3}/.+Padding.*);', re.M)
    # 1030.不安全的密钥长度风险检测
    unsafe_key_pattern = re.compile(r'KeyPairGenerator\s+(\w+)\s*=\s*KeyPairGenerator\.getInstance.*;', re.M)
    # 1031.AES-ECB弱加密风险检测.
    aes_ecb_pattern = re.compile(r'^\s*(.*AES/ECB/.+Padding.*);', re.M)
    # 1032.IVParameterSpec不安全初始化向量检测
    iv_parameter_spec_pattern = re.compile(r'new\s+IvParameterSpec\((\w+)\)', re.M)
    # 1033.RSA中不使用Padding风险检测
    rsa_no_padding_pattern = re.compile(r'^\s*(.*RSA/\w+/NoPadding.*);', re.M)

    # 1034.剪贴板敏感信息泄露风险检测
    clip_data_pattern = re.compile(r'\s*(.*ClipData\.newPlainText.*);', re.M)
    # 1035.Intent敏感数据泄露风险检测
    # intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
    intent_setflag_pattern = re.compile(r'\s*(.*setFlags.*FLAG_ACTIVITY_NEW_TASK.*);', re.M)
    # 1036.PendingIntent误用风险
    pending_intent_pattern = re.compile(r'(PendingIntent\.get(Service|Activity|Broadcast)\(\w*, \w*, (\w*).*\))')
    # 1037.密钥硬编码
    # String str = "keyTest0755";
    # byte[] key = str.getBytes();
    # SecretKey secretKey = new SecretKeySpec(key, "AES");
    secretkeyspec_pattern = re.compile(r'new\s+SecretKeySpec\((\w+),.*\)')
    # 1038.BASE64安全检测
    base64_pattern = re.compile(r'"(([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==))"', re.M)

    # 1039.日志泄露风险检测
    # Log.v、Log.d、Log.e、Log.i、Log.w、Log.f、Log.s
    log_pattern = re.compile(r'\s*(Log\.[vdeiwfs].*);', re.M)
    # 1040.安全相关的函数检测
    safe_function_pattern = re.compile(
        r'(\w*(encrypt|decrypt|encod|decod|aes|sha1|sha256|sha512|md5|decode|encode)\w*\(.*?\))', re.M | re.I)
    # 1041.安全相关的类检测
    safe_class_pattern = re.compile(r'encrypt|decrypt|encod|decod|aes|sha1|sha256|sha512|md5|decode|encode',
                                    re.M | re.I)
    # 1042.运行命令检测
    getruntime_pattern = re.compile(r'Runtime\s+(\w+).*Runtime\.getRuntime\(\);', re.M)
    # 1043.Native Library加载检测
    load_library_pattern = re.compile(r'(System.loadLibrary\("\w+\.so"\));', re.M)
    # 1044.外部动态加载DEX检测
    # dexclassloader_pattern = re.compile(r'DexClassLoader.*=\s*?new\s+DexClassLoader\s*?\(.*?\);', re.S)
    dexclassloader_pattern = re.compile(r'\s*(.*=\s*?new\s+DexClassLoader\s*?\(.*?\));', re.M)
    # 1045.root代码检测
    root_exec_pattern = re.compile(r'\s*(.*\w+\.exec\s*\(\"su"\));', re.M)
    # 1046.获取IMEI和Device ID敏感信息代码检测
    getdeviceid_pattern = re.compile(r'\s*(.*getDeviceId.*);')
    # 1047.获取AndroidID敏感信息代码检测
    secure_androidid_pattern = re.compile(r'\s*(Secure\.getString.*Secure\.ANDROID_ID.*);', re.M)
    # 1048.发送SMS敏感代码检测
    send_sms_pattern = re.compile(r'\s*(.*send(Text|Data|Multimedia)Message\(.*\));', re.M)
    # 1049.文件删除代码检测
    getfile_pattern = re.compile(r'File\s+(\w+).*new\s+File.*;', re.M)
    # 1050.signature代码检测
    signature_pattern = re.compile(r'(\w+\s*=\s*\w+\.getPackageInfo.*?PackageManager\.GET_SIGNATURES\).*?);', re.S)
    # 1051.Fragment注入漏洞CVE-2013-6271检测
    isvalid_fragment_pattern = re.compile(
        r'extends PreferenceActivity.*boolean isValidFragment.*?{\s*return true;\s*?}', re.S)
    # 1052.随机数生成漏洞
    set_seed_pattern = re.compile(r'\s*(.*\.setSeed.+);', re.M)


Matching_rules = [i for i in dir(Regex) if "__" not in i]  # 保存Regex里的正则表达式
L = []  # 定义全局变量保存.java文件所在路径


# def file_name(file_dir):
#     for root, dirs, files in os.walk(file_dir):
#         for file in files:
#             if re.match('(.*?)java$', str(file)):
#                 L.append(os.path.join(root, file))
#     return L


def get_line(path, str):
    with open(path, "r", encoding="utf-8", errors='ignore') as f:
        count = 0
        for line in f.readlines():
            if str in line:
                return count
            count += 1


def get_result(path, vuln_id,rule):
    context_list = []
    new_data = []
    with open(path, "r", encoding="utf-8", errors='ignore') as f:
        source = f.read()
        result = re.finditer(rule, source)
    for res in result:
        vuln_text = res.group()
        dict = {}
        line = get_line(path, vuln_text)
        dict["line"] = line
        dict["vuln_text"] = vuln_text.strip()
        dict["vuln_id"] = vuln_id
        context_list.append(dict)
    for x in context_list:
        if x not in new_data:
            new_data.append(x)
    return new_data


def get_vuln_text(path_list, vuln_id,rule):
    match_list = []
    for path in path_list:
        match_result = {}
        res = get_result(path, vuln_id,rule)
        if res:
            match_result["path"] = path
            match_result["value"] = res
            match_list.append(match_result)
    return match_list


def vuln_match_all(path):
    vuln_list = []
    Match_start = 1001  # 漏洞正则匹配表达式开始编号
    for i in range(len(Matching_rules)):
        rule = getattr(Regex, Matching_rules[i])
        vuln_id = Match_start - 1
        res = get_vuln_text(path, vuln_id,rule)
        Match_start += 1
        if len(res) != 0:
            vuln_list.append(res)
            # print(res)
    return vuln_list
