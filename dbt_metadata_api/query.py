from typing import Annotated

import strawberry
import strawberry.types

from .types import (
    ExposureNode,
    MacroNode,
    MetricNode,
    ModelNode,
    SeedNode,
    SnapshotNode,
    SourceNode,
    TestNode,
    convert_to_strawberry,
)
from .utils import get_manifest


@strawberry.type
class Query:
    @strawberry.field
    def exposures(self, info: strawberry.types.Info) -> list[ExposureNode]:
        manifest = get_manifest(info)
        return [
            convert_to_strawberry(unique_id, "exposure")
            for unique_id in manifest.exposures
        ]

    @strawberry.field
    def exposure(
        self,
        unique_id: Annotated[
            str, strawberry.argument(description="The unique_id of this exposure")
        ],
        info: strawberry.types.Info,
    ) -> ExposureNode:
        return convert_to_strawberry(unique_id, "exposure")

    @strawberry.field
    def macros(self, info: strawberry.types.Info) -> list[MacroNode]:
        manifest = get_manifest(info)
        return [
            convert_to_strawberry(unique_id, "macro") for unique_id in manifest.macros
        ]

    @strawberry.field
    def macro(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular macro"),
        ],
        info: strawberry.types.Info,
    ) -> MacroNode:
        return convert_to_strawberry(unique_id, "macro")

    @strawberry.field
    def metrics(self, info: strawberry.types.Info) -> list[MetricNode]:
        manifest = get_manifest(info)
        return [
            convert_to_strawberry(unique_id, "metric") for unique_id in manifest.metrics
        ]

    @strawberry.field
    def metric(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular metric"),
        ],
        info: strawberry.types.Info,
    ) -> MetricNode:
        return convert_to_strawberry(unique_id, "metric")

    @strawberry.field
    def models(self, info: strawberry.types.Info) -> list[ModelNode]:
        manifest = get_manifest(info)
        return [
            convert_to_strawberry(unique_id, "model")
            for unique_id, node in manifest.nodes.items()
            if node.resource_type.name == "model"
        ]

    @strawberry.field
    def model(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular model"),
        ],
        info: strawberry.types.Info,
    ) -> ModelNode:
        return convert_to_strawberry(unique_id, "model")

    @strawberry.field
    def seeds(self, info: strawberry.types.Info) -> list[SeedNode]:
        manifest = get_manifest(info)
        return [
            convert_to_strawberry(unique_id, "seed")
            for unique_id, node in manifest.nodes.items()
            if node.resource_type.name == "seed"
        ]

    @strawberry.field
    def seed(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular seed"),
        ],
    ) -> SeedNode:
        return convert_to_strawberry(unique_id, "seed")

    @strawberry.field
    def snapshots(self, info: strawberry.types.Info) -> list[SnapshotNode]:
        manifest = get_manifest(info)
        return [
            convert_to_strawberry(unique_id, "snapshot")
            for unique_id, node in manifest.nodes.items()
            if node.resource_type.name == "snapshot"
        ]

    @strawberry.field
    def snapshot(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular model"),
        ],
    ) -> SnapshotNode:
        return convert_to_strawberry(unique_id, "snapshot")

    @strawberry.field
    def sources(self, info: strawberry.types.Info) -> list[SourceNode]:
        manifest = get_manifest(info)
        return [
            convert_to_strawberry(unique_id, "source")
            for unique_id in manifest.sources.values()
        ]

    @strawberry.field
    def source(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular source"),
        ],
    ) -> SourceNode:
        return convert_to_strawberry(unique_id, "source")

    @strawberry.field
    def tests(self, info: strawberry.types.Info) -> list[TestNode]:
        manifest = get_manifest(info)
        return [
            convert_to_strawberry(unique_id, "test")
            for unique_id, node in manifest.nodes.items()
            if node.resource_type.name == "test"
        ]

    @strawberry.field
    def test(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular test"),
        ],
        info: strawberry.types.Info,
    ) -> TestNode:
        return convert_to_strawberry(unique_id, "test")
