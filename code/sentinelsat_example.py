from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt

user = 's5pguest'
password = 's5pguest'
url = 'https://s5phub.copernicus.eu/dhus'
search_polygon = './data/landkreis_osnabrueck.geojson'
start_date = '20190910'
end_date = '20190911'

# query api for available products
api = SentinelAPI(user, password, url)
footprint = geojson_to_wkt(read_geojson(search_polygon))
products = api.query(area=footprint,
                     date=(start_date, end_date))

# convert to panas data frame
products_df = api.to_dataframe(products)

# inspect data
products_df.head()  # view top of df
products_df.columns  # show column names

# filter only one product of CO
where = products_df.producttypedescription == 'Carbon Monoxide'
one_id = products_df.uuid[where][0]

# download one product
api.download(one_id)


