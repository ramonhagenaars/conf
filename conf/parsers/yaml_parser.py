try:
    import yaml
except ImportError:
    pass


def parse(file_stream):
    """
    Parse the given file stream of yaml format to a dict.
    """
    major, minor = [int(i) for i in yaml.__version__.split('.')][0:2]

    if (major == 5 and minor >= 1) or (major > 5):
        loaded = yaml.load(file_stream, Loader=yaml.FullLoader)
    else:
        loaded = yaml.load(file_stream)

    if loaded:
        return dict(loaded.items())
    return {}
