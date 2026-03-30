import json
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='underground_infra',
    user='postgres',
    password='Latitude'
)
cur = conn.cursor()

with open('../data/infrastructure.geojson', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

for feature in data['features']:
    geom = json.dumps(feature['geometry'])
    props = feature['properties']
    cur.execute('''
        INSERT INTO infrastructure (type, label, material, depth_m, install_year, status, geom)
        VALUES (%s, %s, %s, %s, %s, %s, ST_SetSRID(ST_GeomFromGeoJSON(%s), 4326))
        ON CONFLICT DO NOTHING
    ''', (
        props.get('type'),
        props.get('label'),
        props.get('material'),
        props.get('depth_m'),
        props.get('install_year'),
        props.get('status'),
        geom
    ))

conn.commit()
cur.close()
conn.close()
print('Data loaded successfully - ' + str(len(data['features'])) + ' features inserted')