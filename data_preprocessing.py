"""
This python script preprocesses data into torch datasets that can then be used for training    
"""

import torch
import numpy as np
import xarray as xr

class GebcoDataset(torch.utils.data.Dataset):
    """Data Container for the gebco bathymetry data set

    Args:
        torch (Dataset): stores the gebco dataset in an xarray for fast processing
    """
    def __init__(self, netcdf_path):
        self.ds = xr.open_dataset(netcdf_path)
        self.elev_da = self.ds['elevation']
        self.lats = self.ds['lat'].values
        self.lons = self.ds['lon'].values
        
        # Print coordinate info for debugging
        print(f"Latitude range: {self.lats.min():.2f} to {self.lats.max():.2f}")
        print(f"Longitude range: {self.lons.min():.2f} to {self.lons.max():.2f}")
        print(f"Lat ascending: {self.lats[0] < self.lats[-1]}")
        
    def __len__(self):
        return len(self.lats) * len(self.lons)

    def __getitem__(self, bbox):
        lat_min, lat_max, lon_min, lon_max = bbox
        print(f"Requested bbox: lat({lat_min}, {lat_max}), lon({lon_min}, {lon_max})")
        
        # Handle longitude conversion if dataset uses 0-360
        if self.lons.min() >= 0 and lon_min < 0:
            lon_min = lon_min + 360
            lon_max = lon_max + 360
            print(f"Converted to 0-360: lon({lon_min}, {lon_max})")
        
        # Determine latitude slice order (depends on whether coords are ascending/descending)
        if self.lats[0] > self.lats[-1]:  # Descending latitudes
            lat_slice = slice(lat_max, lat_min)
        else:  # Ascending latitudes
            lat_slice = slice(lat_min, lat_max)
            
        lon_slice = slice(lon_min, lon_max)
        
        # Select subset
        elev_subset_da = self.elev_da.sel(lat=lat_slice, lon=lon_slice)
        
        print(f"Selected {len(elev_subset_da.lat)} lats, {len(elev_subset_da.lon)} lons")
        print(f"Actual lat range: {elev_subset_da.lat.values}")
        print(f"Actual lon range: {elev_subset_da.lon.values}")
        
        # Convert to tensors
        elev_subset = torch.from_numpy(elev_subset_da.values.astype(np.float32))
        lat_subset = torch.from_numpy(elev_subset_da['lat'].values.astype(np.float32))
        lon_subset = torch.from_numpy(elev_subset_da['lon'].values.astype(np.float32))
        
        return elev_subset, lat_subset, lon_subset
    

class SeisCRUSTDataset(torch.utils.data.Dataset):
    # TODO : implement
    pass

class ecm1Dataset(torch.utils.data.Dataset):
    # TODO : implement
    pass