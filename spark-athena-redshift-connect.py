# Connecting to Athena 
remote_table = spark.read.format("jdbc").option("url", "jdbc:awsathena://athena.us.amazonaws.com:443;User=<usernmame>;Password=<password>;S3OutputLocation=s3://aws-temporary;").option("dbtable","<schema.tablename>").option("driver","com.simba.athena.jdbc.Driver").load()

remote_table.show(10)

display(remote_table.select("col1","col2","col3"))

# Connecting to RedShift
remote_table_2 = spark.read.format("jdbc").option("url", "jdbc:redshift:iam://redshift-cluster:5439/databasename?AccessKeyID=<accessId>&SecretAccessKey=<secretKey>&ssl=true&DbUser=<username>").option("dbtable","<schema.tablename>").option("driver","com.amazon.redshift.jdbc42.Driver").load()

remote_table_2.show(10)
