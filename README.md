This program loads a basic machine configuration file included in the repository, applies your chosen node group, and deploys it to the cluster that you're logged into. The configuration applied is a bas64 encoded version of the following:

```
server 0.rhel.pool.ntp.org iburst
server 1.rhel.pool.ntp.org iburst
server 2.rhel.pool.ntp.org iburst
server 3.rhel.pool.ntp.org iburst
driftfile /var/lib/chrony/drift
makestep 1.0 3
rtcsync
logdir /var/log/chrony 
```

Because this configuration relies on the rhel.pool.ntp.org time servers, this will not work in disconnected environments or in environments where you wish to configure your cluster to use in-house NTP.

Please note that this solution is experimental, and is not supported by Red Hat or representative of its best practices for NTP configuration on RHCOS hosts.
