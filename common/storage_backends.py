from abc import ABC

from storages.backends.s3boto3 import S3Boto3Storage


class StaticFilesStorage(ABC, S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'
    file_overwrite = True
    querystring_auth = False


class PublicMediaStorage(ABC, S3Boto3Storage):
    location = 'media/public'
    default_acl = 'public-read'
    file_overwrite = False
    querystring_auth = False


class PrivateMediaStorage(ABC, S3Boto3Storage):
    location = 'media/private'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False
