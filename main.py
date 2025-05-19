from fastapi.responses import StreamingResponse
from langchain_openai import ChatOpenAI
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    chat = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    async def async_generator():
        async for chunk in chat.astream("疲労の原因は何ですか？"):
            yield chunk.content

    return StreamingResponse(
        async_generator(),
        media_type="text/event-stream; charset=utf-8"
    )
