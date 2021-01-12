# q2-repeat-rarefy: QIIME2 plugin for repeat rarefy method for library size normalization
When handling a sparse dataset, I noticed that the rare taxa was easily ignored by the traditional one-shot rarefication. 
So I proposed a repeat rarefy strategy, and wrote a very simple plugin to deal with this problem (ref: ).
Repeat rarefy simply runs random rarefication N times, and computes the average count (floats are round up) of each OTU (ASV/feature) to gernerate the final average rarefied OTU table. 
It proves that most rare OTUs were maintained while using repeat rarefy to normalize library size (unpublised results).
As the float average count of OTU are round up, the total OTU count of each sample may not exactly the same.
This method may be a good alternative to the one-shot rarefication, given its ability to keep information.

## Installing
```
conda activate qiime2-2020.11
pip install git+https://github.com/yxia0125/q2-repeat-rarefy.git
```
Type "qiime repeat-rarefy" to test if the installation is sucessful.

## Uninstalling
`pip uninstall q2-repeat-rarefy`

## Using
```
qiime repeat-rarefy repeat-rarefy --i-table table.qza \
                                  --p-sampling-depth 2000 \
                                  --p-repeat-times 100 \
                                  --o-rarefied-table average_rarefied_table.qza
```
The above example rarefied the 'table.qza', under sampling depth of 2000 and repeat times of 100, to 'average_rarefied_table.qza'. 
You can set the sampling depth based on your own dataset and increase repeat times to 1,000, 10,000 ...

## Citing 
If you are interested to use repeat rarefy for any published research, please including the following citation:
`Yao Xia, q2-repeat-rarefy, (2021), GitHub repository, https://github.com/yxia0125/q2-repeat-rarefy.`
