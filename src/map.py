import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Get geo data
shp_filepath = "./data/nycb2020_23c/nycb2020.shp"
ny_tracts = gpd.read_file(shp_filepath)

# Clean geo data
ny_tracts.columns = map(str.lower, ny_tracts.columns)
ny_tracts["bctcb2020"] = ny_tracts["bctcb2020"].astype(float)

# Get owner data
cols = ["bct2020", "bctcb2020", "xcoord", "ycoord", "latitude", "longitude", "ownertype", "ownername"]
filepath = "./data/Primary_Land_Use_Tax_Lot_Output__PLUTO__20231115.csv"
df = pd.read_csv(filepath, usecols=cols)

# Clean owner data
df.apply(lambda col:pd.to_numeric(col, errors='coerce'))

# Merge geo and owner data
merged = df.merge(ny_tracts, on="bctcb2020", how="left")

# Save data
merged.to_csv("plotting_data.csv")

# Map data
fig, ax2 = plt.subplots(figsize=(30,18))
ax2.set_title('Land Ownership NYC')
mergedMap = gpd.GeoDataFrame(merged)
mergedMap.plot(
    column="ownertype",
    legend=True,
    ax=ax2,
)
fig.savefig("nyc-land-ownership-map.png", format='png')
