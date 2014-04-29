#!/bin/bash

cat features | ./mapper.py > w.data
cat features | ./predict.py w.data s > ../visual_test/prediction.txt
cd ../visual_test
python visual_test.py
cd -