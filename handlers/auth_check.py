# (c) @AbirHasan2005 & @HuzunluArtemis

from configs import Config

async def AuthCheck(chat_id: int, user_id: int):
    if 0 in Config.AUTH_IDS:
        print("AuthCheck - bot is public. returning true.")
        return True
    elif user_id in Config.AUTH_IDS:
        print("AuthCheck - userid found. returning true.")
        return True
    elif chat_id in Config.AUTH_IDS:
        print("AuthCheck - chat_id found. returning true.")
        return True
    else:
        print("AuthCheck - nothing found. returning false. if you did somethign wrong, read all readme")
        return False
        