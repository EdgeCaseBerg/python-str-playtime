generatereport:
	@python -m cProfile main.py add1 > report.txt
	@echo "-------------------------------------------" >> report.txt
	@python -m cProfile main.py add2 interpolate >> report.txt
	@echo "-------------------------------------------" >> report.txt
	@python -m cProfile main.py add3 addition test >> report.txt
	@echo "-------------------------------------------" >> report.txt
	@python -m cProfile main.py add4 interpolate test 2 >> report.txt
	@echo "-------------------------------------------" >> report.txt
	@python -m cProfile main.py add5 addition test last one >> report.txt
	@echo "-------------------------------------------" >> report.txt
	@python -m cProfile main.py add6 interpolate test for last time >> report.txt
	
