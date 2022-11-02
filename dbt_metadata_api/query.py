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
)
from .utils import get_manifest


@strawberry.type
class Query:
    @strawberry.field
    def exposures(self, info: strawberry.types.Info) -> list[ExposureNode]:
        manifest = get_manifest(info)
        return [ExposureNode(unique_id=unique_id) for unique_id in manifest.exposures]

    @strawberry.field
    def exposure(
        self,
        unique_id: Annotated[
            str, strawberry.argument(description="The unique_id of this exposure")
        ],
        info: strawberry.types.Info,
    ) -> ExposureNode:
        return ExposureNode(unique_id=unique_id)

    @strawberry.field
    def macros(self, info: strawberry.types.Info) -> list[MacroNode]:
        manifest = get_manifest(info)
        return [MacroNode(unique_id=unique_id) for unique_id in manifest.macros]

    @strawberry.field
    def macro(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular macro"),
        ],
        info: strawberry.types.Info,
    ) -> MacroNode:
        return MacroNode(unique_id=unique_id)

    @strawberry.field
    def metrics(self, info: strawberry.types.Info) -> list[MetricNode]:
        manifest = get_manifest(info)
        return [MetricNode(unique_id=unique_id) for unique_id in manifest.metrics]

    @strawberry.field
    def metric(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular metric"),
        ],
        info: strawberry.types.Info,
    ) -> MetricNode:
        return MetricNode(unique_id=unique_id)

    @strawberry.field
    def models(self, info: strawberry.types.Info) -> list[ModelNode]:
        manifest = get_manifest(info)
        return [
            ModelNode(unique_id=unique_id)
            for unique_id, node in manifest.nodes.items()
            if node.resource_type == "model"
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
        return ModelNode(unique_id=unique_id)

    @strawberry.field
    def seeds(self, info: strawberry.types.Info) -> list[SeedNode]:
        manifest = get_manifest(info)
        return [
            SeedNode(unique_id=unique_id)
            for unique_id, node in manifest.nodes.items()
            if node.resource_type == "seed"
        ]

    @strawberry.field
    def seed(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular seed"),
        ],
    ) -> SeedNode:
        return SeedNode(unique_id=unique_id)

    @strawberry.field
    def snapshots(self, info: strawberry.types.Info) -> list[SnapshotNode]:
        manifest = get_manifest(info)
        return [
            SnapshotNode(unique_id=unique_id)
            for unique_id, node in manifest.nodes.items()
            if node.resource_type == "snapshot"
        ]

    @strawberry.field
    def snapshot(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular model"),
        ],
    ) -> SnapshotNode:
        return SnapshotNode(unique_id=unique_id)

    @strawberry.field
    def sources(self, info: strawberry.types.Info) -> list[SourceNode]:
        manifest = get_manifest(info)
        return [
            SourceNode(unique_id=unique_id) for unique_id in manifest.sources.keys()
        ]

    @strawberry.field
    def source(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular source"),
        ],
    ) -> SourceNode:
        return SourceNode(unique_id=unique_id)

    @strawberry.field
    def tests(self, info: strawberry.types.Info) -> list[TestNode]:
        manifest = get_manifest(info)
        return [
            TestNode(unique_id=unique_id)
            for unique_id, node in manifest.nodes.items()
            if node.resource_type == "test"
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
        return TestNode(unique_id=unique_id)
