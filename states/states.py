from aiogram.dispatcher.filters.state import State, StatesGroup


class Start(StatesGroup):
    waiting_for_tz = State()


class NewCountdown(StatesGroup):
    waiting_for_format = State()
    waiting_for_name = State()
    waiting_for_preference = State()
    waiting_for_dt = State()


class MyCountdowns(StatesGroup):
    browsing_cds = State()
    countdown_selected = State()
    edit_name = State()
    edit_dt = State()
