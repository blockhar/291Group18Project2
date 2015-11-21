#!/bin/sh

sort -o -u pterms.txt
sort -o -u rterms.txt
sort -o -u scores.txt

break.pl

db_load -c -T -t hash -f reviews.txt rw.idx
db_load -c duplicates=1 -T -t btree -f pterms.txt pt.idx
db_load -c duplicates=1 -T -t btree -f rterms.txt rt.idx
db_load -c duplicates=1 -T -t btree -f scores.txt sc.idx

db_dump -f rw.idx
db_dump -f pt.idx
db_dump -f rt.idx
db_dump -f sc.idx
