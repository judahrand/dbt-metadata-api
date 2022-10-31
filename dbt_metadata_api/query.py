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


@strawberry.type
class Query:
    @strawberry.field
    def exposures(self, info: strawberry.types.Info) -> list[ExposureNode]:
        manifest = info.context["manifest"]
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
        info: strawberry.types.Info,
    ) -> ExposureNode:
        manifest = info.context["manifest"]
        return convert_to_strawberry(manifest, manifest.exposures[unique_id])

    @strawberry.field
    def macros(self, info: strawberry.types.Info) -> list[MacroNode]:
        manifest = info.context["manifest"]
        return [
            convert_to_strawberry(manifest, node) for node in manifest.macros.values()
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
        manifest = info.context["manifest"]
        return convert_to_strawberry(
            manifest,
            manifest.macros[unique_id],
        )

    @strawberry.field
    def metrics(self, info: strawberry.types.Info) -> list[MetricNode]:
        manifest = info.context["manifest"]
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
        info: strawberry.types.Info,
    ) -> MetricNode:
        manifest = info.context["manifest"]
        return convert_to_strawberry(manifest, manifest.metrics[unique_id])

    @strawberry.field
    def models(self, info: strawberry.types.Info) -> list[ModelNode]:
        manifest = info.context["manifest"]
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
        info: strawberry.types.Info,
    ) -> ModelNode:
        manifest = info.context["manifest"]
        return convert_to_strawberry(
            manifest,
            manifest.nodes[unique_id],
            expected_resource_type="model",
        )

    # @strawberry.field
    # def seeds(self, info: strawberry.types.Info) -> list[SeedNode]:
    #     return [
    #         SeedNode.from_pydantic(node)
    #         for node in info.context["manifest"].nodes.values()
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
    #     node = info.context["manifest"].nodes[unique_id]
    #     if node.resource_type.value == "seed":
    #         raise ValueError(f"No seed called {unique_id} found")
    #     return SeedNode.from_pydantic(node)

    # @strawberry.field
    # def snapshots(self, info: strawberry.types.Info) -> list[SnapshotNode]:
    #     return [
    #         SnapshotNode.from_pydantic(node)
    #         for node in info.context["manifest"].nodes.values()
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
    #     node = info.context["manifest"].nodes[unique_id]
    #     if node.resource_type.value == "snapshot":
    #         raise ValueError(f"No snapshot called {unique_id} found")
    #     return SeedNode.from_pydantic(node)

    # @strawberry.field
    # def sources(self, info: strawberry.types.Info) -> list[SourceNode]:
    #     return [
    #         SourceNode.from_pydantic(node)
    #         for node in info.context["manifest"].nodes.values()
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
    #     node = info.context["manifest"].nodes[unique_id]
    #     if node.resource_type.value == "source":
    #         raise ValueError(f"No source called {unique_id} found")
    #     return SourceNode.from_pydantic(node)

    @strawberry.field
    def tests(self, info: strawberry.types.Info) -> list[TestNode]:
        manifest = info.context["manifest"]
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
        info: strawberry.types.Info,
    ) -> TestNode:
        manifest = info.context["manifest"]
        return convert_to_strawberry(
            manifest,
            manifest.nodes[unique_id],
            expected_resource_type="test",
        )
