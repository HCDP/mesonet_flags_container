import os
import sys
from tapipy.tapis import Tapis

[ image, actor_id, tapis_username, tapis_password ] = sys.argv[1:]

tapis_client = Tapis(
    base_url = "https://dev.develop.tapis.io",
    username = tapis_username,
    password = tapis_password,
    account_type = "user",
    tenant_id = "dev"
)

tapis_client.get_tokens()
tapis_client.actors.update_actor(actor_id = actor_id, image = image)