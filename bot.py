from pyrogram import Client, errors

# Your API credentials
API_ID = 29737595
API_HASH = "b35140b7172a12ba745587952560e4da"
CHANNEL_ID = -1002335581846  # Your Channel ID

# Initialize Pyrogram client
app = Client("my_userbot", api_id=API_ID, api_hash=API_HASH)

async def approve_requests():
    async with app:
        try:
            # Fetch and approve join requests one by one
            async for request in app.get_chat_join_requests(CHANNEL_ID):
                try:
                    if hasattr(request, "user"):
                        user_id = request.user.id  # Some versions might use `request.user.id`
                    else:
                        user_id = request.from_user.id  # Older versions might use `from_user`

                    await app.approve_chat_join_request(CHANNEL_ID, user_id)
                    print(f"Approved: {user_id}")
                except errors.RPCError as e:
                    print(f"Error approving {user_id}: {e}")
                except Exception as e:
                    print(f"Unexpected error: {e}")

        except errors.RPCError as e:
            print(f"Error fetching requests: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Run the function
app.run(approve_requests())
