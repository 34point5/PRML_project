#!/bin/bash

python make_type_list.py

while [ 1 ]; do
	python study_type_list.py
done