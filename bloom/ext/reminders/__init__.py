from .extension import Reminders

async def setup(bot):
    await bot.add_cog(Reminders(bot))