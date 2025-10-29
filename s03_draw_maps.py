from pathlib import Path

import h3
import plotly.express as px
import shapely

from s02_load_datasets import *


def reverse_coord_order(line_string):
    return [p[::-1] for p in line_string]


def idx_to_polygon(idx):
    coords = h3.cell_to_boundary(idx)
    coords = [coord[::-1] for coord in coords]
    return shapely.Polygon(coords)


def geom_to_cells(geom, res):
    obj = json.loads(shapely.to_geojson(geom))
    if obj['type']=='Polygon':
        polygons = [obj['coordinates']]
    if obj['type']=='GeometryCollection':
        polygons = [g['coordinates'] for g in obj['geometries']]
    
    cells = set()
    for polygon in polygons:
        shell = reverse_coord_order(polygon[0])
        holes = []
        if len(polygon) > 1:
            holes = [reverse_coord_order(ls) for ls in polygon[1:]]
        h3shape = h3.LatLngPoly(shell, *holes)
        cells.update(h3.polygon_to_cells(h3shape, res))
    
    return list(cells)


def fix_geometry_type(geom):
    if geom.geom_type == 'GeometryCollection':
        return shapely.MultiPolygon(geom.geoms)
    else:
        return geom


def draw_choropleth(df, color_column, title, filename):
    geometries = df.geometry.apply(fix_geometry_type)
    fig = px.choropleth(
        df,
        geojson=geometries,
        locations=df.index,
        color=color_column,
        color_continuous_scale=px.colors.sequential.BuGn,
    )

    fig.update_layout(
        title_text = title,
        title_xref = 'paper', title_yref = 'paper',
        title_x = 0, title_y = 0.95,
        title_yanchor = 'middle',
        title_font_family = 'JetBrainsMono Nerd Font',
        title_font_weight = 500,
        title_font_size = 16,
        legend_title_font_size = 12,
        font = dict(
            family = "JetBrainsMono Nerd Font",
            size = 12,
        )
    )

    fig.layout.images = [dict(
        source=my_logo_b64,
        xref="paper", yref="paper",
        x=0.0, y=0.05,
        sizex=0.1, sizey=0.1,
        xanchor="left", yanchor="middle"
    )]

    fig.add_annotation(
        xref='paper', yref='paper',
        yanchor='middle',
        x=0.1, y=0.05,
        text='© Karthik Devan (kdqed.com)',
        showarrow=False,
        font=dict(
            family='JetBrainsMono Nerd Font',
            size=16,
        )
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.write_image(Path('results') / filename)


def map_for_corporation(corp):
    cells = geom_to_cells(corp['geometry'], 8)
    h3df = gpd.GeoDataFrame({
        'h3': cells,
        'geometry': list(map(idx_to_polygon, cells)),
        'Tree Count': [0] * len(cells)
    }, geometry='geometry')
    
    cell_counts = trees[trees['gba_corporation'] == corp['name']][['h3_res8']].groupby(by='h3_res8').value_counts()
    cell_counts = cell_counts.reset_index(name='Count')
    
    def update_count(r):
        h3df.loc[ h3df['h3'] == r['h3_res8'], 'Tree Count' ] = r['Count']
        
    cell_counts.apply(update_count, axis=1)
    p_name = corp['name'][0].upper() + corp['name'][1:]
    draw_choropleth(h3df, 'Tree Count', 
        f'BLR {p_name} Corporation: Density Map of Census Trees',
        f'density_map_{corp["name"]}.png'
    )

corps.apply(map_for_corporation, axis=1)

# do full BLR map
cell_lists = list(corps['geometry'].map(lambda geom: geom_to_cells(geom, 7)))
cells = list(set([cell for cell_list in cell_lists for cell in cell_list]))

h3df = gpd.GeoDataFrame({
    'h3': cells,
    'geometry': list(map(idx_to_polygon, cells)),
    'Tree Count': [0] * len(cells)
}, geometry='geometry')

cell_counts = trees[['h3_res7']].groupby(by='h3_res7').value_counts()
cell_counts = cell_counts.reset_index(name='Count')

def update_count(r):
    h3df.loc[ h3df['h3'] == r['h3_res7'], 'Tree Count' ] = r['Count']
        
cell_counts.apply(update_count, axis=1)
draw_choropleth(h3df, 'Tree Count', 
    f'Bengaluru GBA Area: Density Map of Census Trees',
    f'density_map_blr_wide.png'
)
