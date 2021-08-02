# Dataset
## Aquarium Fish
Send e-mail to apply for download permission, `yangzai126@126.com`

Large scale fish data can promote the development of stronger and more complex recognition networks and algorithms. However, fish species are complex and diverse. How to accurately organize and collect data sets is still the key problem in data set processing. Therefore, this experiment collects fish video images in the aquarium and manually cleans them to remove blurred and non fish images. 10042 images including 83 species of fish were obtained, with a total of 13558 targets, and the resolution of each image was 600 ¡Á 400 pixels. In order to meet the requirements of the data set in target detection and recognition based on supervised learning, labelme software is used to label the images. Each image includes target detection frame (x, y, W, H) and category label information. Where x, y, W and H represent the position (x, y) and length and width (W, H) of the detection frame respectively. In the experiment, the data were summarized and sorted according to the VOC (visual object classes) format, so that other relevant studies can be reused.


## FishCLEF-2015
  dataset come from https://github.com/perceivelab/FishCLEF-2015
### FishCLEF-2015 data processing
  source dataset from https://tinyurl.com/FishCLEF-2015    
  our processing dataset: https://pan.baidu.com/s/1EVY1sQ4KErlE4JT7VxIoFQ    
  baiduyun Extraction code: gy72
  - **step 1:** Convert video annotation files to image annotation files    
    `python data_prosses.py`    
  - **step 2:** Convert the annotation file to VOC format    
    `python voc_label.py`
### Training Data distribution

| id  | name                      | number |
| --- | ------------------------- | -----  |
| 0   | Abudefduf Vaigiensis      |   132  | 
| 1   | Dascyllus Reticulatus     |  3164  |
| 2   | Acanthurus Nigrofuscus    |   294  |
| 3   | Hemigumnus Malapterus     |   214  |
| -   |  Hemigymnus Fasciatus     |    -   |
| 5   | Amphiprion Clarkii        |   362  |
| 6   | Myripristis Kuntee        |   242  |
| 7   | Chaetodon Lununatus       |  1217  |
| 8   | Neoglyphidodon Nigroris   |    85  |
| 9   | Chaetodon Speculum        |   138  |
| 10  | Pempheris Vanicolensis    |   999  |
| 11  | Chaetodon Trifascialis    |   335  |
| 12  | Plectrogly-Phidodon Dickii|   737  |
| 13  | Chromis Chrysura          |   275  |
| 14  | Zebrasoma Scopas          |    72  |
| 15  | Dascyllus Aruanus         |   894  |
|  -  |  Plectorhinchus Vittatus   |  -    |
|  -  |  Canthigaster Valentini    |  -    |
|  -  |  Neoniphon Sammara         |  -    |
|  -  |  Pomacentrus Moluccensis   |  -    |
|  -  |  Scaridae                  |  -    |
|  -  |  Siganus Fuscescens        |  -    |
|  -  |  Scolopsis Bilineata       |  -    |
|  -  |  Chaetodon Auripes         |  -    |
|  -  |  Lethrinus Ornatus         |  -    |
|  -  |  NULL                      |  -    |
  
### Testing Data distribution 

| id  | name                      | number |
| --- | ------------------------- | -----  |
|  0  |  Abudefduf Vaigiensis      |   93  |   
|  1  |  Dascyllus Reticulatus     | 5046  |
|  2  |  Acanthurus Nigrofuscus    |  129  |
|  -  |  Hemigumnus Malapterus     |   -   |
|  4  |  Hemigymnus Fasciatus      |    7  |
|  5  |  Amphiprion Clarkii        |  517  |
|  6  |  Myripristis Kuntee        |  118  |
|  7  |  Chaetodon Lununatus       | 1876  |
|  8  |  Neoglyphidodon Nigroris   | 1593  |
|  -  |  Chaetodon  Speculum       |  -    |
|  -  |  Pempheris  Vanicolensis   |  -    |
|  11 |  Chaetodon Trifascialis    | 1317  |
|  12 |  Plectrogly-Phidodon Dickii|  700  |
|  13 |  Chromis Chrysura          |   24  |
|  14 |  Zebrasoma Scopas          |  187  |
|  15 |  Dascyllus Aruanus         | 1985  |
|  16 |  Plectorhinchus Vittatus   |    8  |
|  17 |  Canthigaster Valentini    |   50  |
|  18 |  Neoniphon Sammara         |    6  |
|  19 |  Pomacentrus Moluccensis   |   40  |
|  20 |  Scaridae                  |   42  |
|  21 |  Siganus Fuscescens        |  269  |
|  22 |  Scolopsis Bilineata       |   20  |
|  23 |  Chaetodon Auripes         |   15  |
|  24 |  Lethrinus Ornatus         |    7  |
|  25 |  NULL                      |  150  |

