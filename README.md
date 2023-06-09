# NMEA2KML
NMEA2KML is a Python script that imports NMEA (National Marine Electronics Association) data via a file and outputs to KML (Keyhole Markup Language) format for use with Google Earth Pro, Google Maps & Bing Maps. \
This has purely been created for use with CTF's.

![Screenshot 2023-06-09 073559](https://github.com/B0neShAd0w/NMEA2KML/assets/117080369/a00faef7-5672-4ccb-8327-d4e3bd0793ef)

## Setup

#### Clone the repository
```shell
git clone https://github.com/B0neShad0w/NMEA2KML
cd NMEA2KML
```

#### Install requirements
```shell
pip install -r requirements.txt
```

## Usage

#### Import NMEA data from a file and export to an KML file.
```python
python NMEA2KML.py --input <INPUT_FILE> --output <OUTPUTFILE>
```

## Example

#### Import file named `nmea_data.nmea` & output to a file named `kml_data`
```python
# Note: the KML extension is automatically appended to the output file name.
python NMEA2KML.py --input nmea_data.nmea --output kml_data
```

## Planned features

- [X] None currently

<!-- CSV, SHP (shapefile), GeoJSON, KML, KMZ or TFRecord -->

## Contact
Feel free to contact me on <a href="https://twitter.com/B0neShad0w">Twitter</a>
