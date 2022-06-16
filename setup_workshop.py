!pip3 install --upgrade pip scikit-learn
!HADOOP_USER_NAME=hdfs hdfs dfs -mkdir /user/$HADOOP_USER_NAME
!HADOOP_USER_NAME=hdfs hdfs dfs -chown $HADOOP_USER_NAME:$HADOOP_USER_NAME /user/$HADOOP_USER_NAME
!hdfs dfs -put data/historical_iot.txt /user/$HADOOP_USER_NAME
!hdfs dfs -ls -R /user/$HADOOP_USER_NAME
