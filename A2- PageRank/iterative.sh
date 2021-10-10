#!/bin/sh
CONVERGE=1
ITER=1
rm v v1 log*

$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave
hdfs dfs -rm -r /Assignment-2/output/task-* 

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
-mapper "'/home/pes_bigdata/Desktop/Assignment-2/mapper_t1.py'" \
-reducer "'/home/pes_bigdata/Desktop/Assignment-2/reducer_t1.py' '/home/pes_bigdata/Desktop/Assignment-2/v'" \
-input /Assignment-2/Input/dataset-sample.txt \
-output /Assignment-2/output/task-1-output

while [ "$CONVERGE" -ne 0 ]
do
	echo "############################# ITERATION $ITER #############################"
	hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
	-mapper "'/home/pes_bigdata/Desktop/Assignment-2/mapper_t2.py' '/home/pes_bigdata/Desktop/Assignment-2/v' '/home/pes_bigdata/Desktop/Assignment-2/Input/node-map-sample.json'" \
	-reducer "'/home/pes_bigdata/Desktop/Assignment-2/reducer_t2.py'" \
	-input /Assignment-2/output/task-1-output/part-00000 \
	-output /Assignment-2/output/task-2-output
	touch v1
	hadoop fs -cat /Assignment-2/output/task-2-output/part-00000 > "/home/pes_bigdata/Desktop/Assignment-2/v1"
	CONVERGE=$(python3 check_conv.py $ITER>&1)
	ITER=$((ITER+1))
	hdfs dfs -rm -r /Assignment-2/output/task-2-output/
	echo $CONVERGE
done
