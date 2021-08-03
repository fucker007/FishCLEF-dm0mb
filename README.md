# Fish detector
## Aquarium Fish
![image](https://github.com/fucker007/FishCLEF-2020/blob/main/images/Picture1.png)
Send e-mail to apply for download permission, `yangzai126@126.com`

Large scale fish data can promote the development of stronger and more complex recognition networks and algorithms. However, fish species are complex and diverse. How to accurately organize and collect data sets is still the key problem in data set processing. Therefore, this experiment collects fish video images in the aquarium and manually cleans them to remove blurred and non fish images. 10042 images including 83 species of fish were obtained, with a total of 13558 targets, and the resolution of each image was 600 × 400 pixels. In order to meet the requirements of the data set in target detection and recognition based on supervised learning, labelme software is used to label the images. Each image includes target detection frame (x, y, W, H) and category label information. Where x, y, W and H represent the position (x, y) and length and width (W, H) of the detection frame respectively. In the experiment, the data were summarized and sorted according to the VOC (visual object classes) format, so that other relevant studies can be reused.

### datset distribution
![image](https://github.com/fucker007/FishCLEF-2020/blob/main/images/train_val_test.png)
### result 
![image](https://github.com/fucker007/FishCLEF-2020/blob/main/images/Picture2.png)
![image](https://github.com/fucker007/FishCLEF-2020/blob/main/images/mAP_for83_class.png)
### Comparison with other methods
![image](https://github.com/fucker007/FishCLEF-2020/blob/main/images/mAP_train.png)
![image](https://github.com/fucker007/FishCLEF-2020/blob/main/images/recall_train.png)

#### BTP-YOLOV4

| image size |	mAP	Average| IoU     |
| -------    | ---------- | ------- |
| 608×608    |  92.57 %   | 63.71 % | 
| 512×512    |  94.37%	   | 72.81%
| 416×416    |  94.23 %   | 69.83 % |
| 306×306    |  88.16 %   | 63.67 % |
| 256×256    |  85.26 %   | 66.13 % |
| 208×208    |  60.62 %   | 54.33 % |

| Mixup	 |  Cutmix |	Mosaic |	ReLU |	Swish |	Mish  |	ELU  |	BN  |	mAP@0.5  |
| ------ | ------- | --------  | --------| ------ | ----- | ---- | ---- | ---------- |
|        |         |           |     x   |		  |       |      |   x  |  92.34%   |
|   x    |         |           |     x   |        |       |      |   x   |  92.69%   |   
|        |    x    |           |     x   |        |       |      |   x   |  92.93%   |
|        |         |     x     |     x   |        |       |      |   x   |  93.12%   |
|   x    |    x    |    x      |     x   |        |       |      |   x   |  93.61%   |
|   x    |    x    |    x      |         |    x   |       |      |   x   |  93.01%    |
|   x    |    x    |    x      |         |        |  x    |      |   x   |  94.37%   |
|   x    |    x    |    x      |         |        |  x    |      |       |  89.66%   |
|   x    |    x    |    x      |         |        |       |  x   |   x   |  93.27%   |

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

我们将train和test中的0-15号数，做了合并，在充分混合后，取11812作为训练集，2953张作为测试集。
train data :183, 6528, 323, 171, 694, 283, 2471, 1342, 106, 799, 1358, 1170, 234, 200, 2313

```
@article{liu2021research,
  title={Research on Optimization Method of Multi-scale Fish Target Fast Detection Network},
  author={Liu, Yang and Zhang, Shengmao and Wang, Fei and Fan, Wei and Zou, Guohua and Bo, Jing},
  journal={arXiv preprint arXiv:2104.05050},
  year={2021}
}
```
