from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


# Use the static loaction specified in settings
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


# Use the media location specified in settings
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
