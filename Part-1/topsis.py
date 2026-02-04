import sys
import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):

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
        matrix = data.iloc[:, 1:].astype(float)
    except:
        print("Error: From 2nd to last columns must contain numeric values only")
        sys.exit(1)

    weights = weights.split(",")
    impacts = impacts.split(",")

    if len(weights) != matrix.shape[1] or len(impacts) != matrix.shape[1]:
        print("Error: Number of weights, impacts and columns must be same")
        sys.exit(1)

    weights = np.array(weights, dtype=float)

    for i in impacts:
        if i not in ['+', '-']:
            print("Error: Impacts must be + or -")
            sys.exit(1)

    # Step 1: Normalize
    norm = matrix / np.sqrt((matrix**2).sum())

    # Step 2: Weight multiplication
    weighted = norm * weights

    # Step 3: Ideal best and worst
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Distances
    dist_best = np.sqrt(((weighted - ideal_best)**2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst)**2).sum(axis=1))

    # Step 5: Score
    score = dist_worst / (dist_best + dist_worst)

    data["Topsis Score"] = score
    data["Rank"] = data["Topsis Score"].rank(ascending=False)

    data.to_csv(output_file, index=False)
    print("Result saved in", output_file)

# Command Line Handling
if len(sys.argv) != 5:
    print("Usage: python topsis.py <InputFile> <Weights> <Impacts> <OutputFile>")
    sys.exit(1)

topsis(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
