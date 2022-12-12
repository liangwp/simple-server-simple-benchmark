# A Really Simple Benchmark Of Some Web Frameworks

- Basic servers for Python, NodeJS, and Rust, each implemented to run in docker
    - Python: FastAPI + uvicorn
    - NodeJS: ExpressJS
    - Rust: Rocket.rs
- Each server is set up with a single route. When called, the server counts from 0 to 100,000, then
  returns a json response.
- Each server is set up to listen on host port 8000
  - Each folder contains a `docker-compose.yml`
  - Run `docker-compose up --build` to start the server
  - Run `docker-compose down` to stop it
- We have a shell script `./curl_loop.sh` on the docker host
  - This script generates a curl command to call a server 1000 times in a single http connection
    (attempting to reduce both bash and http overhead)
  - It then prints out the execution time of the script
- Each time we start a different server for testing, we only keep the timing for the **2nd** run of
  the `curl_loop.sh`. In theory, this should exclude the time for whatever jit compilation that
  the frameworks might perform.

## Results

Tests are run on a single linux laptop, on this particular config of hardware and software that we
shall not concern ourselves with.

* Python: ~2 seconds

  ```
  real	0m2.014s
  user	0m0.045s
  sys	0m0.026s
  ```

* NodeJS: ~0.23 seconds

  ```
  real	0m0.233s
  user	0m0.028s
  sys	0m0.025s
  ```

* Rust: ~0.09 seconds

  ```
  real	0m0.091s
  user	0m0.035s
  sys	0m0.016s
  ```
