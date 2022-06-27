# MapReduce-assignement
Appliying mapReduce model with python

Assignment: Counting Host Sizes

- Suppose we have a large web corpus
- The metadata file has lines of the form (URL, size, date, ...)
- For each host, find the total number of bytes, i.e. the sum of the page sizes for all URLs from that host

Solution steps: 
- Creating Web Corpus randomly (because this type of data is not available)
- Implementing the Map and Reduce functions
- Creating map and reduce clusters using dispy package with JobCluster utility
- Creating map and reduce jobs
- Reducing size count of each host
- Printing the results
