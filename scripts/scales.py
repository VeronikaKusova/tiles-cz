"""
Purpose: Script, which is calculating scales and resolutions for S-JTSK tile matrix sets
License: GNU/GPLv3
Author: Jachym Cepicky jachym.cepicky at opengeolabs.cz

Usage:

    python3 scales.py

Output: Tabular representation of zoom levels, scales and resolutions
Dependencies: pip3 install tabulate
"""

try:
    from tabulate import tabulate
except ModuleNotFoundError as e:
    tabulate = None
    print ("tabulate not installed, using `print`")

import json
import math

dpi = 90
maxscaledenom = 7315200

top = -920000
left = -925000
meters_per_inch = 0.0254
inch_per_meter = 1/meters_per_inch
tilesize = 256

dots_per_meter = dpi * inch_per_meter

tilesize_meters = tilesize / dots_per_meter

data = [
        [
        "zoom", "scaledenom", "resolution", "columns and rows", "bbox"
        ]
       ]

for zoom in range(0, 20):

    scaledenom = maxscaledenom/(2**zoom)

    cols_rows = 2**zoom

    tilesize_meters_scale = tilesize_meters * scaledenom

    resolution = tilesize_meters_scale/tilesize

    last_bbox = bbox = [left,  top - cols_rows * tilesize_meters_scale, left + cols_rows * tilesize_meters_scale , top]

    data.append([zoom, scaledenom, resolution, cols_rows, bbox])

if tabulate:
    print(tabulate(data))
else:
    for row in data:
        print("\t|".join([str(i) for i in row]))

geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "polygon",
                    "coordinates": [[
                        [ data[-1][-1][0], data[-1][-1][1] ],
                        [ data[-1][-1][2], data[-1][-1][1] ],
                        [ data[-1][-1][2], data[-1][-1][3] ],
                        [ data[-1][-1][0], data[-1][-1][3] ],
                        [ data[-1][-1][0], data[-1][-1][1] ],
                        ]]
                    }
            }
        ]
        }
print(json.dumps(geojson))

## decadic S-JTSK

data = [
        [
        "zoom", "scaledenom", "resolution", "columns and rows", "bbox"
        ]
       ]

scales = [
            10000000, 5000000, 2500000,
            1000000, 500000, 200000,
            100000, 50000, 25000,
            10000, 5000, 2000,
            1000, 500, 200,
            100, 50, 20,
            10, 5, 2,
            1
]

geojson = {
        "type": "FeatureCollection",
        "features": [
        ]
        }

for zoom in range(len(scales)):

    scaledenom = scales[zoom]

    tilesize_meters_scale = tilesize_meters * scaledenom
    width = last_bbox[2] - last_bbox[0]
    height = last_bbox[3] - last_bbox[1]
    tilesw = math.ceil(width/tilesize_meters_scale)
    tilesh = math.ceil(height/tilesize_meters_scale)
    #print(tilesize_meters_scale, tilesw, tilesh)

    cols_rows = tilesw

    resolution = tilesize_meters_scale/tilesize

    bbox = [left,  top - cols_rows * tilesize_meters_scale, left + cols_rows * tilesize_meters_scale , top]

    geojson["features"].append(
        {
            "type": "Feature",
            "properties": {
                "zoom": zoom,
                "resolution": resolution
            },
            "geometry": {
                "type": "polygon",
                "coordinates": [[
                    [ bbox[0], bbox[1] ],
                    [ bbox[2], bbox[1] ],
                    [ bbox[2], bbox[3] ],
                    [ bbox[0], bbox[3] ],
                    [ bbox[0], bbox[1] ],
                    ]]
                }
        }
    )

    data.append([zoom, scaledenom, resolution, cols_rows, bbox])

if tabulate:
    print(tabulate(data))
else:
    for row in data:
        print("\t|".join([str(i) for i in row]))

with open("/tmp/geojson-decadic.geojson", "w") as out:
    out.write(json.dumps(geojson))
