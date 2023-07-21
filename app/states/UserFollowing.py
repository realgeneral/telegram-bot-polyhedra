from aiogram.dispatcher.filters.state import State, StatesGroup


class UserFollowing(StatesGroup):
    start_navigation = State()
    ask_wallet = State()
    wallet_menu = State()
    claim_all = State()
    send_API = State()
    send_statistics = State()
    new_private = State()
    new_api = State()
    get_api_keys = State()
    choose_point = State()

