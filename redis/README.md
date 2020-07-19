## Stand up redis and application pods

```
kubectl apply -f .
```

## Deploy Redis Cluster

The next step is to form a Redis Cluster. To do this, we run the following command and type yes to accept the configuration. The first three nodes become masters, and the last three become slaves.

`kubectl exec -it redis-cluster-0 -- redis-cli --cluster create --cluster-replicas 1 $(kubectl get pods -l app=redis-cluster -o jsonpath='{range.items[*]}{.status.podIP}:6379 ')`


## Check the cluster details and the role for each member.

`kubectl exec -it redis-cluster-0 -- redis-cli cluster info`

`for x in $(seq 0 5); do echo "redis-cluster-$x"; kubectl exec redis-cluster-$x -- redis-cli role; echo; done`

## To see all keys and their values

> https://stackoverflow.com/a/49902933/2177559

`
for key in $(redis-cli -p 6379 keys \*);
  do echo "Key : '$key'" 
     redis-cli -p 6379 GET $key;
done
`

## Simulate a Node Failure

We can simulate the failure of a cluster member by deleting the Pod via kubectl. When we delete redis-cluster-0, which was originally a master, we see that Kubernetes promotes redis-cluster-3 to master, and when redis-cluster-0 returns, it does so as a slave.

```
kubectl describe pods redis-cluster-0 | grep IP
kubectl describe pods redis-cluster-3 | grep IP

kubectl exec -it redis-cluster-0 -- redis-cli role
kubectl exec -it redis-cluster-3 -- redis-cli role
```

### Tutorial steps taken from

> https://rancher.com/blog/2019/deploying-redis-cluster
