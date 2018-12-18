"""
This module contains the parsers that parse file streams to dicts.
"""
import configparser
import json
import yaml


def parse_from_yaml(file_stream):
    # Parse the given file stream of yaml format to a dict.
    loaded = yaml.load(file_stream)
    if loaded:
        return dict(loaded.items())
    return {}


def parse_from_json(file_stream):
    # Parse the given file stream of json format to a dict.
    return json.load(file_stream)


def parse_from_ini(file_stream):
    # Parse the given file stream of ini format to a dict.
    parser = configparser.ConfigParser()
    parser.read_file(file_stream)
    return {section: dict(parser[section].items())
            for section in parser.sections()}
