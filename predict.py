import pandas as pd

# Unpickle model 
model = pd.read_pickle('generate.pickle') 

# Take input from user
gre = int(input("Enter GRE    : "))
tof = int(input("Enter TOEFL  : "))
cgpa = float(input("Enter CGPA : "))

# Predict chances 
result = model.predict([[gre,tof,cgpa]])  # input must be 2D array
print(f"Chances are : {result[0] * 100:.2f}%")

