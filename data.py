from typing import List
import os
import logging

import pandas as pd


def _read_sentences(path: str) -> List[str]:
    with open(path, 'r') as f:
        return [line.replace('\n', '') for line in f.readlines()]


def load_data(folder: str, balance: bool = True) -> pd.DataFrame:

    
    trump_sentences = pd.DataFrame(
        _read_sentences(os.path.join('data', 'trump.txt')),
        columns=['sentence']
    )
    bernie_sentences = pd.DataFrame(
        _read_sentences(os.path.join('data', 'bernie.txt')),
        columns=['sentence']
    )

    # Add labels
    trump_sentences.loc[:, 'is_trump'] = True
    bernie_sentences.loc[:, 'is_trump'] = False
    
    # Balance classes, if requested
    if len(trump_sentences) > len(bernie_sentences):
        trump_sentences = trump_sentences.sample(len(bernie_sentences))
    else:
        bernie_sentences = bernie_sentences.sample(len(trump_sentences))
    
    logging.info(f'Sentences for Trump: {len(trump_sentences)}')
    logging.info(f'Sentences for Bernie: {len(bernie_sentences)}')
    
    return pd.concat([trump_sentences, bernie_sentences], axis=0)
