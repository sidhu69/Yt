from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from states.user import UserForm
from database.db import create_user, get_user

router = Router()

@router.message(CommandStart())
async def start_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user = get_user(user_id)

    if user:
        await message.answer(f"👋 Welcome back, <b>{user[1]}</b>!\nType /menu to continue.")
        return

    await message.answer("✅ Welcome! Please enter your name:")
    await state.set_state(UserForm.name)

@router.message(UserForm.name)
async def process_name(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    name = message.text.strip()
    if len(name) < 2:
        await message.answer("❌ Please enter a valid name")
        return

    create_user(user_id, name)
    await message.answer(f"✅ Registration complete! 👤 Name: <b>{name}</b>\nType /menu to explore")
    await state.clear()
