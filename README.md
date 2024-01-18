# Exploring How Corona Relate to Happiness Factors Worldwide

## Porject report:
In this link you can find a complete report about this project :

https://github.com/fmohammadipour/MADE-WS2023/blob/main/project/final-report.ipynb

## Data Exploration
if you are interested in exploring choosen dataset you can go over this file and see some visualization on them :

https://github.com/fmohammadipour/MADE-WS2023/blob/main/project/data-exploration.ipynb

## Presentation
in the following link you can also see the slides presenting this project as well:

https://github.com/fmohammadipour/MADE-WS2023/blob/main/project/slides.pdf

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
