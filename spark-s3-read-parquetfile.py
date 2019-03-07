from pyspark import SparkContext
from pyspark.sql.session import SparkSession
#sc = SparkContext("local", "Simple App")
#hadoop_conf=sc._jsc.hadoopConfiguration()
#hadoop_conf.set("fs.s3n.impl", "org.apache.hadoop.fs.s3native.NativeS3FileSystem")
#hadoop_conf.set("fs.s3n.awsAccessKeyId", "")
#hadoop_conf.set("fs.s3n.awsSecretAccessKey", "")
#spark = SparkSession(sc)
df = spark.read.parquet("s3a://accessId:SecretKey@/S3PATH/users.parquet")
df.show()

df.createOrReplaceTempView("users")
names = spark.sql("select * from users where favorite_color is not null")
names.show()
