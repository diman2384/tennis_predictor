# Tennis Predictor - Telegram Mini App

AI-powered tennis prediction app for Telegram Mini App platform.

## Features

- 🎾 Match predictions with probabilities
- 📊 Player analytics and form tracking
- 🤖 AI analysis (ML + LLM)
- 📱 Sentiment analysis from social media and news
- 💬 Telegram Mini App interface

## Quick Start

### Prerequisites

- Docker & Docker Compose
- Telegram Bot Token (from @BotFather)

### Setup

1. Clone the repository
2. Copy environment file:
   ```bash
   cp .env.example .env
   ```
3. Set your Telegram Bot Token in `.env`
4. Start the services:
   ```bash
   docker-compose up -d
   ```

### Development

**Backend:**
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## Project Structure

```
tennis_predictor/
├── backend/           # FastAPI backend
│   ├── app/
│   │   ├── api/       # API routes
│   │   ├── models/    # Database models
│   │   ├── services/  # Business logic
│   │   ├── ml/        # ML models
│   │   └── telegram/  # Telegram bot
│   └── requirements.txt
├── frontend/          # React Mini App
│   └── src/
├── docker-compose.yml
└── plans/             # Architecture docs
```

## API Endpoints

- `GET /health` - Health check
- `GET /api/matches/upcoming` - Upcoming matches
- `POST /api/predict/match` - Get match prediction
- `GET /api/players/{id}` - Player profile
- `GET /api/players/{id}/form` - Player form
- `GET /api/players/{id}/sentiment` - Sentiment analysis

## Tech Stack

- **Backend:** FastAPI, SQLAlchemy, PostgreSQL, Redis
- **ML:** XGBoost, scikit-learn, LangChain
- **Frontend:** React, TypeScript, TailwindCSS
- **Telegram:** aiogram, @twa-dev/sdk

## License

MIT