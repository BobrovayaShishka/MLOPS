import numpy as np
from sklearn.datasets import fetch_openml
import pandas as pd

def download_data():
    mnist = fetch_openml('mnist_784', version=1)
    data = pd.DataFrame(mnist.data)
    target = pd.DataFrame(mnist.target)
    data.to_csv("data.csv", index=False)
    target.to_csv("target.csv", index=False)
    print("Данные успешно загружены!")

if __name__ == "__main__":
    download_data()
