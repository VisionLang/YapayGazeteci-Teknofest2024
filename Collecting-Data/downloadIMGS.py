import pandas as pd 
import requests
import os 

def get_data():
    df_list = []

    data_path = '../Data/news-data.csv'

    df = pd.read_csv(data_path)
    df = df.iloc[:100]
    return df

def download_img(url, content_url):
    folder = '../Data/imgs' 
    try:    
        response = requests.get(url)
        if response.status_code == 200:
            
            img_type = url.split('.')[-1]
            
            content_url = content_url.strip()
            
            img_path = f'{folder}/{content_url}.{img_type}' 

            with open(img_path, 'wb') as f:
                f.write(response.content)

            return img_path
        else:
            return None

    except Exception as e:
        print(f"Img could not be downloaded,{content_url}.")
        return None

def main():
    df = get_data()

    df['img_path'] = None

    folder = '../Data/imgs' 

    if os.path.exists(folder):
        os.rmdir(path=folder)

    os.makedirs(folder)
     
    for i, img_url in enumerate(df['Img_url']):

        try:
            img = img_url.split('?u=')[1]
        except:
            img = img_url.split('?u=')[0]
        
        content_url = df[df['Img_url'] == img_url]['Content_url'].values[0]
        content_url = content_url.replace('/', '_')

        img_path = download_img(img, content_url)

        if img_path:
            df.at[i, 'img_path'] = img_path

    df.to_csv('../Data/news-data-with-imgs.csv', index=False)  

    return df

if __name__ == '__main__':
    main()