#!/bin/bash
echo "4 10 21
6 20 31 "\
| awk '{s += $1 ; u += $2 ; m += $3; ave1= s/2; ave2=u/2; ave3=m/2 } END  {print s,u,m,  ave1,ave2,ave3} '

