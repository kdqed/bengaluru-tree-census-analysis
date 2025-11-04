from pathlib import Path

from s02_load_datasets import *

RESULTS = Path('results')

for corp in ['blr'] + list(corp_areas.keys()):
    df = trees if corp=='blr' else trees[trees['gba_corporation'] == corp]
    total_trees = df.shape[0]
    
    tree_grouping = df[['TreeName']].groupby(by='TreeName').value_counts()
    tree_counts = tree_grouping.sort_values(ascending=False).reset_index(name='Count')
    tree_counts['Percentage'] = tree_counts['Count'].apply(
        lambda c: round(100*c/total_trees, 1)
    )
    tree_counts.sort_values(by='Percentage', ascending=False)
    tree_counts.to_markdown(RESULTS / f'{corp}_species_frequency.md', index=False)
