install:
	python setup.py install

run:
	python src/main.py

test:
	pytest src/tests/test_csv_processor.py 

pydoc:
	pydoc -w ./src/processors/csv_processor.py
