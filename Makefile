install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt && python3 -m spacy download en

