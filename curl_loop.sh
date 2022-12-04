#!/bin/bash

for i in {1..100}; do
  curl -s 'localhost:8000' > /dev/null
done
