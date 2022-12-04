import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def read_root():
    # a cpu-bound loop
    counter = 0
    counter_max = 2_000_000
    while counter < counter_max:
        counter += 1
    return { 'hello': 'world' }

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False, access_log=False)
