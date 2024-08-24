class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1647602447"
    sudo_users = "1647602447"
    GROUP_ID = -1002210286036
    TOKEN = "7452110956:AAE3DCldVOdNpBimfS0G6-LxvsHIlBES1Rk"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "@Anime_Chat_Group_International"
    UPDATE_CHAT = "@Anime_Chat_Group_International"
    BOT_USERNAME = "itachigrab_bot"
    CHARA_CHANNEL_ID = "-1002210286036"
    api_id = 22257865
    api_hash = "97fc23c20e06f411abbf36cad8e118ce"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
