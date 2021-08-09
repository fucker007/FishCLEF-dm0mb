# Fish detector
## Aquarium Fish
![image](https://github.com/fucker007/FishCLEF-2020/blob/main/images/Picture1.png)
      
Send e-mail to apply for download permission, `yangzai126@126.com`

Large scale fish data can promote the development of stronger and more complex recognition networks and algorithms. However, fish species are complex and diverse. How to accurately organize and collect data sets is still the key problem in data set processing. Therefore, this experiment collects fish video images in the aquarium and manually cleans them to remove blurred and non fish images. 10042 images including 83 species of fish were obtained, with a total of 13558 targets, and the resolution of each image was 600 × 400 pixels. In order to meet the requirements of the data set in target detection and recognition based on supervised learning, labelme software is used to label the images. Each image includes target detection frame (x, y, W, H) and category label information. Where x, y, W and H represent the position (x, y) and length and width (W, H) of the detection frame respectively. In the experiment, the data were summarized and sorted according to the VOC (visual object classes) format, so that other relevant studies can be reused.

### datset distribution
![image](https://github.com/fucker007/FishCLEF-2020/blob/main/images/train_val_test.png)
Fish species: 
Sardine, China's Horseshoe, double faced clown, clown, rootle, big fish, the Atlantic sea thorn, dog's nest, hermit crab, general, a small sardine, snapshot, snapshot, sail, crane, jellyfish, nurse, shark, spotted jellyfish, squirrel, dream rose, acantha, towel, fairy, puffer, sardine, Hainan, sardines, sea moon, sea god, sea apple, sea anemone, jellyfish, sea fish, seahorse, sea eel. Freshwater pomfret, clean shrimp, grey hanging, swallow ray, one horned hanging, rose fish, hawksbill shell, white trick fish, white fin shark, Queen Fairy, stone beauty, Mickey, purple print, red clown, red tailed cat, red zebra, green turtle, green dragon, beauty shrimp, bright red, Sumei, blue Mody, blue inverted hanging, blue fin Finch, tiger skin hanging, lice, blood parrot, damselfly, leopard > shark, red ray, golden eye hanging, golden drum fish, golden dragon fish, beautiful lobster, lightning Finch, Finless eel, Chardonnay jellyfish, green Mody, frog fish, catfish, mackerel, duck billed fish, mandarin duck, shell fish, parrot beak, sacked butterfly, yellow Mody, yellow bride, yellow fox, yellow dragon, black fin shark
(七彩吊,中国鲎,人字鲽,关刀,千手佛,双带小丑,圆燕,大目鱼,大西洋海刺,天狗吊,寄居蟹,将军甲,小沙丁鱼,川纹笛鲷,巨石斑,帆吊,彩色水母,护士鲨,斑点水母,松鼠鱼,梦幻玫瑰,棘皮海星,毛巾神仙,河豚,海南沙丁鱼,海月,海神像,海苹果,海葵,海蜇,海象鱼,海马,海鳝,淡水鲳鱼,清洁虾,灰吊,燕子鳐,独角吊,玫瑰鱼,玳瑁,白招财鱼,白鳍鲨,皇后神仙,石美人,米奇,紫印,红小丑,红尾猫,红斑马,绿海龟,绿龙,美人虾,艳红,苏眉,蓝么,蓝倒吊,蓝鳍雀,虎皮吊,虱目鱼,血鹦鹉鱼,豆娘,豹纹鲨,赤魟,金目吊,金鼓鱼,金龙鱼,锦绣龙虾,闪电雀,雀鳝,霞水母,青么,青蛙鱼,鮣鱼,鲭鱼,鸭嘴鱼,鸳鸯炮弹鱼,鹦鹉嘴,麻包蝶,黄么,黄新娘,黄狐狸,黄龙,黑鳍鲨)
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


```
@article{liu2021research,
  title={Research on Optimization Method of Multi-scale Fish Target Fast Detection Network},
  author={Liu, Yang and Zhang, Shengmao and Wang, Fei and Fan, Wei and Zou, Guohua and Bo, Jing},
  journal={arXiv preprint arXiv:2104.05050},
  year={2021}
}
```
