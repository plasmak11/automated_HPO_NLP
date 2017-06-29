#!/bin/bash
#
# MetaMap and UMLS powered clinical genetic phenotype extractor
#
# Local version of MetaMap server must be running
#
# Change '../../bin/' to location of the 'metamap' application
#

for filename in *.txt; do
    ../../bin/metamap -I -p -J -K -g -D -8 --negex --conj --cascade cgab,genf,lbpr,lbtr,patf,dsyn,fndg,mobd -R "HPO" -r 550 --composite_phrases 3 $filename
done 

for f in *txt.out; do
    grep_output=$(grep -P '(?<!N )C[0-9][0-9].*:*' $f -o | cut -d ':' -f 2 | sort | uniq | sed 's/([^()].*)//g' | sed 's/\[[^][]*\]//g')
    echo "$f,\"$grep_output\""
done