from typing import Annotated

import strawberry

from dbt_metadata_api.enums import ResourceType
from dbt_metadata_api.models.manifest import ParsedSingularTestNode
from dbt_metadata_api.types.tests import GenericTestNode, SingularTestNode

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
    def exposures(self) -> list[ExposureNode]:
        return list(get_manifest().exposures.values())

    @strawberry.field
    def exposure(
        self,
        name: Annotated[
            str, strawberry.argument(description="The name of this exposure")
        ],
    ) -> ExposureNode:
        return get_manifest().exposures.get(name)

    @strawberry.field
    def macros(self) -> list[MacroNode]:
        return list(get_manifest().macros.values())

    @strawberry.field
    def macro(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular macro"),
        ],
    ) -> MacroNode:
        return get_manifest().exposures.get(unique_id)

    @strawberry.field
    def metrics(self) -> list[MetricNode]:
        return list(get_manifest().metrics.values())

    @strawberry.field
    def metric(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular metric"),
        ],
    ) -> MetricNode:
        return get_manifest().metrics.get(unique_id)

    @strawberry.field
    def models(self) -> list[ModelNode]:
        return [
            ModelNode.from_pydantic(node)
            for node in get_manifest().nodes.values()
            if node.resource_type == ResourceType.model
        ]

    @strawberry.field
    def model(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular model"),
        ],
    ) -> ModelNode:
        node = get_manifest().nodes[unique_id]
        if node.resource_type == ResourceType.model:
            raise ValueError(f"No model called {unique_id} found")
        return ModelNode.from_pydantic(node)

    @strawberry.field
    def seeds(self) -> list[SeedNode]:
        return [
            SeedNode.from_pydantic(node)
            for node in get_manifest().nodes.values()
            if node.resource_type == ResourceType.seed
        ]

    @strawberry.field
    def seed(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular seed"),
        ],
    ) -> SeedNode:
        node = get_manifest().nodes[unique_id]
        if node.resource_type == ResourceType.seed:
            raise ValueError(f"No seed called {unique_id} found")
        return SeedNode.from_pydantic(node)

    @strawberry.field
    def snapshots(self) -> list[SnapshotNode]:
        return [
            SnapshotNode.from_pydantic(node)
            for node in get_manifest().nodes.values()
            if node.resource_type == ResourceType.snapshot
        ]

    @strawberry.field
    def snapshot(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular model"),
        ],
    ) -> SnapshotNode:
        node = get_manifest().nodes[unique_id]
        if node.resource_type == ResourceType.snapshot:
            raise ValueError(f"No snapshot called {unique_id} found")
        return SeedNode.from_pydantic(node)

    @strawberry.field
    def sources(self) -> list[SourceNode]:
        return [
            SourceNode.from_pydantic(node)
            for node in get_manifest().nodes.values()
            if node.resource_type == ResourceType.source
        ]

    @strawberry.field
    def source(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular source"),
        ],
    ) -> SourceNode:
        node = get_manifest().nodes[unique_id]
        if node.resource_type == ResourceType.source:
            raise ValueError(f"No source called {unique_id} found")
        return SourceNode.from_pydantic(node)

    @strawberry.field
    def tests(self) -> list[TestNode]:
        return [
            SingularTestNode.from_pydantic(node)
            if isinstance(node, ParsedSingularTestNode)
            else GenericTestNode.from_pydantic(node)
            for node in get_manifest().nodes.values()
            if node.resource_type == ResourceType.test
        ]

    @strawberry.field
    def test(
        self,
        unique_id: Annotated[
            str,
            strawberry.argument(description="The unique ID of this particular test"),
        ],
    ) -> TestNode:
        node = get_manifest().nodes[unique_id]
        if node.resource_type == ResourceType.test:
            raise ValueError(f"No test called {unique_id} found")
        if isinstance(node, ParsedSingularTestNode):
            return SingularTestNode.from_pydantic(node)
        return GenericTestNode.from_pydantic(node)
