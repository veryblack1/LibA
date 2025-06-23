from setuptools import setup, find_packages

print("Setup:liba imported!")

setup(
    name="liba",                      # 包名
    version="0.1.0",                  # 版本号
    author="yangtuomao",             # 作者名
    author_email="ytm@example.com",  # 邮箱（可选）
    description="A utility lib",     # 简短描述
    long_description=open("README.md").read(),  # 可选：长描述
    long_description_content_type="text/markdown",
    url="https://github.com/yangtuomao/liba",   # 项目地址
    packages=find_packages(),        # 自动递归包含包
    install_requires=[],             # 依赖包列表
    classifiers=[                    # 可选：元数据（可用于 PyPI）
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',         # Python 最低版本要求
)














