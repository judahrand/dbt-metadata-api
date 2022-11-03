# dbt-metadata

To start the server please run:

```bash
poetry install --all-extras
export DBT_METADATA_REFRESH=30
export DBT_METADATA_MANIFEST=gs://my-bucket/manifest.json
poetry run uvicorn dbt_metadata_api:app --host 127.0.0.1 --port 8000
```

* `DBT_METADATA_MANIFEST` can be a path to a local file, a GCS blob, an S3 blob, or an Azure Storage blob.
* `DBT_METADATA_REFRESH` is the frequency in second with which the Manifest will be updated.
