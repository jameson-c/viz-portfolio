# -*- coding: utf-8 -*-
"""
Creating GeoJSON Files from flight
"""
import csv, json
from geojson import Feature, FeatureCollection, Point

features = []
with open('C:/Users/jacar/OneDrive/Documents/Carnegie Mellon/Fall 2022/Telling Stories with Data/Final Project/Data/tri_2020_pa.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    print(reader)
    next(reader)
    for id, facility, latitude, longitude, sector, carcinogens in reader:
        latitude, longitude = map(float, (latitude, longitude))
        features.append(
            Feature(
                geometry = Point((longitude, latitude)),
                properties = {
                    'Facility Name': facility,
                    'Sector': sector,
                    'Carcinogenic Emissions': carcinogens
                }
            )
        )

collection = FeatureCollection(features)
with open("toxic_factories.json", "w") as f:
    f.write('%s' % collection)