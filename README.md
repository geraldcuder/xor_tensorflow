# A tensorflow implemetation to solve the XOR-Problem

This repository contains a simple neural network that solves the XOR-Problem. The network was created using `keras` and `tensorflow`. Furthermore, a simple program is provided that allows the user to test the trained model. The `environment.yml` makes sure that the user can recreate the conda environment in which this example was build.

## How to run 

1) Create a virtual environment by using one of the following options:
   
   **Conda environment**  
   Use the `Makefile` and run `make xx_environment` to recreate the environment this expample was build in, whereas the `xx` stands either for `osx_` or `linux_` due to some build-issues (see notes).

   **Pipenv**  
   A `Pipfile` and a `Pipfile.lock` are provided if you prefer to use `pipenv`. Use the command
   `$ pipenv shell` in the project directory.

   **requirements.txt**  
   If you prefer to use a plain `requirements.txt` to create a virtual environment using `virtualenv`.

2) Run `make train` to train a simple neural network created in keras, consisting of one hidden dense layer with 16 neurons. The model should be saved in the directory `models/`
3) Run `make test` to load the trained model. A command-prompt should appear showing `input>`. 
4) Enter a command of the shape `x, y` whereas `x` and `y` map to two input sources that are either `0` or `1`, i.e `input> 1, 0`. 
5) An output prompt should appear, showing either `0` or `1` depending on the input, i.e. `output> 0.0`. 
6) Enter `input> exit` to quit the program. 


## Background

**Which network architecture was used?**

I used a simple feed-forward neural network with one hidden dense layer using a rectified linear unit (RelU) activation. The hidden layer contains 16 neurons. The final output-layer is also a dense layer with one neuron, activated using a sigmoid function which maps the input of the hidden layer to a ouput between `0` and `1`, indicating a probablity. The input of the network is a numpy array containing four samples (every way to combine the numbers `0` and `1`), whereas each sample was of dimension `2`. So the shape of the input was `(4,2)`. 

**The minimum number of layers required**

The short answer to this question is that one hidden layer, one input and one output layer are required to get valid results. 

However, in the `notebook/`-folder, the notebook `1_xor_prototype_keras.ipynb` shows several experiments with different model architectures. It can be stated that more complex architectures, such as an increased number of hidden layers and/or an increased number of neurons per layer can certainly improve the performance of the model in a way that fewer epochs are required to get a higher accuracy. 

## Notes

* This example was created under Linux (Ubuntu 18.04 LTS) and tested on a Mac. Due to some conda-issues, two separate `environment.yml`-files were created. If you use Linux, use the `linux_environment.yml`, and `osx_environment.yml` if you use MacOS. 
* This example uses Python 3.7

