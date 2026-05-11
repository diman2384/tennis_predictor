import { useState, useEffect } from 'react'
import WebApp from '@twa-dev/sdk'

// Types
interface Match {
  id: number
  player_a: string
  player_b: string
  tournament: string
  surface: string
  time: string
}

interface Prediction {
  player_a_win_prob: number
  player_b_win_prob: number
  confidence: number
  ai_analysis: string
}

type Screen = 'home' | 'prediction' | 'player' | 'settings'

function App() {
  const [screen, setScreen] = useState<Screen>('home')
  const [user, setUser] = useState<any>(null)
  const [matches, setMatches] = useState<Match[]>([])
  const [prediction, setPrediction] = useState<Prediction | null>(null)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    // Initialize Telegram WebApp
    WebApp.ready()
    WebApp.expand()
    
    // Get user data from Telegram
    if (WebApp.initDataUnsafe?.user) {
      setUser(WebApp.initDataUnsafe.user)
    }

    // Set theme colors
    document.body.style.backgroundColor = WebApp.themeParams.bg_color || '#ffffff'
    document.body.style.color = WebApp.themeParams.text_color || '#000000'

    // Load matches
    loadMatches()
  }, [])

  const loadMatches = async () => {
    // Mock data - will be replaced with API call
    setMatches([
      { id: 1, player_a: 'Джокович Н.', player_b: 'Алькарас К.', tournament: 'ATP Finals', surface: 'Hard', time: '14:00' },
      { id: 2, player_a: 'Синнер Я.', player_b: 'Медведев Д.', tournament: 'ATP Finals', surface: 'Hard', time: '16:30' },
      { id: 3, player_a: 'Рублёв А.', player_b: 'Циципас С.', tournament: 'ATP 500', surface: 'Clay', time: '18:00' },
    ])
  }

  const getPrediction = async (matchId: number) => {
    setLoading(true)
    try {
      // Mock prediction
      setPrediction({
        player_a_win_prob: 0.62,
        player_b_win_prob: 0.38,
        confidence: 0.75,
        ai_analysis: 'Игрок A в отличной форме с серией из 5 побед. Sentiment из соцсетей положительный.'
      })
    } catch (error) {
      console.error('Prediction error:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleMatchClick = (match: Match) => {
    getPrediction(match.id)
    setScreen('prediction')
    WebApp.BackButton.show()
    WebApp.BackButton.onClick(() => {
      setScreen('home')
      WebApp.BackButton.hide()
    })
  }

  // Home Screen
  if (screen === 'home') {
    return (
      <div className="min-h-screen p-4">
        <h1 className="text-2xl font-bold mb-4">🎾 Tennis Predictor</h1>
        
        {user && (
          <p className="mb-4 text-sm opacity-70">Привет, {user.first_name}!</p>
        )}

        <div className="space-y-3">
          <h2 className="text-lg font-semibold">Сегодняшние матчи</h2>
          {matches.map((match) => (
            <div
              key={match.id}
              onClick={() => handleMatchClick(match)}
              className="bg-gray-100 dark:bg-gray-800 p-4 rounded-lg cursor-pointer active:opacity-70"
            >
              <div className="flex justify-between items-center mb-2">
                <span className="text-xs opacity-60">{match.tournament} • {match.surface}</span>
                <span className="text-xs opacity-60">{match.time}</span>
              </div>
              <div className="font-medium">
                <div>{match.player_a}</div>
                <div className="text-xs opacity-50">vs</div>
                <div>{match.player_b}</div>
              </div>
              <div className="mt-2 text-sm text-blue-500">Получить предсказание →</div>
            </div>
          ))}
        </div>
      </div>
    )
  }

  // Prediction Screen
  if (screen === 'prediction' && prediction) {
    return (
      <div className="min-h-screen p-4">
        <h1 className="text-2xl font-bold mb-4">📊 Предсказание</h1>
        
        {loading ? (
          <div className="text-center py-8">Загрузка...</div>
        ) : (
          <div className="space-y-4">
            {/* Win Probabilities */}
            <div className="bg-gray-100 dark:bg-gray-800 p-4 rounded-lg">
              <h2 className="text-lg font-semibold mb-3">Вероятность победы</h2>
              <div className="space-y-2">
                <div>
                  <div className="flex justify-between text-sm mb-1">
                    <span>Игрок A</span>
                    <span>{(prediction.player_a_win_prob * 100).toFixed(0)}%</span>
                  </div>
                  <div className="w-full bg-gray-300 rounded-full h-3">
                    <div
                      className="bg-green-500 h-3 rounded-full"
                      style={{ width: `${prediction.player_a_win_prob * 100}%` }}
                    />
                  </div>
                </div>
                <div>
                  <div className="flex justify-between text-sm mb-1">
                    <span>Игрок B</span>
                    <span>{(prediction.player_b_win_prob * 100).toFixed(0)}%</span>
                  </div>
                  <div className="w-full bg-gray-300 rounded-full h-3">
                    <div
                      className="bg-red-500 h-3 rounded-full"
                      style={{ width: `${prediction.player_b_win_prob * 100}%` }}
                    />
                  </div>
                </div>
              </div>
            </div>

            {/* Confidence */}
            <div className="bg-gray-100 dark:bg-gray-800 p-4 rounded-lg">
              <h2 className="text-lg font-semibold mb-2">Уверенность</h2>
              <div className="text-3xl font-bold text-center">
                {(prediction.confidence * 100).toFixed(0)}%
              </div>
            </div>

            {/* AI Analysis */}
            <div className="bg-gray-100 dark:bg-gray-800 p-4 rounded-lg">
              <h2 className="text-lg font-semibold mb-2">🤖 AI Анализ</h2>
              <p className="text-sm opacity-80">{prediction.ai_analysis}</p>
            </div>
          </div>
        )}
      </div>
    )
  }

  return null
}

export default App