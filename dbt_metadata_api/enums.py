import strawberry

from .models import manifest

ResourceType = strawberry.enum(manifest.ResourceType)
