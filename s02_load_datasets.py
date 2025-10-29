import base64
import json
import zipfile

import geopandas as gpd

my_logo = base64.b64encode(open('logo-dark.png', 'rb').read())
my_logo_b64 = 'data:image/png;base64,{}'.format(my_logo.decode())
corps = gpd.read_file('corp_bounds.geojson')
corp_areas = json.loads(open('corp_areas.json').read())

trees = gpd.read_parquet('processed_census_data.parquet')

