from fastapi import FastAPI
from hindsight_client import Hindsight

app = FastAPI()

# This connects our API to the 'Filing Cabinet'
# We will assume Hindsight is running on your computer
memory = Hindsight(base_url="http://localhost:8888")

@app.get("/log")
async def log_incident(event: str):
    # This 'Retains' the memory in a bank called 'my_stories'
    await memory.aretain(bank_id="my_stories", content=event)
    
    return {"status": "I have added this event to my memory bank!"}

@app.get("/recall")
async def see_memories(topic: str):
    # This 'Recalls' similar stories from the cabinet
    past_stories = await memory.arecall(bank_id="my_stories", query=topic)
    return {"what_i_remember": past_stories}