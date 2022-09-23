from joblib import load
import matplotlib.pyplot as plt
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--latitude", required=True, help="Latitude")
ap.add_argument("-o", "--longitude", required=True, help="Longitude")
ap.add_argument("-p", "--ctdprs", required=True, help="CTDPRS")
ap.add_argument("-t", "--ctdpot", required=True, help="CTDPOT")
ap.add_argument("-s", "--ctdsal", required=True, help="CTDSAL")

args = vars(ap.parse_args())

Latitude= float(args["latitude"])
Longitude= float(args["longitude"])
CTDPRS= float(args["ctdprs"])
CTDPOT= float(args["ctdpot"])
CTDSAL= float(args["ctdsal"])

model = load('model_regr_et_combined.joblib') 
labels = ['EDW','ENACW12', 'WNACW7', 'SPMW', 'SACWT12', 'SACWE12', 'WW', 'AAIW5','AAIW3', 'MW', 'LSW', 'ISOW', 'DSOW', 'CDW', 'WSDW', 'SAIW']
prediction = model.predict([[Latitude,Longitude,CTDPRS,CTDPOT, CTDSAL]])
probs = prediction[0]
res = {labels[i]: float(probs[i])*100 for i in range(len(labels))}
plt.bar(*zip(*res.items()))
plt.xticks(rotation=90)
plt.savefig('prediction.png')
print(res)
