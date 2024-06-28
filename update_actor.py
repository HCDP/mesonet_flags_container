import os
import sys

actor_id = os.environ.get("ACTOR_ID")
tapis_client = Tapis(
    base_url = "https://dev.develop.tapis.io",
    username = os.environ.get("TAPIS_USERNAME"),
    password = os.environ.get("TAPIS_PASSWORD"),
    account_type = "user",
    tenant_id = "dev"
)

tapis_client.get_tokens()
tapis_client.streams.update_actor(actor_id = actor_id, image = sys.argv[1])