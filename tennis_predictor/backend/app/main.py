from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.config import get_settings
from app.database import init_db, close_db
from app.api.router import api_router
from app.telegram import bot, dp
from app.telegram.handlers import router as handlers_router
import asyncio

settings = get_settings()


async def start_bot():
    """Start Telegram bot polling in background."""
    dp.include_router(handlers_router)
    await dp.start_polling(bot)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan."""
    # Startup
    await init_db()
    print("Database initialized")
    
    # Start bot in background task
    if settings.TELEGRAM_BOT_TOKEN:
        asyncio.create_task(start_bot())
        print("Telegram bot started")
    
    yield
    
    # Shutdown
    await close_db()
    print("Database connection closed")
    
    if settings.TELEGRAM_BOT_TOKEN:
        await bot.session.close()


app = FastAPI(
    title=settings.APP_NAME,
    description="Tennis Predictor Telegram Mini App API",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS middleware for Mini App
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.MINI_APP_URL, "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api")


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok", "version": "0.1.0"}