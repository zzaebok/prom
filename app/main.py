from fastapi import FastAPI
from prometheus_client import Counter
import prometheus_client

app = FastAPI()
metrics_app = prometheus_client.make_asgi_app()
app.mount("/metrics", metrics_app)

request_root = Counter("request_count", "Total request count of the host")

@app.get("/")
def read_root():
    request_root.inc()
    return {"Hello": "World"}