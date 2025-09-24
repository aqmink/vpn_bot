from datetime import datetime, timedelta

from client_base import BaseAPIServer
from script import get_current_user, from_data


class APIClient():
    def __init__(self):
        self.client = BaseAPIServer()
    
    async def get_clients(self):
        return from_data(await self.client.get("/panel/api/inbounds/get/6"))
    
    async def set_client(self, user_id):
        settings = "{\"clients\": [{\"id\": \"" + f"{user_id}" + "\", \"flow\": \"xtls-rprx-vision\",\"email\": " + f"\"freenet-vpn-{user_id}\"" + ",\"limitIp\": 0,\"totalGB\": 0,\"expiryTime\": " + f"{(datetime.now() + timedelta(days=30)).timestamp() * 1000}" + ",\"enable\": true,\"tgId\": \"\",\"subId\": \"rqv5zw1ydutamcp0\",\"comment\": \"((\",\"reset\": 0}]}"
        return await self.client.post(
            url="/panel/api/inbounds/addClient",
            data={
                "id": 6,
                "settings": settings,
            }
        )
    
    async def update_client(self, user_id, enable):
        user = await self.get_client_by_email(f"freenet-vpn-{user_id}")
        enable = "true" if enable else "false"
        settings =  "{\"clients\": [{\"id\":" + f" \"{user_id}\"," + "\"flow\": \"xtls-rprx-vision\", \"email\": " + f"\"freenet-vpn-{user_id}\"," + "\"limitIp\": 0,\"totalGB\": 0,\"expiryTime\": " + f"{(datetime.now() + timedelta(days=30)).timestamp() * 1000}," + "\"enable\": " + f"{enable}" + ",\"tgId\": \"\",\"subId\": " + f"\"{user['sid']}\"," + " \"reset\": 0}]}"
        await self.client.post(
            f"/panel/api/inbounds/updateClient/{user_id}",
            data={
                "id": 6,
                "settings": settings,
            }
        )
        return await self.get_client_by_email(f"freenet-vpn-{user_id}")
    
    async def get_client_by_email(self, email):
        return get_current_user(await self.get_clients(), email)
