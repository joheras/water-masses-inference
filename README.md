# Inference of water masses

Code for applying the model developed in the paper "Application of multi-regression machine learning algorithms to solve ocean water mass mixing in the Atlantic Ocean".

The model can be used in three different ways:
- As a [HuggingFace space](https://huggingface.co/spaces/joheras/water-masses-inference).
- As a [Jupyter notebook](Inference.ipynb).
- As a local script. 

The first option does not require installation, for the latter two you need to install the packages indicated in the requirements file and clone the current repository.

The notebook contains all the instructions to download the model and use it for inference. 

For the script, you need to download the [model](https://github.com/joheras/water-masses-inference/releases/download/v1.0/model_regr_et_combined.joblib) in the same folder where you cloned the repository.

Then, to execute the script you have to run:

```bash
python main.py --latitude XXX --longitude XXX --ctdprs XXX --ctdpot XXX --ctdsal XXX
```

where `XXX` should be replaced with the actual values. 


For example, 

```bash
python main.py --latitude -57.4997 --longitude -31.5992 --ctdprs 347.9 --ctdpot 1.8694 --ctdsal 34.587
```

This will print the predictions and also generate a image file called prediction.png as the following one. 




