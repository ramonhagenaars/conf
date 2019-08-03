try:
    import yaml
except ImportError:
    pass


def parse(file_stream):
    # Parse the given file stream of yaml format to a dict.
    loaded = yaml.load(file_stream, Loader=yaml.FullLoader)
    if loaded:
        return dict(loaded.items())
    return {}
