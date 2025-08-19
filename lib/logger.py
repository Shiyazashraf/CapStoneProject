class Log4J:
    def __init__(self,spark):
        log4j = spark._jvm.org.apache.log4j
        root_class = "spark.project"
        self.logger = log4j.LogManager.getLogger(root_class)

    def warn(self,message):
        self.logger.warn(message)
    def error(self,message):
        self.logger.error(message)
    def debug(self,message):
        self.logger.debug(message)
    def info(self,message):
        self.logger.info(message)