# News Generation

## Introduction

This project is a part of the Teknofest 2024 Türkçe Doğal Dil İşleme competition. The aim of the project is to
generate news title and content from a given image.

## Dataset

The dataset is collected from the ![Sabah](https://www.sabah.com.tr/timeline/) news website.
The dataset consist of news titles, news content and images. The dataset is in Turkish Language.

## Data-Preprocessing

````md
```python
sample_title = "Bursa’da servis minibüsü üst geçit inşaat alanına düştü!"
```

![image](https://isbh.tmgrup.com.tr/sbh/2021/12/17/bursada-servis-minibusu-ust-gecit-insaat-alanina-dustu-5-kisi-yaralandi-1639700937583.jpg)

1. Tokenization

```python
sample_title = ["Bursa", "da", "servis", "minibüsü", "üst", "geçit", "inşaat", "alanına", "düştü", "!"]

index_to_word = {0: "Bursa", 1: "da", 2: "servis", 3: "minibüsü", 4: "üst", 5: "geçit", 6: "inşaat", 7: "alanına", 8: "düştü", 9: "!"}

tokenized_title = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```
## Model

The model is a combination of CNN and LSTM, where the image is fed to the Encoder(CNN) and the output of the CNN is
fed to the Decoder(LSTM) along with the input text.
```
````
