#！/bin/bash
#download package
yum install -y wget
yum install gcc-c++ make zlib-devel libcurl-devel -y
#add username and add password
useradd iptv
echo "iptv:inno0802" | chpasswd
usermod -g video iptv
echo "iptv	ALL=(ALL)  ALL" >> /etc/sudoers
#set selinux
sed -i 's/^SELINUX=.*/SELINUX=disabled/' /etc/selinux/config
#set network
sed 's/ONBOOT=no/ONBOOT=yes/' /etc/sysconfig/network-scripts/ifcfg-eno1
sed 's/BOOTPROTO=dhcp/BOOTPROTO=static/' /etc/sysconfig/network-scripts/ifcfg-eno1
echo "IPADDR=192.168.1.151" >> /etc/sysconfig/network-scripts/ifcfg-eno1
echo "NETMASK=255.255.255.0" >> /etc/sysconfig/network-scripts/ifcfg-eno1
echo "GATEWAY=192.168.1.1" >> /etc/sysconfig/network-scripts/ifcfg-eno1
echo "USERCTL=no" >> /etc/sysconfig/network-scripts/ifcfg-eno1
echo "ZONE=public" >> /etc/sysconfig/network-scripts/ifcfg-eno1
echo "DNS1=8.8.8.8" >> /etc/sysconfig/network-scripts/ifcfg-eno1
echo "DNS2=8.8.4.4" >> /etc/sysconfig/network-scripts/ifcfg-eno1

sed 's/ONBOOT=no/ONBOOT=yes/' /etc/sysconfig/network-scripts/ifcfg-eno2
sed 's/BOOTPROTO=dhcp/BOOTPROTO=static/' /etc/sysconfig/network-scripts/ifcfg-eno2
echo "IPADDR=192.168.1.152" >> /etc/sysconfig/network-scripts/ifcfg-eno2
echo "NETMASK=255.255.255.0" >> /etc/sysconfig/network-scripts/ifcfg-eno2
echo "GATEWAY=192.168.1.1" >> /etc/sysconfig/network-scripts/ifcfg-eno2
echo "USERCTL=no" >> /etc/sysconfig/network-scripts/ifcfg-eno2
echo "ZONE=public" >> /etc/sysconfig/network-scripts/ifcfg-eno2
echo "DNS1=8.8.8.8" >> /etc/sysconfig/network-scripts/ifcfg-eno2
echo "DNS2=1.1.1.1" >> /etc/sysconfig/network-scripts/ifcfg-eno2
#install intel sdk
cd /tmp
wget http://135.0.197.98:8091/intel/MediaServerStudioEssentials2018R2/SDK2018Production16.9.tar.gz
tar -xvf  SDK2018Production16.9.tar.gz
cd SDK2018Production16.9/centos
tar -xvf install_scripts_centos_16.9-00183.tar.gz
./install_sdk_CentOS.sh
#install ffmpeg_libs
cd /tmp
wget http://135.0.197.98:8091/ffmpeg_libs.tar.gz
tar zxvf  ffmpeg_libs.tar.gz
cp -rf ffmpeg_libs/libs/* /usr/local/lib/ && cp -rf ffmpeg_libs/include/* /usr/local/include/
#install binutils
cd /tmp
wget http://ftp.gnu.org/gnu/binutils/binutils-2.32.tar.gz
tar -zxvf binutils-2.32.tar.gz
cd binutils-2.32/
./configure
make && make install

#install mqsv
cd /tmp
git clone http://dev.cnv8.tv:8900/root/mqsv.git
cd mqsv
chmod +x install.sh
./install.sh
#install knife
cd /tmp
git clone http://dev.cnv8.tv:8900/root/knife.git
cd knife/
chmod +x install.sh
./install.sh
#add ims service
cd /tmp
sftp root@192.168.1.201
get /usr/lib/systemd/system/ims-transcoder.service .
get /usr/lib/systemd/system/ims-relayer.service .
get /usr/lib/systemd/system/ims-streamer.service .
get /usr/lib/systemd/system/ims-cms.service .
get /usr/lib/systemd/system/ims-source.service .
get /usr/lib/systemd/system/ims-agent.service .
get /usr/lib/systemd/system/ims-monitor.service .
exit
mv /tmp/ims-*.service /usr/lib/systemd/system/

systemctl start ims-relayer.service
systemctl enable ims-relayer.service
systemctl start ims-transcoder.service
systemctl enable ims-transcoder.service
systemctl start ims-streamer.service
systemctl enable ims-streamer.service

#set ssh port
echo "Port 8822" >> /etc/ssh/sshd_config
systemctl restart sshd.service
#set firewall port
mv /etc/firewalld/zones/public.xml  /etc/firewalld/zones/public_bak.xml
touch /etc/firewalld/zones/public.xml
echo '<?xml version="1.0" encoding="utf-8"?>' > /etc/firewalld/zones/public.xml
echo '<zone>' >> /etc/firewalld/zones/public.xml
echo '  <short>Public</short>' >> /etc/firewalld/zones/public.xml
echo '  <description>For use in public areas. You do not trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.</description>' >> /etc/firewalld/zones/public.xml
echo '  <service name="ssh"/>' >> /etc/firewalld/zones/public.xml
echo '  <service name="dhcpv6-client"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="tcp" port="80"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="udp" port="1234"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="tcp" port="8500"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="tcp" port="8300"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="tcp" port="8301"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="tcp" port="8501"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="tcp" port="8502"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="tcp" port="8600"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="udp" port="8600"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="tcp" port="1236"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="tcp" port="1235"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="tcp" port="1234"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="tcp" port="8802"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="tcp" port="8822"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="tcp" port="1234-1236"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="tcp" port="3306"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="udp" port="2234"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="tcp" port="1237"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="tcp" port="8095"/>' >> /etc/firewalld/zones/public.xml
echo '  <port protocol="tcp" port="8800"/>' >> /etc/firewalld/zones/public.xml
echo '</zone>' >> /etc/firewalld/zones/public.xml
firewall-cmd --reload

#install ffmpeg
 wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
 tar xvJf ffmpeg-release-amd64-static.tar.xz
 cd ffmpeg-4.1.3-amd64-static/
 cp ffmpeg /usr/bin/
 cp ffprobe /usr/bin

#test and verify
#nohup ffmpeg -re -stream_loop -1 -i /tmp/colorbar.mp4 -vcodec copy -f mpegts udp://127.0.0.1:11001 &
#curl http://127.0.0.1:1236/start?ch=1
#curl http://127.0.0.1:1235/start?ch=1
#ffmpeg -i udp://127.0.0.1:12001
#ffmpeg -i http://127.0.0.1:8095/hls/1/index.m3u8


#install jdk1.8
yum install java-1.8.0-openjdk-* -y
java -verison

#install MariaDB, the MariaDB version is at least 10.1;
cd /etc/yum.repos.d/
touch MariaDB.repo
echo '[mariadb]' > MariaDB.repo
echo 'name=MariaDB' >> MariaDB.repo
echo 'baseurl=http://yum.mariadb.org/10.3/centos7-amd64' >> MariaDB.repo
echo 'gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB' >> MariaDB.repo
echo 'gpgcheck=1' >> MariaDB.repo
yum install MariaDB-server MariaDB-client -y
#vi /etc/my.cnf.d/server.cnf
mysqladmin version
mysql -urooot
