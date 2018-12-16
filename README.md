# Tugas Besar<br>IF4041 Teknologi Basis Data

## 1. Data Stream
_Data Stream_ menggunakan data *tweet* dan dilakukan dengan menggunakan:
- [Tweepy](http://www.tweepy.org/)
- [Twitter](https://www.twitter.com/)
- [Python3](https://www.python.org/download/releases/3.0/)
### 1.1 Sampling
#### 1.1.1 Pendahuluan
_Sampling_ dilakukan dengan menggunakan algoritma _Reservoir Sampling_.
#### 1.1.2 Source Code
Sampling dapat dilihat pada file
```
sampling.py
```
Contoh hasil sampling dapat dilihat pada
```
sample.json
```
### 1.2 Filtering
#### 1.2.1 Pendahuluan
_Filtering_ dilakukan dengan menggunakan algoritma _Bloom Filter_. _List of keys_ yang digunakan berisi _userid_ yang dianggap merupakan pakar teknologi/figur publik.
#### 1.2.2 Source Code
_Filtering_ dapat dilihat pada _file_
```
filtering.py
```
Contoh hasil sampling dapat dilihat pada
```
filter.json
```
_List of keys_ yang digunakan dapat dilihat pada.
```
listofkeys.json
```
### 1.3 Counting Distinct
#### 1.3.1 Pendahuluan
_Counting Distinct_ menggunakan algoritma _Flajolet Martin_
#### 1.3.2 Source Code
_Counting Distinct_ dapat dilihat pada _file_
```
count_distinct.py
```
dengan menggunakan data
```
streaming
```
### 1.4 Counting Itemset
#### 1.4.1 Pendahuluan
_Counting Itemset_ menggunakan algoritma DGIM
#### 1.4.2 Source Code
_Counting Itemset_ dapat dilihat pada _file_
```
count_itemset.py
```
dengan menggunakan data
```
streaming
```
## 2. Eksplorasi Analisis Graph
Eksplorasi analisis graph menggunakan yang didapatkan dari situs Amazon. Graf ini didasarkan pada “pelanggan yang membeli item a juga membeli item b” dari situs Amazon. Data tersebut adalah data sampel belanja pelanggan pada tanggal 2 Maret 2003, 12 Maret 2003, 5 Mei 2003 dan 1 Juni 2003. Sumber data yang digunakan adalah:
+ [Amazon 3 Maret 2003](https://snap.stanford.edu/data/amazon0302.html)
+ [Amazon 12 Maret 2003](https://snap.stanford.edu/data/amazon0312.html)
+ [Amazon 5 Mei 2003](https://snap.stanford.edu/data/amazon0505.html)
+ [Amazon 1 Juni 2003](https://snap.stanford.edu/data/amazon0601.html)

Tools yang digunakan adalah:
- [NetworkX](https://networkx.github.io/documentation/networkx-1.10/index.html)
### Source Code
Eksplorasi yang dilakukan dapat dilihat pada _file_
```
amazon.py
```
dengan menggunakan data
```
amazon0302.txt
amazon0312.txt
amazon0505.txt
amazon0601.txt
```