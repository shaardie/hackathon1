import gdal

from geojson import Feature, Point, FeatureCollection, dump

# Path of netCDF file
# note: this data file is not in the repo, it was retrieved from:
# https://data.lkiesow.io/emissions-api/
file_name = "data/S5P_NRTI_L2__CO_____20190921T104303_20190921T104803_10045_01_010302_20190921T124803.nc"  # noqa

# Specify the layer name to rea
data_name = "//PRODUCT/carbonmonoxide_total_column"
longitude_name = "//PRODUCT/longitude"
latitude_name = "//PRODUCT/latitude"


def main():
    # Open netcdf file.nc with gdal
    data = gdal.Open("HDF5:{}:{}".format(file_name, data_name)).ReadAsArray()
    longitude = gdal.Open(
        "HDF5:{}:{}".format(file_name, longitude_name)).ReadAsArray()
    latitude = gdal.Open(
        "HDF5:{}:{}".format(file_name, latitude_name)).ReadAsArray()

    feature_list = []
    shape = data.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            feature_list.append(
                Feature(
                    geometry=Point(
                        (float(longitude[i, j]), float(latitude[i, j]))),
                    properties={"CO": float(data[i, j])}
                )
            )

    fc = FeatureCollection(feature_list)
    with open("geojson.json", 'w') as f:
        dump(fc, f)


if __name__ == '__main__':
    main()
