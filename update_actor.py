import os
import sys
from tapipy.tapis import Tapis
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path(os.environ.get("GITHUB_ENV"))
load_dotenv(dotenv_path = dotenv_path)

actor_id = os.environ.get("ACTOR_ID")
print(actor_id)
tapis_client = Tapis(
    base_url = "https://dev.develop.tapis.io",
    username = os.environ.get("TAPIS_USERNAME"),
    password = os.environ.get("TAPIS_PASSWORD"),
    account_type = "user",
    tenant_id = "dev"
)

tapis_client.get_tokens()
tapis_client.streams.update_actor(actor_id = actor_id, image = sys.argv[1])