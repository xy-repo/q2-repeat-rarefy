# q2-repeat-rarefy: QIIME2 plugin for generating the average rarefied table for library size normalization using repeated rarefaction
* When handling a sparse dataset, I noticed that the rare taxa were easily ignored by the traditional one-shot rarefaction.  
* To deal with this problem, I proposed the "Average Rarefied Table" method and wrote a very simple plugin (reference: https://github.com/qiime2/q2-feature-table/tree/master/q2_feature_table/_normalize.py)).  
* Repeat rarefy simply runs random rarefaction *N* times, and computes the average count (floats are round up) of each OTU (ASV/feature) to generate the final average rarefied OTU table.  
* It proves that comparing with the one-shot rarefaction, using repeat rarefy to normalize library size can keep significantly more OTUs (unpublished results).  
* As the float average count of OTU is round up, the total OTU count of each sample may not be exactly the same.  
* This method has the potential to be an ideal alternative to the current one-shot rarefaction, as it can keep information and avoid variation of composition.
* In addition to OTU (ASV/feature) table, the "Average Rarefied Table" method can also be extended to other profile tables (e.g., taxonomic profile table, gene profile table).

## Installing
```
conda activate qiime2-2020.11
pip install git+https://github.com/yxia0125/q2-repeat-rarefy.git
```
Type "qiime repeat-rarefy" to test if the installation is successful.

## Uninstalling
`pip uninstall q2-repeat-rarefy`

## Using
```
qiime repeat-rarefy repeat-rarefy --i-table table.qza \
                                  --p-sampling-depth 2000 \
                                  --p-repeat-times 100 \
                                  --o-rarefied-table average_rarefied_table.qza
```
The above example rarefied the 'table.qza', with the sampling depth of 2000 and the repeat times of 100, to 'average_rarefied_table.qza'.  
You can set the sampling depth based on your own dataset and increase repeat times to 1,000, 10,000 ...

## Citing 
If you are interested to use this method, please include the following citation:
```
Yao Xia, q2-repeat-rarefy: QIIME2 plugin for generating the average rarefied table for library size normalization using 
repeated rarefaction, (2021), GitHub repository, https://github.com/yxia0125/q2-repeat-rarefy.
```
