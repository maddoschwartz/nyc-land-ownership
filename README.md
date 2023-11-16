# README

This project uses public data from NYC to generate a map of the land ownership in the region.

## Data

Sources:
- [Primary Land Use Tax Lot Output (PLUTO)](https://data.cityofnewyork.us/City-Government/Primary-Land-Use-Tax-Lot-Output-PLUTO-/64uk-42ks)
- [2020 Census Blocks (Clipped to Shoreline) Data ](https://www.nyc.gov/site/planning/data-maps/open-data/census-download-metadata.page)


Data of interest from PLUTO Dataset (see data/PLUTODD.pdf)
- OwnerType: A code indicating type of ownership for the tax lot

| OwnerType Code | Meaning          |
| ---------------|------------------|
| C              | City ownership   |
| M              | Mixed city & private ownership |
| O              | Other – owned by either a public authority or the state or federal government |
| P              | Private ownership |
| X              | Fully tax-exempt property that may be owned by the city, state, or federal government; a public authority; or a private institution |
| blank          | Unknown (usually private ownership) |


## Coding Resources

- Geopandas: https://geopandas.org/en/stable/docs/reference
- Pandas: https://pandas.pydata.org/docs/reference/api

## Getting Started

Download the data and place it in the `data` directory.

Install latest version of Python: https://www.python.org/downloads/

Create virtual environment, which is an isolated location for package management.
```
python3 -m venv venv
source venv/bin/activate
```

Install Python libraries
```
pip3 install -r requirements.txt
```

Run Python script
```
python3 data.py
```

View output at nyc-land-ownership-map.png

## Future Work

Future work could include:

1. Aggregating and displaying public land-owners

    There are some public land-owners that could be of interest
    - STATE UNIVERSITY OF (of what??)
    - UNITED STATES OF AMERICA
    - NEW YORK STATE DEPARTMENT
    - NYC DEPARTMENT OF TRANSPORTATION

2. Map an overlay of LandUse

    Some values in the data include Transportaiton/Utility, Industrial/Manufacturing, etc.

4. Making the map interactive

    Make a map that lets you zoom in-out and hover over to discover more information.
