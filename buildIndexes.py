"""Sort all the files built in Phase 1 (except the file reviews.txt which is sorted)
  using the Linux sort command; pass the right option to the sort command to keep only
  the unique rows (see the man page for sort). You can keep the sorted data under the
  same file names or pass sorted records to stdout so they can be piped to your loading
  program (as described next). Suppose the sorted files are named as before (to simplify
  our presentation here). Given the sorted files reviews.txt, pterms.txt, prterms.txt
  and scores.txt, create the following four indexes: (1) a hash index on reviews.txt with
  review id as key and the full review record as data, (2) a B+-tree index on pterms.txt
  with terms as keys and review ids as data, (3) a B+-tree index on rterms.txt with terms
  as keys and review ids as data, (4) a B+-tree index on scores.txt with scores as keys
  and review ids as data. You should note that the keys in all 4 cases are the character
  strings before the first comma and the data is everything that comes after the comma.
  Use the db_load command to build your indexes. db_load by default expects keys in one
  line and data in the next line. Here is a simple Perl script that converts input records
  into the format db_load expects. Your program for Phase 2 would produces four indexes
  which should be named rw.idx, pt.idx, rt.idx, and sc.idx respectively corresponding to
  indexes 1, 2, 3, and 4, as discussed above.
  
  In addition to db_load, you may also find db_dump with option p useful as you are building
  and testing the correctness of your indexes."""

# https://eclass.srv.ualberta.ca/mod/page/view.php?id=1635284
# https://www.jcea.es/programacion/pybsddb_doc/

import sys

def buildIndexes():
  # import or get passed (probably import) text files
  # pterms.txt rterms.txt scores.txt
  
  
  # sort
  
  
  # return/store indexes (probably return)

if __name__ == '__main__':
  #test
