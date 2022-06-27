
from controllers.fake_data_generator import *

import os

def mapper(doc):
   hosts = []
   with open(os.path.join('/tmp', doc)) as fd:
      for line in fd:
         split = line.split(', ')
         hosts.extend((split[0], int(split[1])))
   return hosts

def reducer(hosts):
   size_count = {}
   for host, size in hosts:
      if host not in size_count:
         size_count[host] = 0
      size_count[host]  += size
   return size_count



def main():
   import dispy
   # generate data
   # FakeDataGenerator.generate()

   map_cluster = dispy.JobCluster( mapper, reentrant = True)
   #any node can work on reduce
   reduce_cluster = dispy.JobCluster(reducer, nodes=['*'], reentrant = True)
   map_jobs = []
   for f in ['doc1', 'doc2', 'doc3']:
      job = map_cluster.submit(f)
      map_jobs.append(job)
   
   reduce_jobs = []
   for map_job in map_jobs:
      hosts = map_job()
      if not hosts:
         print(map_job.exception)
         continue
      
      n = 0
      while n < len(hosts):
         m = min(len(hosts) - m, 1000)
         reduce_job = reduce_cluster.submit(hosts[n:n+m])
         reduce_jobs.append(reduce_job)
         n += m
   
   # reduce
   size_count = {}
   for reduce_job in reduce_jobs:
      hosts = reduce_job()
      if not hosts:
         print(reduce_job.exception)
         continue
      for host, size in hosts.iteritems():
         if host not in size_count:
            size_count[host] = 0
         size_count[host] += size
   
   for host in size_count:
      count = size_count[word]
      print(host, count)
   
   reduce_cluster.print_status()


if __name__ == "__main__":
    main()