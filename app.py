if __name__ == "__main__":
    from aiogram import executor
    from bot import dp

    executor.start_polling(dp, skip_updates=True)