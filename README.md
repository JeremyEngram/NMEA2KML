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
pip3 install -r requirements.txt
```

## Usage

#### Import NMEA data from file and export to an KML file.
> <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/B0neShAd0w/Markdown/main/Blockquotes/Light-Theme/note.svg">
>   <img alt="Info" src="https://raw.githubusercontent.com/B0neShAd0w/Markdown/main/Blockquotes/Dark-Theme/note.svg">
> </picture><br>
>
> The Output file will be saved to the same directory where Input file resides.
```python
# This will outfile a file using the name as the input file (auto appended with .kml)
python NMEA2KML.py --input input_test_data.nmea

# Use a desired output file name name/location (make sure to add .kml extension!)
python NMEA2KML.py --input input_test_data.nmea --output output_data.kml
```
#### Load the outputted KML file into Google Earth Pro/Google Maps etc.

Google Earth Pro

![2023-06-12_11-02](https://github.com/B0neShAd0w/NMEA2KML/assets/117080369/65ab3c7d-3ff5-49f5-9ce5-2dec1a865d83)

Google Maps (My Maps)

![2023-06-12_10-58](https://github.com/B0neShAd0w/NMEA2KML/assets/117080369/5b9a1ed1-52f1-46f9-883a-ba2376aa17da)

## Planned features

- [X] None currently

<!-- CSV, SHP (shapefile), GeoJSON, KML, KMZ or TFRecord -->

## Contact
Feel free to contact me on <a href="https://twitter.com/B0neShad0w">Twitter</a>
