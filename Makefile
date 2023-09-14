run:
	python src/main.py

test:
	pytest src/tests/test_csv_processor.py > log.txt

