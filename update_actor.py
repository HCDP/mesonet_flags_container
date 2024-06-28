import os
import sys
from tapipy.tapis import Tapis

[ image, actor_id, tapis_username, tapis_password ] = sys.argv[1:]

print(image, actor_id)
# tapis_client = Tapis(
#     base_url = "https://dev.develop.tapis.io",
#     username = os.environ.get("TAPIS_USERNAME"),
#     password = os.environ.get("TAPIS_PASSWORD"),
#     account_type = "user",
#     tenant_id = "dev"
# )

# tapis_client.get_tokens()
# tapis_client.streams.update_actor(actor_id = actor_id, image = sys.argv[1])