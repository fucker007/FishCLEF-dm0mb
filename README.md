# FishCLEF-2015
  dataset come from https://github.com/perceivelab/FishCLEF-2015
## FishCLEF-2015 data processing
  source dataset from https://tinyurl.com/FishCLEF-2015
  our processing dataset: 
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

