from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from keyboards import (
    get_main_keyboard, 
    get_balance_keyboard, 
    get_buy_keyboard, 
    get_back_keyboard
)
from config import ABOUT_TEXT, FAQ_TEXT, SUPPORT_TEXT, BALANCE_TEXT, BUY_TEXT

router = Router()


# ===== КОМАНДА /start =====
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        text=ABOUT_TEXT,
        reply_markup=get_main_keyboard(),
        parse_mode="HTML"
    )


# ===== ПОПОЛНИТЬ БАЛАНС =====
@router.callback_query(F.data == "balance")
async def callback_balance(callback: CallbackQuery):
    await callback.message.edit_text(
        text=BALANCE_TEXT,
        reply_markup=get_balance_keyboard(),
        parse_mode="HTML"
    )
    await callback.answer()


# ===== ОБРАБОТКА ОПЛАТЫ =====
@router.callback_query(F.data.startswith("pay_"))
async def callback_payment(callback: CallbackQuery):
    amount = callback.data.split("_")[1]
    await callback.answer(
        f"💳 Оплата на сумму {amount} ₽ в разработке...", 
        show_alert=True
    )


# ===== КУПИТЬ =====
@router.callback_query(F.data == "buy")
async def callback_buy(callback: CallbackQuery):
    await callback.message.edit_text(
        text=BUY_TEXT,
        reply_markup=get_buy_keyboard(),
        parse_mode="HTML"
    )
    await callback.answer()


# ===== ОБРАБОТКА ПОКУПКИ ТОВАРА =====
@router.callback_query(F.data.startswith("product_"))
async def callback_product(callback: CallbackQuery):
    product_id = callback.data.split("_")[1]
    await callback.answer(
        f"📦 Покупка товара #{product_id} в разработке...", 
        show_alert=True
    )


# ===== ПОДДЕРЖКА =====
@router.callback_query(F.data == "support")
async def callback_support(callback: CallbackQuery):
    await callback.message.edit_text(
        text=SUPPORT_TEXT,
        reply_markup=get_back_keyboard(),
        parse_mode="HTML"
    )
    await callback.answer()


# ===== FAQ =====
@router.callback_query(F.data == "faq")
async def callback_faq(callback: CallbackQuery):
    await callback.message.edit_text(
        text=FAQ_TEXT,
        reply_markup=get_back_keyboard(),
        parse_mode="HTML"
    )
    await callback.answer()


# ===== НАЗАД В ГЛАВНОЕ МЕНЮ =====
@router.callback_query(F.data == "back_to_main")
async def callback_back(callback: CallbackQuery):
    await callback.message.edit_text(
        text=ABOUT_TEXT,
        reply_markup=get_main_keyboard(),
        parse_mode="HTML"
    )
    await callback.answer()