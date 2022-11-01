import hashlib
import pathlib
from typing import cast

import strawberry.types
from dbt.contracts.graph.manifest import WritableManifest


class ManifestLoader:
    def __init__(self, manifest_path: pathlib.Path) -> None:
        self.manifest_path = manifest_path
        self.manifest, self.hash = self.load()

    def load(self) -> tuple[WritableManifest, bytes]:
        manifest = WritableManifest.read_and_check_versions(str(self.manifest_path))
        hash = hashlib.md5(self.manifest_path.read_text().encode("UTF-8")).digest()
        return manifest, hash

    def refresh(self) -> bool:
        manifest, hash = self.load()
        if hash != self.hash:
            print("MANIFEST CHANGED RELOAD")
            self.manifest = manifest
            self.hash = hash
            return True
        return False

    def current(self) -> WritableManifest:
        return self.manifest


def get_manifest(info: strawberry.types.Info) -> WritableManifest:
    return cast(info.context["manifest"], WritableManifest)
