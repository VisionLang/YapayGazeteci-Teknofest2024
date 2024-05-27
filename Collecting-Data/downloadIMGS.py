import pandas as pd 
import requests
import os 

def get_data():
    data_path = '../Data/news-data.csv'
    df = pd.read_csv(data_path)
    df = df.iloc[:2000]
    return df

def download_img(url, content_url, index):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            img_type = url.split('.')[-1]
            content_url = content_url.strip()
            img_name = "img_" + str(index+1) + '.' + img_type

            img_path = os.path.join(img_folder, img_name)

            if os.path.exists(img_path):
                return img_path

            with open(img_path, 'wb') as f:
                f.write(response.content)

            return img_path
        else:
            print(f"Failed to download image from {url}. Status code: {response.status_code}")
            return None

    except Exception as e:
        print(f"Error downloading image from {url}: {e}")
        return None

def main():
    df = get_data()

    global img_folder
    img_folder = '../Data/imgs'

    if not os.path.exists(img_folder):
        os.makedirs(img_folder)
    
    else:
        # Delete all files in the folder and recreate it
        for file in os.listdir(img_folder):
            file_path = os.path.join(img_folder, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")

    csv_file = '../Data/news-data-with-imgs.csv'

    if os.path.exists(csv_file):
        os.remove(csv_file)
    
    valid_rows = []

    for i, row in df.iterrows():
        img_url = row['Img_url']
        try:
            img = img_url.split('?u=')[1]
        except IndexError:
            img = img_url.split('?u=')[0]
        
        content_url = row['Content_url']
        content_url = content_url.replace('/', '_')

        img_path = download_img(img, content_url, i)

        if img_path:
            row['img_path'] = img_path
            valid_rows.append(row)

    valid_df = pd.DataFrame(valid_rows)
    valid_df.to_csv(csv_file, index=False)  
    print(f"Downloaded {len(valid_df)} images")
    return valid_df

if __name__ == '__main__':
    main()
