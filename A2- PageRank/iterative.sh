#!/bin/sh
CONVERGE=1
ITER=1
rm /home/pes1ug19cs592/A2/v.txt /home/pes1ug19cs592/A2/v1.txt /home/pes1ug19cs592/A2/log*

$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave
hdfs dfs -rm -r /A2/output/task*

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
-mapper "'/home/pes1ug19cs592/A2/mapper_t1.py'" \
-reducer "'/home/pes1ug19cs592/A2/reducer_t1.py' '/home/pes1ug19cs592/A2/v.txt'" \
-input /A2/dataset_1percent.txt \
-output /A2/output/task1

while [ "$CONVERGE" -ne 0 ]
do
	echo "############################# ITERATION $ITER #############################"
	hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
	-mapper "'/home/pes1ug19cs592/A2/mapper_t2.py' '/home/pes1ug19cs592/A2/v.txt' '/home/pes1ug19cs592/A2/embedding_1percent.json'" \
	-reducer "'/home/pes1ug19cs592/A2/reducer_t2.py'" \
	-input /A2/output/task1/part-00000 \
	-output /A2/output/task2
	touch /home/pes1ug19cs592/A2/v1.txt
	hadoop fs -cat /A2/output/task2/part-00000 > "/home/pes1ug19cs592/A2/v1.txt"
	CONVERGE=$(python3 check_conv.py $ITER>&1)
	ITER=$((ITER+1))
	hdfs dfs -rm -r /A2/output/task2/
	echo $CONVERGE
done
