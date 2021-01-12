# ----------------------------------------------------------------------------
# Reference: QIIME 2 development team, https://github.com/qiime2/q2-feature-table/tree/master/q2_feature_table/_normalize.py 
#
# Copyright (c) 2021, Yao Xia.
# 
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import biom
import numpy as np
import pandas as pd

def repeat_rarefy(table: biom.Table, sampling_depth: int, repeat_times: int,
        with_replacement: bool = False) -> biom.Table:
    
    output_table = table.subsample(sampling_depth, axis='sample', by_id=False, 
            with_replacement=with_replacement)

    if repeat_times != 1:
        for i in range(repeat_times-1):
            sub_table = table.subsample(sampling_depth, axis='sample', by_id=False,
                with_replacement=with_replacement)
            output_table = output_table.merge(sub_table)
        
        df = output_table.to_dataframe()
        df = df/(repeat_times)
        df = df.apply(np.ceil)
        
        output_table = biom.Table(df.values, df.index.to_list(), df.columns.to_list())

    if output_table.is_empty():
        raise ValueError('The rarefied table contains no features.')

    return output_table
