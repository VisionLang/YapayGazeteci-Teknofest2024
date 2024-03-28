import pandas as pd 
import requests
import os 

def get_data():
    data_path = '../Data/news-data.csv'
    df = pd.read_csv(data_path)
    df = df.iloc[:1000]
    return df

def download_img(url, content_url):
    folder = '../Data/imgs' 
    try:
        response = requests.get(url)
        if response.status_code == 200:
            img_type = url.split('.')[-1]
            content_url = content_url.strip()
            img_name = content_url.replace('/', '_') + '.' + img_type

            img_path = os.path.join(folder, img_name)

            if os.path.exists(img_path):
                return img_path

            with open(img_path, 'wb') as f:
                f.write(response.content)

            return img_path
        else:
            print(f"Failed to download image from {url}. Status code: {response.status_code}")
            return Nonex

    except Exception as e:
        print(f"Error downloading image from {url}: {e}")
        return None

def main():
    df = get_data()

    folder = '../Data/imgs' 

    os.makedirs(folder, exist_ok=True)
     
    for i, img_url in enumerate(df['Img_url']):
        try:
            img = img_url.split('?u=')[1]
        except IndexError:
            img = img_url.split('?u=')[0]
        
        content_url = df.at[i, 'Content_url']
        content_url = content_url.replace('/', '_')

        img_path = download_img(img, content_url)

        if img_path:
            df.at[i, 'img_path'] = img_path

    df.to_csv('../Data/news-data-with-imgs.csv', index=False)  

    return df

if __name__ == '__main__':
    main()
