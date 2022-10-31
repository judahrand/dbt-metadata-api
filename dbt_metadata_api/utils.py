import hashlib
import json
import pathlib
from typing import Union

from dbt_artifacts_parser.parser import (
    ManifestV5,
    ManifestV6,
    ManifestV7,
    parse_manifest,
)

from .models.manifest import Model as Manifest

Manifest = Union[
    ManifestV5,
    ManifestV6,
    ManifestV7,
]

MANIFEST_PATH = pathlib.Path("./manifest_v7.json")


class ManifestLoader:
    def __init__(self, manifest_path: pathlib.Path) -> None:
        self.manifest_path = manifest_path
        self.manifest, self.hash = self.load()

    def load(self) -> tuple[Manifest, bytes]:
        content = self.manifest_path.read_text()
        hash = hashlib.md5(content.encode("UTF-8")).digest()
        return parse_manifest(json.loads(content)), hash

    def refresh(self) -> bool:
        manifest, hash = self.load()
        if hash != self.hash:
            print("MANIFEST CHANGED RELOAD")
            self.manifest = manifest
            self.hash = hash
            return True
        return False
