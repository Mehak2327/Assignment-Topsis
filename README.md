# Assignment – TOPSIS

Implementation of TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) using Python as a command line tool, a Python package published on PyPI, and a Flask-based web application. This project demonstrates an end-to-end solution for solving Multi-Criteria Decision Making (MCDM) problems using the TOPSIS method.

Folder Structure: Assignment-Topsis/ Part-1/ Part-2/ Part-3/

Part-1 (Command Line Program):  
Run → python Part-1/topsis.py Part-1/data.xlsx "1,1,1,1,1" "+,+,-,+,+" result.csv  
The output file result.csv contains TOPSIS score and rank.

Part-2 (PyPI Package):  
Install → pip install Topsis-Mehak-102303792  
Run → topsis data.xlsx "1,1,1,1,1" "+,+,-,+,+" output.csv  
PyPI Link → https://pypi.org/project/Topsis-Mehak-102303792/

Part-3 (Web Application):  
Install requirements → pip install -r Part-3/requirements.txt  
Run → python Part-3/app.py  
Open in browser → http://127.0.0.1:5000  
Note: This is a locally hosted Flask application and runs on localhost.

The web application accepts input file, weights, impacts and email ID, then sends the TOPSIS result CSV file to the provided email.

Author: Mehak  
Roll No: 102303792  

Conclusion: This project successfully demonstrates implementation, packaging, and deployment of the TOPSIS algorithm using Python.
