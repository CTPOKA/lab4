FROM centos
COPY lab4.py .
RUN yum install epel-release -y
RUN yum install python36 -y
CMD python36 lab4.py

