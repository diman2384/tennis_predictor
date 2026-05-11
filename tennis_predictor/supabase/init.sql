-- Supabase database initialization script
-- Run this in Supabase SQL Editor

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    telegram_id BIGINT UNIQUE NOT NULL,
    username VARCHAR(100),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    language_code VARCHAR(10),
    is_premium BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- User settings table
CREATE TABLE IF NOT EXISTS user_settings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE REFERENCES users(id),
    notifications_enabled BOOLEAN DEFAULT TRUE,
    prediction_types JSONB DEFAULT '["match_winner"]',
    favorite_players JSONB DEFAULT '[]',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Players table
CREATE TABLE IF NOT EXISTS players (
    id SERIAL PRIMARY KEY,
    api_id INTEGER UNIQUE NOT NULL,
    name VARCHAR(200) NOT NULL,
    country VARCHAR(3),
    ranking INTEGER,
    age INTEGER,
    height INTEGER,
    weight INTEGER,
    plays VARCHAR(20),
    turned_pro INTEGER,
    photo_url VARCHAR(500),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Matches table
CREATE TABLE IF NOT EXISTS matches (
    id SERIAL PRIMARY KEY,
    api_id INTEGER UNIQUE,
    player_id INTEGER REFERENCES players(id),
    opponent_id INTEGER REFERENCES players(id),
    tournament VARCHAR(200),
    surface VARCHAR(20),
    round VARCHAR(50),
    date TIMESTAMP WITH TIME ZONE,
    is_completed BOOLEAN DEFAULT FALSE,
    winner_id INTEGER,
    score VARCHAR(200),
    stats JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Player form table
CREATE TABLE IF NOT EXISTS player_form (
    id SERIAL PRIMARY KEY,
    player_id INTEGER UNIQUE REFERENCES players(id),
    win_rate_10 FLOAT,
    win_rate_20 FLOAT,
    win_rate_50 FLOAT,
    win_rate_100 FLOAT,
    current_streak INTEGER,
    aces_per_match FLOAT,
    double_faults_per_match FLOAT,
    serve_win_pct FLOAT,
    return_win_pct FLOAT,
    break_points_saved_pct FLOAT,
    rest_days INTEGER,
    injury_risk FLOAT,
    form_score FLOAT,
    last_matches JSONB DEFAULT '[]',
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Player sentiment table
CREATE TABLE IF NOT EXISTS player_sentiment (
    id SERIAL PRIMARY KEY,
    player_id INTEGER UNIQUE REFERENCES players(id),
    overall_score FLOAT,
    social_score FLOAT,
    news_score FLOAT,
    positive_news_count INTEGER DEFAULT 0,
    negative_news_count INTEGER DEFAULT 0,
    neutral_news_count INTEGER DEFAULT 0,
    recent_posts JSONB DEFAULT '[]',
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Predictions table
CREATE TABLE IF NOT EXISTS predictions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    match_id INTEGER REFERENCES matches(id),
    prediction_type VARCHAR(50),
    player_a_win_prob FLOAT,
    player_b_win_prob FLOAT,
    confidence FLOAT,
    ai_analysis TEXT,
    sentiment_impact VARCHAR(50),
    is_correct BOOLEAN,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_users_telegram_id ON users(telegram_id);
CREATE INDEX IF NOT EXISTS idx_matches_player_id ON matches(player_id);
CREATE INDEX IF NOT EXISTS idx_matches_date ON matches(date);
CREATE INDEX IF NOT EXISTS idx_predictions_user_id ON predictions(user_id);
CREATE INDEX IF NOT EXISTS idx_predictions_created_at ON predictions(created_at);

-- Enable Row Level Security (RLS)
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE user_settings ENABLE ROW LEVEL SECURITY;
ALTER TABLE players ENABLE ROW LEVEL SECURITY;
ALTER TABLE matches ENABLE ROW LEVEL SECURITY;
ALTER TABLE player_form ENABLE ROW LEVEL SECURITY;
ALTER TABLE player_sentiment ENABLE ROW LEVEL SECURITY;
ALTER TABLE predictions ENABLE ROW LEVEL SECURITY;

-- Create policies for public read access (for MVP)
CREATE POLICY "Public read access" ON players FOR SELECT USING (true);
CREATE POLICY "Public read access" ON matches FOR SELECT USING (true);
CREATE POLICY "Public read access" ON player_form FOR SELECT USING (true);
CREATE POLICY "Public read access" ON player_sentiment FOR SELECT USING (true);