import hashlib
import tempfile
from typing import cast

import strawberry.types
import upath
from dbt.contracts.graph.manifest import WritableManifest


class ManifestLoader:
    def __init__(self, manifest_path: upath.UPath) -> None:
        self.manifest_path = manifest_path
        self.manifest, self.hash = self.load()

    def load(self) -> tuple[WritableManifest, bytes]:
        content = self.manifest_path.read_bytes()
        hash = hashlib.md5(content).digest()
        with tempfile.NamedTemporaryFile() as tmp_file:
            tmp_file.write(content)
            manifest = WritableManifest.read_and_check_versions(tmp_file.name)
        return manifest, hash

    def refresh(self) -> bool:
        manifest, hash = self.load()
        if hash != self.hash:
            self.manifest = manifest
            self.hash = hash
            return True
        return False

    def current(self) -> WritableManifest:
        return self.manifest


def get_manifest(info: strawberry.types.Info) -> WritableManifest:
    return cast(WritableManifest, info.context["manifest"])
