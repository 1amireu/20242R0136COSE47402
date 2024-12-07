import kagglehub
import os

# Download the dataset to the specified folder
pathr = kagglehub.dataset_download("wilmerarltstrmberg/recipe-dataset-over-2m")
pathf = kagglehub.dataset_download("dansbecker/food-101")

print("Dataset downloaded recipe : " + pathr + "\nfood : "+ pathf)
