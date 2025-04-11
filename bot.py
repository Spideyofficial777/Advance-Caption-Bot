import asyncio
from pyrogram import Client, idle
from info import *

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="AutoCap",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "body"},
            sleep_threshold=15,
        )
        self.force_channel = FORCE_SUB
        self.invitelink = None

    async def start(self):
        await super().start()
        me = await self.get_me()

        # Check force-sub channel
        if self.force_channel:
            try:
                if not str(self.force_channel).startswith("-100"):
                    self.force_channel = f"-100{int(self.force_channel)}"
                self.invitelink = await self.export_chat_invite_link(self.force_channel)
            except Exception as e:
                print(f"[ERROR] Force-subscription setup failed: {e}")
                print("⚠️ Make sure the bot is admin in the force-sub channel.")
                self.force_channel = None

        print(f"✅ {me.first_name} is started successfully!")
        try:
            await self.send_message(
                ADMIN,
                f"✨ **{me.first_name} is up and running!**\n\n💬 Username: @{me.username}\n🆔 ID: `{me.id}`"
            )
        except Exception as e:
            print(f"[WARNING] Could not send start message to admin: {e}")

    async def stop(self, *args):
        print("🛑 Bot is shutting down...")
        await super().stop()
        print("✅ Bot stopped cleanly.")

# Create bot instance
bot = Bot()

# Run it with asyncio
async def main():
    await bot.start()
    await idle()
    await bot.stop()

if __name__ == "__main__":
    asyncio.run(main())
