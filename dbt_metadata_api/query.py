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
)
from .utils import get_manifest


@strawberry.type
class Query:
    # @strawberry.field
    # def exposures(self) -> list[ExposureNode]:
    #     return list(get_manifest().exposures.values())

    # @strawberry.field
    # def exposure(
    #     self,
    #     name: Annotated[
    #         str, strawberry.argument(description="The name of this exposure")
    #     ],
    # ) -> ExposureNode:
    #     return get_manifest().exposures.get(name)

    # @strawberry.field
    # def macros(self) -> list[MacroNode]:
    #     return [
    #         MacroNode.from_pydantic(node) for node in get_manifest().macros.values()
    #     ]

    # @strawberry.field
    # def macro(
    #     self,
    #     unique_id: Annotated[
    #         str,
    #         strawberry.argument(description="The unique ID of this particular macro"),
    #     ],
    # ) -> MacroNode:
    #     return get_manifest().exposures.get(unique_id)

    @strawberry.field
    def metrics(self) -> list[MetricNode]:
        manifest = get_manifest()
        return [
            MetricNode(
                manifest=manifest,
                unique_id=unique_id,
            )
            for unique_id in manifest.metrics.keys()
        ]

    @strawberry.field
    def metric(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular metric"),
        ],
    ) -> MetricNode:
        return MetricNode(
            manifest=get_manifest(),
            unique_id=unique_id,
        )

    @strawberry.field
    def models(self) -> list[ModelNode]:
        manifest = get_manifest()
        return [
            ModelNode(
                manifest=manifest,
                unique_id=node.unique_id,
            )
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
        node = manifest.nodes[unique_id]
        return ModelNode(manifest=manifest, unique_id=node.unique_id)

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

    # @strawberry.field
    # def tests(self) -> list[TestNode]:
    #     return [
    #         TestNode(node)
    #         for node in get_manifest().nodes.values()
    #         if node.resource_type.value == "test"
    #     ]

    # @strawberry.field
    # def test(
    #     self,
    #     unique_id: Annotated[
    #         str,
    #         strawberry.argument(description="The unique ID of this particular test"),
    #     ],
    # ) -> TestNode:
    #     node = get_manifest().nodes[unique_id]
    #     if node.resource_type.value == "test":
    #         raise ValueError(f"No test called {unique_id} found")
    #     if isinstance(node, ParsedSingularTestNode):
    #         return SingularTestNode.from_pydantic(node)
    #     return GenericTestNode.from_pydantic(node)
