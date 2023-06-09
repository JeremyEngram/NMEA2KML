# NMEA2KML
NMEA2KML is a Python script that imports NMEA (National Marine Electronics Association) data via a file and outputs to KML (Keyhole Markup Language) format for use with Google Earth etc. This has purely been created for use in CTF's.

## Setup

#### Clone the repository
```shell
git clone https://github.com/B0neShad0w/NMEA2KML && cd NMEA2KML
```

#### Install requirements
```shell
pip install -r requirements.txt
```

## Usage

#### Import NMEA data from a file and export to an KML file.
```python
python NMEA2KML.py -i <INPUT_FILE> -o <OUTPUTFILE>
```

## Example

#### Import file named `nmea_data.nmea` & output to a file named `kml_data`
```python
# Note: the KML extension is automatically appended to the output file name.
python NMEA2KML.py -i nmea_data.nmea -o kml_data
```

## Planned features

- [ ] Export results in CSV
- [ ] Export results in SHP
- [ ] Export results in GeoJSON
- [ ] Export results in KMZ

<!-- CSV, SHP (shapefile), GeoJSON, KML, KMZ or TFRecord -->

## Contact
Feel free to contact me on <a href="https://twitter.com/B0neShad0w">Twitter</a>
