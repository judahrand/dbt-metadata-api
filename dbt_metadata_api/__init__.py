import asyncio
import os

import strawberry
import upath
from fastapi import Depends, FastAPI
from strawberry.fastapi import GraphQLRouter

from .query import Query
from .utils import ManifestLoader

DBT_METADATA_MANIFEST = upath.UPath(os.getenv("DBT_METADATA_MANIFEST", "manifest.json"))
DBT_METADATA_REFRESH = os.getenv("DBT_METADATA_REFRESH", 30)
DBT_METADATA_MANIFEST_LOADER = ManifestLoader(DBT_METADATA_MANIFEST)


def get_context(manifest=Depends(DBT_METADATA_MANIFEST_LOADER.current)):
    return {"manifest": manifest}


schema = strawberry.Schema(query=Query)

graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
)

app = FastAPI()

app.include_router(graphql_app, prefix="/graphql")


async def refresh_manifest(manifest_loader: ManifestLoader):
    loop = asyncio.get_running_loop()
    while True:
        await asyncio.sleep(float(DBT_METADATA_REFRESH))
        await loop.run_in_executor(executor=None, func=manifest_loader.refresh)


@app.on_event("startup")
async def load_manifest_loader():
    app.manifest_loader = DBT_METADATA_MANIFEST_LOADER
    app.manifest_loader_task = asyncio.create_task(
        refresh_manifest(app.manifest_loader)
    )


@app.on_event("shutdown")
async def cancel_manifest_loader_task():
    app.manifest_loader_task.cancel()
