.PHONY: install
install:
	pip3 install -r requirements.txt

.PHONY: compile
compile:
	pip-compile


.PHONY: setup
setup: compile install


.PHONY: run
run:
	python3 server.py
