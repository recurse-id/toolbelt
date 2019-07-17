#!/usr/bin/env bash

MASTER_NODE=$(pulumi stack output master_node)
echo "$MASTER_NODE"
`ssh -i ~/.ssh/loki.pem -ND 8157 hadoop@"$MASTER_NODE"`