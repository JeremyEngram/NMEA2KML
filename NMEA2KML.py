import sys
import argparse
import os

from colorama import Fore

def right_fields(line):
    tag_info = {
        "name": "",
        "n_fields": 0
    }

    if(line.startswith('$GPGGA')):
        tag_info["name"] = "GPGGA"
        tag_info["n_fields"] = 15

    elif(line.startswith('$GPRMC')):
        tag_info["name"] = "GPRMC"
        tag.info["n_fields"] = 12

    fields = line.split(",")
    if len(fields) == tag_info["n_fields"]:
        return line
    else:
        return None

def valid_line(line):
    checksum = 0

    line_checksum = line[-2:]
    try:
        line_checksum = int(line_checksum, 16)
    except ValueError:
        return False

    for char in line[1:-3]:
        checksum ^= ord(char)

    if checksum == line_checksum:
        return True

    return False

def extract_coordinates(input_string):
    gpgga_coordinates_list = []
    gpgsa_coordinates_list = []
    gprmc_coordinates_list = []

    lines = input_string.strip().split('\n')

    for line in lines:
        if valid_line(line) == False:
            continue

        line = line.strip()
        fields = line.split(',')

        # the line is valid when it has the correct number of fields
        line = right_fields(line)
        if line == None:
            continue

        print(line)

        if line.startswith('$GPGGA'):
            if len(fields) >= 10:
                latitude = fields[2]
                latitude_direction = fields[3]
                longitude = fields[4]
                longitude_direction = fields[5]
                # Convert latitude to decimal format
                latitude_decimal = float(latitude[:2]) + (float(latitude[2:]) / 60)
                if latitude_direction == 'S':
                    latitude_decimal *= -1  # Convert to negative if south
                # Convert longitude to decimal format
                longitude_decimal = float(longitude[:3]) + (float(longitude[3:]) / 60)
                if longitude_direction == 'W':
                    longitude_decimal *= -1  # Convert to negative if west
                gpgga_coordinates_list.append((latitude_decimal, longitude_decimal))

        elif line.startswith('$GPRMC'):
            if len(fields) >= 4:
                latitude = fields[3]
                latitude_direction = fields[4]
                longitude = fields[5]
                longitude_direction = fields[6]
                # Convert latitude to decimal format
                latitude_decimal = float(latitude[:2]) + (float(latitude[2:]) / 60)
                if latitude_direction == 'S':
                    latitude_decimal *= -1  # Convert to negative if south
                # Convert longitude to decimal format
                longitude_decimal = float(longitude[:3]) + (float(longitude[3:]) / 60)
                if longitude_direction == 'W':
                    longitude_decimal *= -1  # Convert to negative if west
                gprmc_coordinates_list.append((latitude_decimal, longitude_decimal))

    return gpgga_coordinates_list, gpgsa_coordinates_list, gprmc_coordinates_list

def write_coordinates_to_kml(file_path, gpgga_coordinates, gpgsa_coordinates, gprmc_coordinates):
    try:
        output_file_path = file_path
        with open(output_file_path, 'w') as file:  # Use 'w' mode to overwrite file
            file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            file.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
            file.write('<Document>\n')
            file.write('<name>Extracted Coordinates</name>\n')

            # Write GPGGA coordinates
            file.write('<Folder>\n')
            file.write('<name>GPGGA Coordinates</name>\n')
            for i, coordinate in enumerate(gpgga_coordinates):
                file.write('<Placemark>\n')
                file.write(f'<name>GPGGA {i+1}</name>\n')
                file.write('<Point>\n')
                file.write(f'<coordinates>{coordinate[1]},{coordinate[0]},0</coordinates>\n')
                file.write('</Point>\n')
                file.write('</Placemark>\n')
            file.write('</Folder>\n')

            # Write GPGSA coordinates
            file.write('<Folder>\n')
            file.write('<name>GPGSA Coordinates</name>\n')
            for i, coordinate in enumerate(gpgsa_coordinates):
                file.write('<Placemark>\n')
                file.write(f'<name>GPGSA {i+1}</name>\n')
                file.write('<Point>\n')
                file.write(f'<coordinates>{coordinate[1]},{coordinate[0]},0</coordinates>\n')
                file.write('</Point>\n')
                file.write('</Placemark>\n')
            file.write('</Folder>\n')

            # Write GPRMC coordinates
            file.write('<Folder>\n')
            file.write('<name>GPRMC Coordinates</name>\n')
            for i, coordinate in enumerate(gprmc_coordinates):
                file.write('<Placemark>\n')
                file.write(f'<name>GPRMC {i+1}</name>\n')
                file.write('<Point>\n')
                file.write(f'<coordinates>{coordinate[1]},{coordinate[0]},0</coordinates>\n')
                file.write('</Point>\n')
                file.write('</Placemark>\n')
            file.write('</Folder>\n')

            file.write('</Document>\n')
            file.write('</kml>\n')
    except IOError:
        print(f"Error: Failed to write to file '{output_file_path}'!")

def main(args):
    input_file_path = args.input
    output_file_path = args.output

    if output_file_path is None:
        output_file_path = input_file_path + ".kml"

    try:
        with open(input_file_path, 'r') as file:
            input_string = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found!")
        sys.exit(1)

    if not input_string.strip():
        print("Warning: Empty input file!")
    else:
        gpgga_coordinates, gpgsa_coordinates, gprmc_coordinates = extract_coordinates(input_string)
        write_coordinates_to_kml(output_file_path, gpgga_coordinates, gpgsa_coordinates, gprmc_coordinates)
        print(f"\033[0m [+] - Coordinates written to '{output_file_path}' file.\n")

def print_help(parser):
    parser.print_help()
    sys.exit()

if __name__ == '__main__':

    print(Fore.WHITE + """
    
    ███╗   ██╗███╗   ███╗███████╗ █████╗ ██████╗ ██╗  ██╗███╗   ███╗██╗     
    ████╗  ██║████╗ ████║██╔════╝██╔══██╗╚════██╗██║ ██╔╝████╗ ████║██║     
    ██╔██╗ ██║██╔████╔██║█████╗  ███████║ █████╔╝█████╔╝ ██╔████╔██║██║     
    ██║╚██╗██║██║╚██╔╝██║██╔══╝  ██╔══██║██╔═══╝ ██╔═██╗ ██║╚██╔╝██║██║     
    ██║ ╚████║██║ ╚═╝ ██║███████╗██║  ██║███████╗██║  ██╗██║ ╚═╝ ██║███████╗
    ╚═╝  ╚═══╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
    
        Created by """ + Fore.WHITE + "BoΠeShΔdϴw³ | https://github.com/B0neShAd0w/NMEA2KML\n")

    parser = argparse.ArgumentParser(description="Extract coordinates and generate KML file")
    parser.add_argument('--input', help='nmea format input file')
    parser.add_argument('--output', help='kml format output file')

    args = parser.parse_args()

    if not any(vars(args).values()):
        print_help(parser)

    if args.input is None:
        print("Error: --input parameter is required.")
        print_help(parser)

    main(args)
