from aiogram.dispatcher.filters.state import State, StatesGroup


class UserFollowing(StatesGroup):
    start_navigation = State()
    ask_wallet = State()
    send_statistics = State()

