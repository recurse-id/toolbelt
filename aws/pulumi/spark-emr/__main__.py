import sys

import pulumi
import json
from pulumi_aws import s3, emr


cluster_name = None
try:
    cluster_name = pulumi.config.Config("spark-emr").require("cluster_name")
except:
    cluster_name = "emr-default-cluster"

#set your ssh_keyname (found in:
keyname = pulumi.config.Config("spark-emr").require("ssh_keyname")

bucket = s3.Bucket(cluster_name)

### JUST COMMENT OUT THE REST IF YOU WANT TO STOP THE CLUSTER and run pulumi up to update the stack this way the s3 bucket stays alive

emr_cluster = bucket.id.apply(lambda bucket_id:
    emr.Cluster(resource_name=cluster_name,
                applications =["Spark", "Zeppelin"],
                master_instance_type="m4.large",
                core_instance_count=2,
                core_instance_type="m5.xlarge",
                release_label="emr-5.24.1",
                ebs_root_volume_size=10,
                name="emr cluster running spark",
                service_role="EMR_DefaultRole",
                configurations=json.dumps([
                    {
                        "classification":"zeppelin-env",
                        "properties":{

                        },
                        "configurations":[
                            {
                                "classification":"export",
                                "properties":{
                                    "ZEPPELIN_NOTEBOOK_STORAGE":"org.apache.zeppelin.notebook.repo.S3NotebookRepo",
                                    "ZEPPELIN_NOTEBOOK_S3_BUCKET":f"{bucket_id}",
                                    "ZEPPELIN_NOTEBOOK_S3_USER":"zeppelin"
                                },
                                "configurations":[

                                ]
                            }
                        ]
                    }
                ]),
                ec2_attributes={
                    "instance_profile": "EMR_EC2_DefaultRole",
                    "key_name": keyname
                }))

pulumi.export("master_node",  emr_cluster.master_public_dns)
