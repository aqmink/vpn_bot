from aiohttp.client import ClientSession

from config import PANEL_USERNAME, PANEL_PASSWORD


class BaseAPIServer:
    def __init__(self):
        self.base_url = "https://saveserf.com:80/home"
    
    async def get(self, url):
        async with ClientSession() as session:
            async with session.post(
                self.base_url + "/login", 
                data={"username": PANEL_USERNAME, "password": PANEL_PASSWORD}
            ) as response:
                # print(await response.json())
                pass
            async with session.get(self.base_url + url) as response:
                # print(await response.json())
                return await response.json()
    
    async def post(self, url, data):
        async with ClientSession() as session:
            async with session.post(
                self.base_url + "/login", 
                json={"username": PANEL_USERNAME, "password": PANEL_PASSWORD}
            ) as response:
                # print(await response.json())
                pass
            async with session.post(self.base_url + url, data=data) as response:
                # print(await response.json())
                return await response.json()
