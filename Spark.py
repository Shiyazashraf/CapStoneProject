import sys

from lib.logger import Log4J
from lib.utils import *
from pyspark.sql import *

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: sbdl {local, qa, prod} {load_date} : Arguments are missing")
        sys.exit(-1)

    job_run_env = sys.argv[1].upper()
    load_date = sys.argv[2]

    spark = get_spark_session(job_run_env)
    logger = Log4J(spark)

    logger.info("Finished creating Spark Session")

