# Inference of water masses

Code for applying the model developed in the paper "Application of multi-regression machine learning algorithms to solve ocean water mass mixing in the Atlantic Ocean".

The model can be used in three different ways:
- As a [HuggingFace space](https://huggingface.co/spaces/joheras/water-masses-inference).
- As a [Jupyter notebook in colab]().
- As a local script. 

The former two options do not require installation, for the latter one you need to install the packages indicated in the requirements file and download the following two files: [the script]() and [the model]().

Then, to execute the script you have to run:

```bash
python main.py --latitude XXX --longitude XXX --ctdprs XXX --ctdpot XXX --ctdsal XXX
```

where `XXX` should be replaced with the actual values. 

For example, 

```bash
python main.py --latitude XXX --longitude XXX --ctdprs XXX --ctdpot XXX --ctdsal XXX
```
