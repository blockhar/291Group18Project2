#!/bin/sh

cat reviews.txt | perl break.pl | db_load -T -t hash rw.idx

sort -u pterms.txt | perl break.pl | db_load -c duplicates=1 -T -t btree pt.idx

sort -u rterms.txt | perl break.pl | db_load -c duplicates=1 -T -t btree rt.idx

sort -u scores.txt | perl break.pl | db_load -c duplicates=1 -T -t btree sc.idx
