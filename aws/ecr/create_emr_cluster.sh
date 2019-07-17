#!/bin/bash
echo "enter cluster name"
read applicationName
echo "enter keyName"
read keyName
echo "enter instance count (including 1 master)"
read numWorkers
aws emr create-cluster --name $applicationName --release-label emr-5.23.0 --applications Name=Spark \
--ec2-attributes KeyName=$keyName --instance-type m4.large --instance-count $numWorkers --use-default-roles