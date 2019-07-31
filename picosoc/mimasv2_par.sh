#!/bin/sh
set -e
edif2ngd mimasv2.edif
ngdbuild mimasv2 -uc mimasv2.ucf -p xc6slx9csg324-3
map -w mimasv2
par -w mimasv2.ncd mimasv2_par.ncd
bitgen -w mimasv2_par.ncd -g Binary:yes
