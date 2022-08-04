import os

class Config(object):
  DEBUG = True

class DevelopmentConfig(Config):
  DEBUG = True

class TestingConfig(Config):
  DEBUG = True

class ProductionConfig(Config):
  DEBUG = True

config_by_name = dict(
  dev = DevelopmentConfig,
  test = TestingConfig,
  prod = ProductionConfig,
)
