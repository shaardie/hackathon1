from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt

user = 's5pguest'
password = 's5pguest'
url = 'https://scihub.copernicus.eu/dhus'
search_polygon = '../data/landkreis_osnabrueck.geojson'

api = SentinelAPI(user, password, url)
footprint = geojson_to_wkt(read_geojson(search_polygon))
products = api.query(footprint,
                     producttype='SLC',
                     orbitdirection='ASCENDING')

api.download_all(products)


