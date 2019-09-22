import gdal

# Path of netCDF file
# note: this data file is not in the repo, it was retrieved from:
# https://data.lkiesow.io/emissions-api/
file_name = "data/S5P_NRTI_L2__CO_____20190921T104303_20190921T104803_10045_01_010302_20190921T124803.nc"

# Specify the layer name to read
layer_name = "//PRODUCT/carbonmonoxide_total_column"

# Open netcdf file.nc with gdal
ds = gdal.Open("HDF5:{}:{}".format(file_name, layer_name))

# read data using raster size
data = ds.ReadAsArray()
print(data)
