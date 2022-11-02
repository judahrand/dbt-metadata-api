from typing import Collection, Dict, List, Optional, Union

from dbt.contracts.graph.compiled import ManifestNode
from dbt.contracts.graph.manifest import WritableManifest
from dbt.contracts.graph.parsed import (
    ColumnInfo,
    ParsedExposure,
    ParsedMetric,
    ParsedSourceDefinition,
)
from dbt.contracts.graph.unparsed import FreshnessThreshold, Time

from dbt_metadata_api.enums import TimePeriod

from .common import CatalogColumn, Criteria, CriteriaInfo


def get_parents(
    unique_id: str,
    manifest: WritableManifest,
    resource_types: Optional[Collection[str]] = None,
) -> Optional[List[str]]:
    possible_parents: dict[str, Union[ManifestNode, ParsedSourceDefinition]] = {
        **manifest.nodes,
        **manifest.sources,
    }
    if manifest.parent_map is not None:
        parents = (
            possible_parents[parent_id] for parent_id in manifest.parent_map[unique_id]
        )
        if resource_types is not None:
            parents = (node for node in parents if node.resource_type in resource_types)

        return [node.unique_id for node in parents]
    return None


def get_children(
    unique_id: str,
    manifest: WritableManifest,
    resource_types: Optional[Collection[str]] = None,
) -> Optional[List[str]]:
    possible_children: dict[str, Union[ManifestNode, ParsedMetric, ParsedExposure]] = {
        **manifest.nodes,
        **manifest.metrics,
        **manifest.exposures,
    }
    if manifest.child_map is not None:
        children = (
            possible_children[child_id] for child_id in manifest.child_map[unique_id]
        )
        if resource_types is not None:
            children = (
                node for node in children if node.resource_type in resource_types
            )

        return [node.unique_id for node in children]
    return None


def get_tests(
    unique_id: str,
    manifest: WritableManifest,
) -> List[str]:
    return [
        node.unique_id
        for node in manifest.nodes.values()
        if node.resource_type == "test" and unique_id in node.depends_on.nodes
    ]


def get_column_catalogs(columns: Dict[str, ColumnInfo]) -> List[CatalogColumn]:
    return [
        CatalogColumn(
            name=col.name,
            index=idx,
            description=col.description,
            meta=col.meta,
            tags=col.tags,
            type=col.data_type,
        )
        for idx, col in enumerate(columns.values())
    ]


def get_criteria(freshness: FreshnessThreshold) -> Criteria:
    error_after: Optional[CriteriaInfo] = None
    if freshness.error_after is not None:
        error_after = get_criteria_info(freshness.error_after)

    warn_after: Optional[CriteriaInfo] = None
    if freshness.warn_after is not None:
        warn_after = get_criteria_info(freshness.warn_after)

    return Criteria(
        error_after=error_after,
        warn_after=warn_after,
    )


def get_criteria_info(time: Time) -> CriteriaInfo:
    period: Optional[TimePeriod] = None
    if time.period is not None:
        period = TimePeriod(period)
    return CriteriaInfo(
        count=time.count,
        period=period,
    )
