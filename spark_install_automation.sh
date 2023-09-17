#!/bin/bash

SPARK_VERSION="3.2.0"
SPARK_HOME="/opt/spark"
DOWNLOAD_URL="https://downloads.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.2.tgz"
sudo mkdir -p $SPARK_HOME
sudo chown -R $USER:$USER $SPARK_HOME
wget $DOWNLOAD_URL -P /tmp
tar -xzf /tmp/spark-$SPARK_VERSION-bin-hadoop3.2.tgz -C $SPARK_HOME
rm /tmp/spark-$SPARK_VERSION-bin-hadoop3.2.tgz
echo "export SPARK_HOME=$SPARK_HOME" >> ~/.bashrc
echo 'export PATH=$PATH:$SPARK_HOME/bin' >> ~/.bashrc
source ~/.bashrc
cp $SPARK_HOME/conf/spark-env.sh.template $SPARK_HOME/conf/spark-env.sh
echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> $SPARK_HOME/conf/spark-env.sh
$SPARK_HOME/sbin/start-all.sh
