#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os  # file handling
import shutil  # file handling2
import zipfile  # zipping
import re
import json


# --------------------
# Core iOS IPA classes
# --------------------

class IosBuildInfo:

    def __init__(self, bundleId, versionNumber, buildNumber, appIconName):
        self.bundleId = bundleId
        self.versionNumber = versionNumber
        self.buildNumber = buildNumber
        self.appIconName = appIconName


class IosIpa:

    def __init__(self, ipa_path):

        self.path = ipa_path
        self.name = ipa_path.rsplit('/', 1)[1]

        self.tmp_dir = os.getcwd() + '/_tmp/ipa_' + self.name
        self.unzip()

        self.infoplist_filepath = self.get_info_plist()
        self.buildInfo = self.get_build_infos()
        self.iconsArray = self.get_icon_files()

    # Unzip IPA to TMP directory
    def unzip(self):
        zip_ref = zipfile.ZipFile(self.path, 'r')
        zip_ref.extractall(self.tmp_dir)
        zip_ref.close()

    # Delete TMP directory
    def delete_tmp(self):
        shutil.rmtree(os.getcwd() + '/_tmp/')

    # Get info plist filepath
    def get_info_plist(self):

        payload_dir = self.tmp_dir + '/Payload'

        # find file
        infoplist_filepath = None

        for app_file in os.listdir(payload_dir):
            if app_file.endswith('.app'):
                for app_subfile in os.listdir(payload_dir + '/' + app_file):
                    if app_subfile == 'Info.plist':
                        infoplist_filepath = payload_dir + '/' + app_file + '/' + app_subfile

        return infoplist_filepath

    # Get build infos as IosBuildInfo object
    def get_build_infos(self):

        # Required params
        bundleIdString = None
        versionNumber = None
        buildNumber = None
        appIcon = None

        # Get plist file
        plist_content = None
        with open(self.infoplist_filepath) as plist:
            plist_content = plist.readlines()

        # Find the required info
        index = 0
        for plist_line in plist_content:

            if "CFBundleIdentifier" in plist_line:
                bundleIdString = get_content_from_string_xml(
                    plist_content[index + 1])

            if "CFBundleShortVersionString" in plist_line:
                versionNumber = get_content_from_string_xml(
                    plist_content[index + 1])

            if "CFBundleVersion" in plist_line:
                buildNumber = get_content_from_string_xml(
                    plist_content[index + 1])

            if "CFBundleIconFiles" in plist_line:
                appIcon = get_content_from_string_xml(plist_content[index + 2])

            index = index + 1

        return IosBuildInfo(bundleIdString, versionNumber, buildNumber, appIcon)

    # Return an array of App icon file names
    def get_icon_files(self):
        pattern = re.compile(r'\bAppIcon\S*?png\b')
        payload_dir = self.tmp_dir + '/Payload'

        # find files
        icon_filepath_array = []

        for app_file in os.listdir(payload_dir):
            if app_file.endswith('.app'):
                for app_subfile in os.listdir(payload_dir + '/' + app_file):
                    res = pattern.search(app_subfile)
                    if res:
                        icon_filepath = payload_dir + '/' + app_file + '/' + res.group()
                        icon_filepath_array.append(icon_filepath)

        return icon_filepath_array

    def get_info(self):
        """获取解析基本信息

        Returns:
            dict: 应用信息. 详见 https://github.com/nKsnC/Melody/tree/dev/plugins/ipa_parser
        """

        build_infos = self.buildInfo

        ipa_name = self.name
        bundle_id = build_infos.bundleId
        version_num = build_infos.versionNumber
        build_num = build_infos.buildNumber
        icon_path = self.iconsArray[0]

        info = {
            "ipa_name": ipa_name,
            "bundle_id": bundle_id.strip(),
            "version_num": version_num.strip(),
            "build_num": build_num.strip(),
            "icon_path": icon_path
        }

        return info


# --------------------
# Plist file parser extension
# --------------------

# Returning content form a <string>ABC</string> plist line
def get_content_from_string_xml(line):
    if 'string' in line:
        content = line.replace('<string>', '')
        content = content.replace('</string>', '')
        content = content.replace('\n', '')
        content = content.replace(' ', '')
        return content
    else:
        return None
