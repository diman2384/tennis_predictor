from aiogram import Router
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.config import get_settings

settings = get_settings()
router = Router()


@router.message(CommandStart())
async def command_start(message: Message):
    """Handle /start command."""
    builder = InlineKeyboardBuilder()
    builder.button(
        text="🎾 Открыть Tennis Predictor",
        web_app=WebAppInfo(url=settings.MINI_APP_URL)
    )
    
    await message.answer(
        "🎾 *Добро пожаловать в Tennis Predictor!*\n\n"
        "Я помогу вам предсказать исходы теннисных матчей с помощью ИИ.\n\n"
        "Нажмите кнопку ниже, чтобы открыть приложение:",
        reply_markup=builder.as_markup()
    )


@router.message(Command("predict"))
async def command_predict(message: Message):
    """Handle /predict command."""
    await message.answer(
        "Для получения предсказания откройте приложение и выберите матч.\n\n"
        "Или нажмите кнопку ниже:",
        reply_markup=InlineKeyboardBuilder().button(
            text="🎾 Предсказать",
            web_app=WebAppInfo(url=f"{settings.MINI_APP_URL}/predict")
        ).as_markup()
    )


@router.message(Command("player"))
async def command_player(message: Message):
    """Handle /player command."""
    await message.answer(
        "Для просмотра профиля игрока откройте приложение:",
        reply_markup=InlineKeyboardBuilder().button(
            text="👤 Профиль игрока",
            web_app=WebAppInfo(url=f"{settings.MINI_APP_URL}/players")
        ).as_markup()
    )


@router.message(Command("settings"))
async def command_settings(message: Message):
    """Handle /settings command."""
    await message.answer(
        "Настройки приложения:",
        reply_markup=InlineKeyboardBuilder().button(
            text="⚙️ Настройки",
            web_app=WebAppInfo(url=f"{settings.MINI_APP_URL}/settings")
        ).as_markup()
    )