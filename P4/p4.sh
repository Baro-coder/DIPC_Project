#!/bin/sh

# Current dir
LOC=`pwd`

# Compile
javac -classpath lib/xmlrpc-2.0.1.jar -d bin p4.java

# 
cd bin

java -classpath $LOC/lib/xmlrpc-2.0.1.jar:$LOC/lib/commons-codec-1.7/commons-codec-1.7.jar:$LOC/bin p4
