#!/bin/bash

# use docker to start  bitnamai/cassandra 4.0.2 with a persistent volume
docker run -d --name cassandra -p 9042:9042 -p 9160:9160 -v cassandra_data:/bitnami bitnami/cassandra:4.0.2