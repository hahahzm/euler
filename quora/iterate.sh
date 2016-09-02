#!/bin/bash

for i in {1..20}
do
	printf "N=$i\t\t"
	./a.out $i
done
