"""Generates ***SQL*** and ***NoSQL*** Database Models from @dataclass"""


__version__ = '0.0.11'


from dbdaora.circuitbreaker import AsyncCircuitBreaker
from dbdaora.data_sources.fallback import FallbackDataSource
from dbdaora.data_sources.fallback.dict import DictFallbackDataSource
from dbdaora.data_sources.memory import MemoryDataSource
from dbdaora.data_sources.memory.dict import DictMemoryDataSource
from dbdaora.hash.query import HashQuery
from dbdaora.hash.repositories import HashData, HashRepository
from dbdaora.hash.service import HashService
from dbdaora.hashring import HashRing
from dbdaora.repository import MemoryRepository
from dbdaora.sorted_set.entity import SortedSetEntity
from dbdaora.sorted_set.query import SortedSetQuery
from dbdaora.sorted_set.repository import SortedSetRepository


try:
    from dbdaora.data_sources.fallback.datastore import DatastoreDataSource
    from dbdaora.hash.repositories.datastore import DatastoreHashRepository
except ImportError:
    DatastoreDataSource = None  # type: ignore


try:
    from dbdaora.data_sources.memory.aioredis import (
        AioRedisDataSource,
        ShardsAioRedisDataSource,
        make as make_aioredis_data_source,
    )
except ImportError:
    AioRedisDataSource = None  # type: ignore
    ShardsAioRedisDataSource = None  # type: ignore


__all__ = [
    'MemoryRepository',
    'HashRepository',
    'HashQuery',
    'HashData',
    'SortedSetRepository',
    'SortedSetQuery',
    'SortedSetEntity',
    'DictFallbackDataSource',
    'HashService',
    'AsyncCircuitBreaker',
    'make_aioredis_data_source',
    'HashRing',
    'FallbackDataSource',
    'MemoryDataSource',
    'DictMemoryDataSource',
]

if AioRedisDataSource:
    __all__.append('AioRedisDataSource')

if ShardsAioRedisDataSource:
    __all__.append('ShardsAioRedisDataSource')

if make_aioredis_data_source:
    __all__.append('make_aioredis_data_source')

if DatastoreDataSource:
    __all__.append('DatastoreDataSource')

if DatastoreHashRepository:
    __all__.append('DatastoreHashRepository')
