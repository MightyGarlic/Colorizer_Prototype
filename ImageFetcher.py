import os
import logging
import pixabay
from typing import Optional

# create directory if it doesn't exist
log_directory = 'ImageFetcher'
os.makedirs(log_directory, exist_ok=True)

# store the log in the new folder
log_file = os.path.join(log_directory, 'ImageFetcher.log')
logging.basicConfig(filename=log_file,encoding='utf-8',level=logging.INFO, filemode = 'w', format='%(levelname)s: %(message)s')

def get_images_from_pixabay(API_key: str, keyword: str, num_images: Optional[int] = None, lang: Optional[str] = 'en',
                            editorsChoice: Optional[int] = False,
                            image_size: Optional[str] = 'webformat') -> None:
    
    ''' 
    image_type: str, optional
        Filter results by image type. Accepted values: 'all', 'photo", 'illustration', 'vector' 

    image_size : str, optional 
        Size of the image to download ('preview', 'webformat', 'largeImage'). Default is 'webformat'
    
    ----------------
    Full Pixabay API documentation: https://pixabay.com/api/docs/
    
    ----------------
    Python pixabay wrapper documentation: https://github.com/Lukas0025/python-pixabay/tree/main

    '''
    
    # init pixabay API
    px = pixabay.core(API_key)

    # search for keyword
    media = px.query(query=keyword, lang=lang, perPage=200, editorsChoice=editorsChoice)

    # amount of total hits
    hits = len(media)
    logging.info(f"{hits} Pixabay hits for keyword {keyword}")

    if hits == 0: 
        logging.info("No images found. Try another keyword.")

    num_images = num_images or 1
    num_images = min(num_images, hits)

    # Download images
    for n in range(num_images):
        image_path = os.path.join('ImageFetcher', f"image_{keyword}_{n}.jpg")
        media[n].download(image_path, image_size)