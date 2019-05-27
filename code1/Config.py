class Config(object):
    """项目共用的一些配置"""
    SECRET_KEY = '123456'


class DevelopmentConfig(Config):
    """开发环境"""
    DEBUG = True  # 打开测试


class ProductionConfig(Config):
    """生产环境"""
    DEBUG = False  # 打开测试


APPCONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
