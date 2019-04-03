SHELL=/bin/bash

help:
	@echo 'Makefile for Quake Log Parser / API                           '
	@echo '                                                              '
	@echo 'Usage:                                                        '
	@echo '    make clean              Remove python compiled files      '
	@echo '    make requirements_dev   Install required packages to Dev  '
	@echo '    make lint               Verify code lint                  '
	@echo '    make unit               Run unit tests                    '
	@echo '    make migrate_db         Apply the migrations to db        '
	@echo '    make runserver          Run the application               '
	@echo '                                                              '

clean:
	find . -iname '*.pyc' -delete;
	find . -iname '*.pyo' -delete;
	find . -iname '__pycache__' -delete;
	rm -rf .pytest_cache;
	rm -rf .cache;

requirements_dev:
	pip install -r requirements/requirements_dev.txt

lint:
	isort --check
	flake8

unit:clean
	python -m pytest --show-capture=no

migrate_db:
	python manage.py makemigrations
	python manage.py migrate
	
runserver:
	python manage.py runserver

