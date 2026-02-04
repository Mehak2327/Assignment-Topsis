# Assignment-Topsis
Implementation of TOPSIS using Python: CLI tool, PyPI package and Web Service

This project implements the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) using Python. The assignment is completed in three parts: a command-line program, a Python package published on PyPI, and a Flask-based web application.

Folder Structure:
Assignment-Topsis/
Part-1/
Part-2/
Part-3/

Part-1 (Command Line Program):
Run:
python Part-1/topsis.py Part-1/data.xlsx "1,1,1,1,1" "+,+,-,+,+" result.csv

Part-2 (PyPI Package):
Install:
pip install Topsis-Mehak-102303792

Run:
topsis data.xlsx "1,1,1,1,1" "+,+,-,+,+" output.csv

PyPI Link:
https://pypi.org/project/Topsis-Mehak-102303792/

Part-3 (Web Application):
Install requirements:
pip install -r Part-3/requirements.txt

Run:
python Part-3/app.py

Open in browser:
http://127.0.0.1:5000

The web application accepts input file, weights, impacts and email ID, then sends the TOPSIS result CSV file to the provided email.

Author:
Mehak  
Roll No: 102303792
