if __name__ == "__main__":
    from aiogram import executor
    from bot import app, dp

    app.start()
    executor.start_polling(dp, skip_updates=True)
