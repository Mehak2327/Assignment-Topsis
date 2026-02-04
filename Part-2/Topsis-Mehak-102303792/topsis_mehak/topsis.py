import sys
import pandas as pd
import numpy as np

def topsis():

    if len(sys.argv) != 5:
        print("Usage: topsis <InputFile> <Weights> <Impacts> <OutputFile>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    try:
        if input_file.endswith(".csv"):
            data = pd.read_csv(input_file)
        elif input_file.endswith(".xlsx"):
            data = pd.read_excel(input_file)
        else:
            print("Error: File must be CSV or XLSX")
            sys.exit(1)
    except:
        print("Error: File not found")
        sys.exit(1)

    if data.shape[1] < 3:
        print("Error: Input file must contain three or more columns")
        sys.exit(1)

    try:
        matrix = data.iloc[:,1:].astype(float)
    except:
        print("Error: Non-numeric value found")
        sys.exit(1)

    weights = np.array(weights.split(","), dtype=float)
    impacts = impacts.split(",")

    if len(weights)!=matrix.shape[1] or len(impacts)!=matrix.shape[1]:
        print("Error: Weights, impacts and columns count mismatch")
        sys.exit(1)

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

    data.to_csv(output_file,index=False)
    print("Result saved in",output_file)
