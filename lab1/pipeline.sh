#!/bin/bash
# This script is used to create the data for the pipeline
DATA_SIZE=$1
POLY_DEGREE=$2
NOISE=$3
ANOMALIES=$4
python3 ./data_creation.py $DATA_SIZE $POLY_DEGREE $NOISE $ANOMALIES
python3 ./model_preprocessing.py
python3 ./model_preparation.py $POLY_DEGREE
python3 ./model_testing.py