# A tensorflow implemetation to solve the XOR-Problem


## How to run 

1) Use the `Makefile` and run `make environment` to recreate the environment this expample was build in. 
2) Run `make train` to train a simple neural network created in keras, consisting of one hidden dense layer with 16 neurons. The model should be saved in the directory `models/`
3) Run `make test` to load the trained model. A command-prompt should appear showing `input>`. 
4) Enter a command of the shape `x, y` whereas `x` and `y` map to two input sources that are either `0` or `1`, i.e `input> 1, 0`. 
5) An output prompt should appear, showing either `0` or `1` depending on the input, i.e. `output> 0.0`. 
6) Enter `input> exit` to quit the program. 


