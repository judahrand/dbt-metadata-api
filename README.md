# dbt-metadata

To run the server please run:

```bash
poetry install
DBT_METADATA_MANIFEST=manifest.json poetry run uvicorn dbt_metadata_api:app --host 127.0.0.1 --port 8000
```
