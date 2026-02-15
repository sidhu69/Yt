from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from states.user import UserForm
from database.db import get_user, create_user
from keyboards.main_menu import main_menu_keyboard  # We'll define this later

router = Router()


# =========================
# /start → CHECK USER + JOIN
# =========================
@router.message(CommandStart())
async def start_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    # Check if user already exists
    user = get_user(user_id)
    if user:
        wallet = user['balance']  # assuming db returns a dict-like object
        await message.answer(
            f"👋 Welcome back!\n"
            f"Your wallet balance: <b>{wallet}</b> coins\n\n"
            "👇 Select an option below:",
            reply_markup=main_menu_keyboard(user_id)
        )
        return

    # New user flow
    await message.answer(
        "✅ Welcome! Let's get you registered.\n"
        "📝 Please enter your name:\n"
        "👉 कृपया अपना नाम बताएं"
    )
    await state.set_state(UserForm.name)
