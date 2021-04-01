from pypresence import Presence
import time
import ruamel.yaml
import os

class ConfigNotFound(Exception):
    pass
# The config not found exception.


class ConfigOpenError(Exception):
    pass
# The exception when the config cannot be opened.


class ClientIDNotProvided(Exception):
    pass
# The exception when a client ID is not provided.


def dict2class(_dict: dict):
    class DictBasedClass:
        def __getattribute__(self, item):
            self.__getattr__(item)

    for key in _dict:
        setattr(DictBasedClass, key, _dict[key])

    return DictBasedClass
# Converts a dictionary to a class.


def load_config(config_location: str):

    if not os.path.isfile(config_location):
        raise ConfigNotFound(
            "Could not find the config."
        )

    try:
        with open(config_location, "r", encoding="utf8") as file_stream:
            loaded_file = ruamel.yaml.load(file_stream, Loader=ruamel.yaml.Loader)
    except ruamel.yaml.YAMLError:
        raise ConfigOpenError(
            "The YAML config seems to be malformed."
        )
    except IOError:
        raise ConfigOpenError(
            "Could not open the config file."
        )
    except FileNotFoundError:
        raise ConfigNotFound(
            "Could not find the config."
        )

    return dict2class(loaded_file)


root = os.path.dirname(os.path.abspath(__file__))
config = load_config(root + "/config.yaml")

config.rpc['start'] = time.time()


client_id = config.client_id
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

def main():
    print("Updated RPC")
    while True:
        RPC.update(**config.rpc)  # Set the presence
        time.sleep(60)

main()