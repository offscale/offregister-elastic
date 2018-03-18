offregister_elastic
====================
This package follows the offregister specification for Elastic (elasticsearch).

## Install dependencies

    pip install -r requirements.txt

## Install package

    pip install .

## Example config

    {
        "module": "offregister-elastic",
        "type": "fabric",
        "kwargs": {
            "VERSION": "0.90.13",
            "NO_UPGRADE": true
        }
    }

To setup your environment to use this config, follow [the getting started guide](https://offscale.io/docs/getting-started).

## Roadmap

  - Additional users and passwords
  - Custom config
  - Clustering
