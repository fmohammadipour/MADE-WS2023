echo "First Step - Run the Pipeline to get data"

python ../data/pipeline.py

echo "Data Pipeline is finished" 

echo "Second Step - perform the test"

python data_test.py

echo "running is finished without any error" 