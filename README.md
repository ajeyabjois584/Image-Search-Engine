# Image-Search-Engine
Content Based Image Retrival based on Color Histogram

This project is basically used to retrive images with same color contrast
The dataset that is used is Inria Holiday Dataset and is open source.You can find it here http://lear.inrialpes.fr/~jegou/data.php

Store the dataset in the folder named dataset and create some query images inside a folder called queries

create a index.csv file to store mapping between images and their respective histograms

inside app folder run the file named searcher.py as follows 

python3 searcher.py --index index.csv --query queries/<name of the query image> --result-path dataset 
boom you will have top 10 images displayed on the screen 

i followed this guy's blog to build this https://www.pyimagesearch.com/
