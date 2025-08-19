import configparser
from pyspark.sql import *

from pyspark import SparkConf


def get_spark_app_config():
    spark_conf = SparkConf()
    config = configparser.ConfigParser()
    config.read("spark.conf")


    for(key,val) in config.items("SPARK_APP_CONFIG"):
        spark_conf.set(key,val)
    return spark_conf

def get_spark_session(env):

    if env == "LOCAL":
        return SparkSession.builder \
        .config("spark.driver.extraJavaOptions", "-Dlog4j.configurationFile=log4j2.properties") \
        .master("local[2]") \
        .enableHiveSupport()\
        .getOrCreate()

    else :
        return SparkSession.builder \
            .enableHiveSupport() \
            .getOrCreate()

