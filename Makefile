install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt && python -m spacy download en

