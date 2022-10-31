from re import M
from typing import Annotated

import strawberry

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
    def exposures(self) -> list[ExposureNode]:
        manifest = get_manifest()
        return [
            convert_to_strawberry(manifest, node)
            for node in manifest.exposures.values()
        ]

    @strawberry.field
    def exposure(
        self,
        unique_id: Annotated[
            str, strawberry.argument(description="The unique_id of this exposure")
        ],
    ) -> ExposureNode:
        manifest = get_manifest()
        return convert_to_strawberry(manifest, manifest.exposures[unique_id])

    @strawberry.field
    def macros(self) -> list[MacroNode]:
        manifest = get_manifest()
        return [
            convert_to_strawberry(manifest, node)
            for node in manifest.macros.values()
        ]

    @strawberry.field
    def macro(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular macro"),
        ],
    ) -> MacroNode:
        manifest = get_manifest()
        return convert_to_strawberry(
            manifest,
            manifest.macros[unique_id],
        )

    @strawberry.field
    def metrics(self) -> list[MetricNode]:
        manifest = get_manifest()
        return [
            convert_to_strawberry(manifest, unique_id)
            for unique_id in manifest.metrics.values()
        ]

    @strawberry.field
    def metric(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular metric"),
        ],
    ) -> MetricNode:
        manifest = get_manifest()
        return convert_to_strawberry(manifest, manifest.metrics[unique_id])

    @strawberry.field
    def models(self) -> list[ModelNode]:
        manifest = get_manifest()
        return [
            convert_to_strawberry(manifest, node)
            for node in manifest.nodes.values()
            if node.resource_type.value == "model"
        ]

    @strawberry.field
    def model(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular model"),
        ],
    ) -> ModelNode:
        manifest = get_manifest()
        return convert_to_strawberry(
            manifest,
            manifest.nodes[unique_id],
            expected_resource_type="model",
        )

    # @strawberry.field
    # def seeds(self) -> list[SeedNode]:
    #     return [
    #         SeedNode.from_pydantic(node)
    #         for node in get_manifest().nodes.values()
    #         if node.resource_type.value == "seed"
    #     ]

    # @strawberry.field
    # def seed(
    #     self,
    #     unique_id: Annotated[
    #         str,
    #         strawberry.argument(description="The unique ID of this particular seed"),
    #     ],
    # ) -> SeedNode:
    #     node = get_manifest().nodes[unique_id]
    #     if node.resource_type.value == "seed":
    #         raise ValueError(f"No seed called {unique_id} found")
    #     return SeedNode.from_pydantic(node)

    # @strawberry.field
    # def snapshots(self) -> list[SnapshotNode]:
    #     return [
    #         SnapshotNode.from_pydantic(node)
    #         for node in get_manifest().nodes.values()
    #         if node.resource_type.value == "snapshot"
    #     ]

    # @strawberry.field
    # def snapshot(
    #     self,
    #     unique_id: Annotated[
    #         str,
    #         strawberry.argument(description="The unique ID of this particular model"),
    #     ],
    # ) -> SnapshotNode:
    #     node = get_manifest().nodes[unique_id]
    #     if node.resource_type.value == "snapshot":
    #         raise ValueError(f"No snapshot called {unique_id} found")
    #     return SeedNode.from_pydantic(node)

    # @strawberry.field
    # def sources(self) -> list[SourceNode]:
    #     return [
    #         SourceNode.from_pydantic(node)
    #         for node in get_manifest().nodes.values()
    #         if node.resource_type.value == "source"
    #     ]

    # @strawberry.field
    # def source(
    #     self,
    #     unique_id: Annotated[
    #         str,
    #         strawberry.argument(description="The unique ID of this particular source"),
    #     ],
    # ) -> SourceNode:
    #     node = get_manifest().nodes[unique_id]
    #     if node.resource_type.value == "source":
    #         raise ValueError(f"No source called {unique_id} found")
    #     return SourceNode.from_pydantic(node)

    @strawberry.field
    def tests(self) -> list[TestNode]:
        manifest = get_manifest()
        return [
            convert_to_strawberry(manifest, node)
            for node in manifest.nodes.values()
            if node.resource_type.value == "test"
        ]

    @strawberry.field
    def test(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular test"),
        ],
    ) -> TestNode:
        manifest = get_manifest()
        return convert_to_strawberry(
            manifest,
            manifest.nodes[unique_id],
            expected_resource_type="test",
        )
