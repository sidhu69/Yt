from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from states.user import UserForm
from database.db import create_user
from keyboards.main_menu import main_menu_keyboard

router = Router()

@router.message(UserForm.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text.strip()
    if len(name) < 2:
        await message.answer("❌ Please enter a valid name")
        return

    user_id = message.from_user.id
    create_user(user_id, name=name, upi=None)  # UPI will be collected later

    await message.answer(
        f"✅ Registration Complete 🎉\n\n"
        f"👤 Name: <b>{name}</b>\n\n"
        "Type /menu to explore the bot and start earning!"
    )

    await state.clear()
