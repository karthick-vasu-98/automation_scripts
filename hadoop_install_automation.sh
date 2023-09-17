#!/bin/bash

sudo apt-get update
HADOOP_VERSION="3.3.6"
HADOOP_URL="https://downloads.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz"
INSTALL_DIR="/opt/hadoop"
sudo mkdir -p $INSTALL_DIR
sudo chown -R $USER:$USER $INSTALL_DIR
wget $HADOOP_URL -P /tmp
tar -xzvf /tmp/hadoop-${HADOOP_VERSION}.tar.gz -C $INSTALL_DIR
rm /tmp/hadoop-${HADOOP_VERSION}.tar.gz
echo "export HADOOP_HOME=$INSTALL_DIR/hadoop-${HADOOP_VERSION}" >> ~/.bashrc
echo 'export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin' >> ~/.bashrc
source ~/.bashrc
cp $HADOOP_HOME/etc/hadoop/* $HADOOP_HOME/etc/hadoop/*.template
sed -i 's/${JAVA_HOME}/\/usr\/lib\/jvm\/java-8-openjdk-amd64/g' $HADOOP_HOME/etc/hadoop/hadoop-env.sh

echo '<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
  </property>
</configuration>' > $HADOOP_HOME/etc/hadoop/core-site.xml

echo '<configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
</configuration>' > $HADOOP_HOME/etc/hadoop/hdfs-site.xml

$HADOOP_HOME/bin/hdfs namenode -format
$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh

