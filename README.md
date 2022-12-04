# A Really Basic Benchmark Of Some Web Frameworks

- Basic servers for Python, NodeJS, and Rust, each implemented to run in docker
    - Python: FastAPI + uvicorn
    - NodeJS: ExpressJS
    - Rust: Rocket.rs
- Each server is set up with a single route. When called it counts from 0 to 2,000,000, then sends a
  json response
- We use a simple shell script running on the docker host, that curls the servers 100 times in a
  loop.

## Results

Python: ~4.5 seconds

```
time ./curl_loop.sh 

real	0m4.553s
user	0m0.235s
sys	0m0.095s
```

NodeJS: ~0.43 seconds

```
time ./curl_loop.sh 

real	0m0.430s
user	0m0.192s
sys	0m0.104s
```

NodeJS: ~0.30 seconds

```
time ./curl_loop.sh 

real	0m0.296s
user	0m0.177s
sys	0m0.089s
```

### Python Test

Start server:
```bash
cd python
docker-compose up --build
```

Another terminal:
```bash
./curl_loop.sh
```

Clean up:
```bash
docker-compose down
```

### NodeJS Test

Start server:
```bash
cd nodejs
docker-compose up --build
```

Another terminal:
```bash
./curl_loop.sh
```

Clean up:
```bash
docker-compose down
```

### Rust Test

Start server:
```bash
cd rust
docker-compose up --build
```

Another terminal:
```bash
./curl_loop.sh
```

Clean up:
```bash
docker-compose down
```
