import os
import requests
import gzip
import tempfile
import shutil
import netCDF4

def fetch_data(url,fname):
    file = fname
    if not os.path.exists(file):
        print("Downloading data ...")
        with open(file, "wb") as f:
            f.write(requests.get(url).content)
        print("Download data complete.")
    return file

def open_netcdf(fname):
    if fname.endswith(".gz"):
        infile = gzip.open(fname, 'rb')
        tmp = tempfile.NamedTemporaryFile(delete=False)
        shutil.copyfileobj(infile, tmp)
        infile.close()
        tmp.close()
        data = netCDF4.Dataset(tmp.name)
        os.unlink(tmp.name)
    else:
        data = netCDF4.Dataset(fname)
    return data
