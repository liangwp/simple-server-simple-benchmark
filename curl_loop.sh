#!/bin/bash

array=();
for i in {1..1000}; do
  array+=(--next http://localhost:8000 ) ; 
done;

time {
  curl -s "${array[@]}" > /dev/null;
}
