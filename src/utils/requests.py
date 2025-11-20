import httpx

async def fetch(**kwargs):
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(**kwargs)
        return response.text