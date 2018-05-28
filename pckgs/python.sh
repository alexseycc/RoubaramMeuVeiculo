#rpm -i python-pip-1.3.1-4.el6.art.noarch.rpm 2>&1 | tee python.error
#dep=`tail -1 python.error | cut -d' ' -f1`
#yum install $dep -y
#rpm -i python-pip-1.3.1-4.el6.art.noarch.rpm
#pip install pymongo
#or next way,written by alexsey rbçs..
yum install python-setuptools -y
rpm -i python-pip-1.3.1-4.el6.art.noarch.rpm
pip install pymongo