environment:
	conda env create  -f environment.yml 
	conda activate xor

train: 
	python3 scripts/train.py
