from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="Topsis-Mehak-102303792",
    version="1.0.1",
    author="Mehak",
    description="Python package implementing TOPSIS method",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["pandas","numpy","openpyxl"],
    entry_points={
        "console_scripts": [
            "topsis=topsis_mehak.topsis:topsis"
        ]
    }
)
