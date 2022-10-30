import json
import pathlib

from .models.manifest import Model as Manifest

MANIFEST = Manifest(
    **json.loads(pathlib.Path("./manifest.json").read_text()),
)


def get_manifest() -> Manifest:
    return MANIFEST
