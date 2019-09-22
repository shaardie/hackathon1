from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt

user = 's5pguest'
password = 's5pguest'
url = 'https://s5phub.copernicus.eu/dhus'
search_polygon = './data/landkreis_osnabrueck.geojson'
start_date = '20190101'
end_date = '20190201'

api = SentinelAPI(user, password, url)
footprint = geojson_to_wkt(read_geojson(search_polygon))
products = api.query(area = footprint, 
                     date=(start_date, end_date))

api.download_all(products)


