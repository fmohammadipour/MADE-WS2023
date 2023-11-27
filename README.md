# Methods of Advanced Data Engineering

### requirements before starting
## requirements : 

## libraries :


## Kaggle Authentication
In this project one of the datasets in provided by kaggle. For downloading and use it in this project, we need to use their authentication system which includes a kaggle.json file. 
you can get it from [link](https://www.kaggle.com/settings)
for more instruction and help about using kaggle api you can visit : 
after getting it, the file should be placed in `/project/kaggle.json`

**Filepath:** `/project/kaggle.json`

```
{
  "username":"far*****r",
  "key":"ad25*******************1f"
}
```


## how to use 

## First step : Run requirements installation

./project/reqInstall.sh

## second step : Run pipeline
```
./project/pipeline.sh
```

this pipeline is designed to run pipeline.py to read data from its source and do some cleaning and save the results in sqlite files in /data folder. 