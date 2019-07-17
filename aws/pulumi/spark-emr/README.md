Setup a spark cluster on EMR with Zeppelin installed.
Zeppelin notebooks are persisted in an S3 bucket

```pulumi up```
 to update the pulumi stack
 
 ```pulumi destroy``` to blow away all the resources
 
 `plumui config set ssh_keyname <keyname>` REQUIRED
  
 `plumui config set cluster_name <clustername>` optional defaults to `emr-default-cluster-XXXX`
 
 comment out the cluster definition code in `__main__.py` 
 if you want to only turn off the cluster and not the s3 bucket that holds the notebooks.
 
 
 