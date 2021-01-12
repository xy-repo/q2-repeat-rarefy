# ----------------------------------------------------------------------------
# Copyright (c) 2016-2020, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import (Plugin, Int, Float, Range, Metadata, Str, Bool,
                           Choices, MetadataColumn, Categorical, List,
                           Citations, TypeMatch)

import q2_repeat_rarefy
from ._normalize import repeat_rarefy
from q2_types.feature_table import (FeatureTable, Frequency)

citations = Citations.load('citations.bib', package='q2_repeat_rarefy')

plugin = Plugin(
    name='repeat-rarefy',
    version=q2_repeat_rarefy.__version__,
    website='https://github.com/yxia0125/repeat-rarefy',
    package='q2_repeat_rarefy',
    short_description=('Repeat rarefy method.'),
    description=('This is a QIIME 2 plugin for repeat rarefy.'),
    citations = Citations.load('citations.bib', package='q2_repeat_rarefy')
)

plugin.methods.register_function(
    function = repeat_rarefy,
    inputs={'table': FeatureTable[Frequency]},
    parameters={'sampling_depth': Int % Range(1, None),
                'with_replacement': Bool,
                'repeat_times': Int % Range(1, None)},
    outputs=[('rarefied_table', FeatureTable[Frequency])],
    input_descriptions={'table': 'The feature table to be rarefied.'},
    parameter_descriptions={
        'sampling_depth': ('The total frequency that each sample should be '
                           'rarefied to. Samples where the sum of frequencies '
                           'is less than the sampling depth will be not be '
                           'included in the resulting table unless '
                           'subsampling is performed with replacement.'),
        'with_replacement': ('Rarefy with replacement by sampling from the '
                             'multinomial distribution instead of rarefying '
                             'without replacement.'),
        'repeat_times': ('Repeat rarefy times. For examples, if set to 10, it '
                         'will run random rarefication 10 times and 10 resulting '
                         'rarefied tables will be merged with union mode. Then the '
                         'average (round-up) count for each asv will be computed to '
                         'generate the final average rarefied feature table.'
                        ),
    },
    output_descriptions={
        'rarefied_table': 'The resulting average rarefied feature table.'
    },
    name='Average rarefied table',
    description=("Repeatly rarefy the feature table"),
    citations = [citations['Xia2021']]
    )

