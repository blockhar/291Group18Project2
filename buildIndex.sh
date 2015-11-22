#!/bin/sh

echo reviews.txt | uniq -u
break.pl
db_load -c -T -t hash rw.idx

sort -u pterms.txt
break.pl
db_load -c duplicates=1 -T -t btree pt.idx

sort -u rterms.txt
break.pl
db_load -c duplicates=1 -T -t btree rt.idx

sort -u scores.txt
break.pl
db_load -c duplicates=1 -T -t btree sc.idx
