poetry-install: # Install poetry
	pipx install poetry==1.2.0

create: # Create virtualenv
	poetry env use python3

activate: # Activate virtualenv
	poetry shell

install: # Install Dependencies
	poetry install

run: # Run service
	python3 -m app.service

run-test: # Run Test cases
	pytest
