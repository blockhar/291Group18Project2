#!/bin/sh

echo reviews.txt
break.pl
db_load -c -T -t hash -f reviews.txt rw.idx

sort -u pterms.txt
break.pl
db_load -c duplicates=1 -T -t btree -f pterms.txt pt.idx

sort -u rterms.txt
break.pl
db_load -c duplicates=1 -T -t btree -f rterms.txt rt.idx

sort -u scores.txt
break.pl
db_load -c duplicates=1 -T -t btree -f scores.txt sc.idx
