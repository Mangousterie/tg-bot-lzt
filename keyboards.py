from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_main_keyboard() -> InlineKeyboardMarkup:
    """Главное меню"""
    builder = InlineKeyboardBuilder()
    
    builder.row(
        InlineKeyboardButton(text="💰 Пополнить баланс", callback_data="balance")
    )
    builder.row(
        InlineKeyboardButton(text="🛒 Купить", callback_data="buy")
    )
    builder.row(
        InlineKeyboardButton(text="🆘 Поддержка", callback_data="support")
    )
    builder.row(
        InlineKeyboardButton(text="❓ FAQ", callback_data="faq")
    )
    
    return builder.as_markup()


def get_balance_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура пополнения баланса"""
    builder = InlineKeyboardBuilder()
    
    builder.row(
        InlineKeyboardButton(text="100 ₽", callback_data="pay_100"),
        InlineKeyboardButton(text="500 ₽", callback_data="pay_500"),
        InlineKeyboardButton(text="1000 ₽", callback_data="pay_1000")
    )
    builder.row(
        InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_main")
    )
    
    return builder.as_markup()


def get_buy_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура покупок"""
    builder = InlineKeyboardBuilder()
    
    builder.row(
        InlineKeyboardButton(text="📦 Товар 1", callback_data="product_1")
    )
    builder.row(
        InlineKeyboardButton(text="📦 Товар 2", callback_data="product_2")
    )
    builder.row(
        InlineKeyboardButton(text="📦 Товар 3", callback_data="product_3")
    )
    builder.row(
        InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_main")
    )
    
    return builder.as_markup()


def get_back_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура с кнопкой назад"""
    builder = InlineKeyboardBuilder()
    
    builder.row(
        InlineKeyboardButton(text="◀️ Назад в меню", callback_data="back_to_main")
    )
    
    return builder.as_markup()