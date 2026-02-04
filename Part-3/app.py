from flask import Flask, request, render_template_string
import pandas as pd
import numpy as np
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

HTML_FORM = """
<h2>TOPSIS Web Service</h2>
<form method="POST" enctype="multipart/form-data">
<input type="file" name="file" required><br><br>
Weights: <input type="text" name="weights" placeholder="1,1,1,1,1" required><br><br>
Impacts: <input type="text" name="impacts" placeholder="+,+,-,+,+" required><br><br>
Email: <input type="email" name="email" required><br><br>
<button type="submit">Submit</button>
</form>
"""

def run_topsis(file, weights, impacts):
    data = pd.read_excel(file)
    matrix = data.iloc[:,1:].astype(float)

    weights = np.array(weights.split(","), dtype=float)
    impacts = impacts.split(",")

    norm = matrix / np.sqrt((matrix**2).sum())
    weighted = norm * weights

    ideal_best=[]
    ideal_worst=[]

    for i in range(len(impacts)):
        if impacts[i]=='+':
            ideal_best.append(weighted.iloc[:,i].max())
            ideal_worst.append(weighted.iloc[:,i].min())
        else:
            ideal_best.append(weighted.iloc[:,i].min())
            ideal_worst.append(weighted.iloc[:,i].max())

    dist_best = np.sqrt(((weighted-ideal_best)**2).sum(axis=1))
    dist_worst = np.sqrt(((weighted-ideal_worst)**2).sum(axis=1))

    score = dist_worst/(dist_best+dist_worst)
    data["Topsis Score"]=score
    data["Rank"]=data["Topsis Score"].rank(ascending=False)

    output="result.csv"
    data.to_csv(output,index=False)
    return output

def send_email(receiver, file):
    EMAIL = "mehakjindal6789@gmail.com"
    PASSWORD = "grqc fibm ipup nmgk"

    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = EMAIL
    msg["To"] = receiver
    msg.set_content("Please find attached TOPSIS result.")

    with open(file,"rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=file)

    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(EMAIL,PASSWORD)
    server.send_message(msg)
    server.quit()

@app.route("/", methods=["GET","POST"])
def home():
    if request.method=="POST":
        file = request.files["file"]
        weights = request.form["weights"]
        impacts = request.form["impacts"]
        email = request.form["email"]

        file.save("input.xlsx")
        result = run_topsis("input.xlsx",weights,impacts)
        send_email(email,result)

        return "Result sent successfully to your email."

    return render_template_string(HTML_FORM)

if __name__ == "__main__":
    app.run(debug=True)
