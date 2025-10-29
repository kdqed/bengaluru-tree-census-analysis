import json
import zipfile

import h3
import geopandas as gpd
from kml2geojson import main as k2g
from pyproj import Geod
from shapely.geometry import shape as Shape, Point
import xmltodict

# First read and process corporation boundaries
corps = k2g.convert('corp_bounds.kml')[0]
with open('corp_bounds.geojson', 'w') as f:
    for feature in corps['features']:
        feature['properties']['name'] = feature['properties']['NewCorp'].lower()
        del feature['properties']['NewCorp']
    f.write(json.dumps(corps, indent=2))

corp_areas = {}
corp_shapes = {}
geod = Geod(ellps='WGS84')
for feature in corps['features']:
    corp = feature['properties']['name']
    corp_shapes[corp] = Shape(feature)
    
    # corp area will be in km^2
    corp_areas[corp] = abs(geod.geometry_area_perimeter(corp_shapes[corp])[0]/1000000) 

with open('corp_areas.json', 'w') as f:
    f.write(json.dumps(corp_areas, indent=2))

def coords_to_corp(coord):
    point = Point(coords[0], coords[1])
    for corp in corp_shapes:
        if corp_shapes[corp].contains(point):
            return corp

    return 'none'


# Second parse the KML file and convert to Geoparquet

features = []

with zipfile.ZipFile('raw_census_data.kmz') as kmz_file:
    with kmz_file.open('bbmp_tree_census_july2025.kml') as kml_file:
        xml_dict = xmltodict.parse(kml_file.read())
        count = 0
        for placemark in xml_dict['kml']['Document']['Folder']['Placemark']:
            count += 1
            print(count, end='\r'*10)
            coords = list(map(float, placemark['Point']['coordinates'].split(',')))
            properties = {}
            
            for obj in placemark['ExtendedData']['SchemaData']['SimpleData']:
                key = obj['@name']
                if key=='WardNumber':
                    properties['bbmp_WardNumber'] = obj['#text']
                else:
                    properties[key] = obj['#text']

            properties['h3_res7'] = h3.latlng_to_cell(coords[1], coords[0], 7)
            properties['h3_res8'] = h3.latlng_to_cell(coords[1], coords[0], 8)

            properties['gba_corporation'] = coords_to_corp(coords)
                
            features.append({
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': coords
                },
                'properties': properties
            })

gdf = gpd.read_file(json.dumps({'type': 'FeatureCollection', 'features': features}))
gdf.to_parquet('processed_census_data.parquet')

