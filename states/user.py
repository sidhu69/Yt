from aiogram.fsm.state import StatesGroup, State

class UserForm(StatesGroup):
    name = State()
    # We will add more states later like UPI, screenshot, video, etc.
