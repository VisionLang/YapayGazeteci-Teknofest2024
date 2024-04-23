# News Generation

## Introduction

This project is a part of the Teknofest 2024 Türkçe Doğal Dil İşleme competition. The aim of the project is to
generate news title and content from a given image.

## Dataset

The dataset is collected from the ![Sabah](https://www.sabah.com.tr/timeline/) news website.
The dataset consist of news titles, news content and images. The dataset is in Turkish Language.

## Data-Preprocessing

- Sample Data:
  ![image](https://isbh.tmgrup.com.tr/sbh/2022/03/31/balikesirde-tarihi-binada-baslayan-ve-restorana-sicrayan-yangin-sonduruldu-1648686422986.jpeg)

  ***

  ```python
    title = "Balıkesir’de tarihi bina yangında küle döndü"
    word_index = {'Balıkesir’de': 9, 'tarihi': 5, 'bina': 3, 'yangında': 7, 'küle': 5, 'döndü': 6 }
    tokens: [start_token, 9, 5, 3, 7, 5, 6, end_token]
  ```

  | Input                                       | Output    |
  | ------------------------------------------- | --------- |
  | Image + start_token                         | 9         |
  | Image + start_token + 9                     | 5         |
  | Image + start_token + 9 + 5                 | 3         |
  | Image + start_token + 9 + 5 + 3             | 7         |
  | Image + start_token + 9 + 5 + 3 + 7         | 5         |
  | Image + start_token + 9 + 5 + 3 + 7 + 5     | 6         |
  | Image + start_token + 9 + 5 + 3 + 7 + 5 + 6 | end_token |

## Model

The model is a combination of CNN and LSTM, where the image is fed to the Encoder(CNN) and the output of the CNN is
fed to the Decoder(LSTM) along with the input text.

Balıkesir’de tarihi bina yangında küle döndü,"Hacıyusuf Mahallesi Yalı Sokak'taki tescilli yapı statüsünde bulunan bir binada henüz belirlenemeyen nedenle yangın çıktı.Binanın yanındaki restorana da sıçrayan yangın, bir hırsızlık olayı için bölgede inceleme yapan polis ekiplerince fark edilerek itfaiye ekiplerine bildirildi.Bölgeye çok sayıda itfaiye ekibi ile İlçe Emniyet Müdürlüğünden TOMA'lar sevk edildi. Çevre binalarda oturan vatandaşlar da yangın nedeniyle evlerinden tahliye edildi.Olay sırasında metruk bina ve restoranda çökmeler meydana gelirken, yan binanın dış cephe kaplamaları da yandı.İtfaiye ekiplerinin müdahalesiyle söndürülen yangında soğutma çalışmaları sürüyor.",/yasam/balikesirde-tarihi-binada-yangin-5932054,Yaşam,30.03.22-00:01,https://iasbh.tmgrup.com.tr/6c1939/752/395/0/57/800/477?u=https://isbh.tmgrup.com.tr/sbh/2022/03/31/balikesirde-tarihi-binada-baslayan-ve-restorana-sicrayan-yangin-sonduruldu-1648686422986.jpeg,../Data/imgs\img_246.jpeg
