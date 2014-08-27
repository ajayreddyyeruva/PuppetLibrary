#!/usr/bin/python

import boto.ec2
import sys
from operator import attrgetter

if len(sys.argv) !=3 :
	print "Please provide all the arguments volumeid max_snapshots_to_keep"
	sys.exit()
volumeId = sys.argv[1]
snapshotsToKeep = int(sys.argv[2])


conn = boto.ec2.connect_to_region('ap-southeast-1')

volumes = conn.get_all_volumes([volumeId])
volume = volumes[0]
print volume

snapshots =  volume.snapshots()
print snapshots

snapshots.sort(key=attrgetter("start_time"))

print "Snapshots sorted by date"
print snapshots

print "Snapshots to be deleted"
for snapshot in snapshots[:-snapshotsToKeep]:
	print snapshot
	snapshot.delete()
	
