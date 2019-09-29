osx_environment:
	conda env create  -f environment_osx.yml 
	conda activate xor_keras

linux_environment:
	conda env create  -f environment_linux.yml 
	conda activate xor_keras

train: 
	python3 scripts/train.py
	
test:
	python3 scripts/test.py
