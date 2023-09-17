#!/bin/bash

HIVE_VERSION="3.1.2"
HIVE_DOWNLOAD_URL="https://downloads.apache.org/hive/hive-${HIVE_VERSION}/apache-hive-${HIVE_VERSION}-bin.tar.gz"
HIVE_HOME="/opt/hive"
HIVE_CONF_DIR="$HIVE_HOME/conf"
HADOOP_HOME="/opt/hadoop"
MYSQL_HOST="localhost"
MYSQL_PORT="3306"
MYSQL_DATABASE="hive_metastore"
MYSQL_USERNAME="hive"
MYSQL_PASSWORD="your_password_here"
wget -P /tmp "$HIVE_DOWNLOAD_URL"
tar -xzvf "/tmp/apache-hive-${HIVE_VERSION}-bin.tar.gz" -C /opt
rm "/tmp/apache-hive-${HIVE_VERSION}-bin.tar.gz"
echo "export HIVE_HOME=$HIVE_HOME" >> ~/.bashrc
echo 'export PATH=$PATH:$HIVE_HOME/bin' >> ~/.bashrc
source ~/.bashrc
cp "$HIVE_CONF_DIR/hive-default.xml.template" "$HIVE_CONF_DIR/hive-site.xml"
echo "<configuration>
  <property>
    <name>javax.jdo.option.ConnectionURL</name>
    <value>jdbc:mysql://$MYSQL_HOST:$MYSQL_PORT/$MYSQL_DATABASE</value>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionDriverName</name>
    <value>com.mysql.jdbc.Driver</value>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionUserName</name>
    <value>$MYSQL_USERNAME</value>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionPassword</name>
    <value>$MYSQL_PASSWORD</value>
  </property>
</configuration>" > "$HIVE_CONF_DIR/hive-site.xml"
mysql -u root -p <<EOF
CREATE DATABASE IF NOT EXISTS $MYSQL_DATABASE;
CREATE USER IF NOT EXISTS '$MYSQL_USERNAME'@'localhost' IDENTIFIED BY '$MYSQL_PASSWORD';
GRANT ALL PRIVILEGES ON $MYSQL_DATABASE.* TO '$MYSQL_USERNAME'@'localhost';
FLUSH PRIVILEGES;
EOF
schematool -dbType mysql -initSchema
echo "Hive $HIVE_VERSION is installed and configured with Hadoop and MySQL."
