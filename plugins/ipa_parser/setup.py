# 引入构建包信息的模块
from distutils.core import setup
# 定义发布的包文件的信息
import setuptools
setup(
    name="ipa_parser",
    version="0.0.1",
    author="ios",
    description="ipa基础信息解析",

    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=[
        'shutil',
        'zipfile'
    ]
)
