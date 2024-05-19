from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from rag_redis_multi_modal_multi_vector.chain import chain as rag_redis_chain
import os
from dotenv import load_dotenv

load_dotenv()

redis_url = os.getenv('REDIS_URL')
openai_api_key = os.getenv('OPENAI_API_KEY')

app = FastAPI()

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


add_routes(
    app,
    rag_redis_chain,
    path="/rag-redis-multi-modal-multi-vector"
)