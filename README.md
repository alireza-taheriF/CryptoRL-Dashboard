# CryptoRL Dashboard

A web-based dashboard for displaying live cryptocurrency prices using React and FastAPI.

## 📋 Features

- 📊 Live cryptocurrency price display
- 🔄 Auto-refresh every 10 seconds
- 🎨 Simple and user-friendly interface
- ⚡ Fast API with FastAPI
- 🌐 CORS support for local development
- 💾 Data caching for improved performance

## 🏗️ Project Architecture

```
cryptorl-dashboard/
├── backend/                 # FastAPI backend
│   ├── main.py             # Main entry point
│   ├── routes/             # API routes
│   │   └── price.py        # Price-related routes
│   ├── services/           # External services
│   │   └── coingecko.py    # CoinGecko API integration
│   └── models/             # Data models
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   │   ├── Dashboard.jsx
│   │   │   └── PriceCard.jsx
│   │   ├── pages/          # Main pages
│   │   │   ├── Home.jsx
│   │   │   ├── About.jsx
│   │   │   └── Portfolio.jsx
│   │   └── App.js          # Main component
│   └── public/
├── data/                   # Project data
└── rl_agent/              # Reinforcement Learning agent (in development)
```

## 🚀 Installation & Setup

### Prerequisites

- Node.js (version 16 or higher)
- Python 3.8+
- pip

### 1. Clone the Repository

```bash
git clone <repository-url>
cd cryptorl-dashboard
```

### 2. Backend Setup

```bash
# Install Python dependencies
pip install fastapi uvicorn requests

# Run the server
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The backend server will be available at `http://localhost:8000`.

### 3. Frontend Setup

```bash
# Install Node.js dependencies
cd frontend
npm install

# Run development server
npm start
```

The frontend application will be available at `http://localhost:3000`.

## 🔌 API Endpoints

### GET `/`
- **Description**: Check API status
- **Response**: `{"message": "CryptoRL Dashboard API is running."}`

### GET `/price/live`
- **Description**: Get live cryptocurrency prices
- **Supported Currencies**: Bitcoin, Ethereum, Shiba Inu, Tether
- **Sample Response**:
```json
{
  "bitcoin": {"usd": 45000},
  "ethereum": {"usd": 3000},
  "shiba-inu": {"usd": 0.00001},
  "tether": {"usd": 1.00}
}
```

## 🛠️ Technologies Used

### Backend
- **FastAPI**: Fast web framework for Python
- **Uvicorn**: ASGI server
- **Requests**: HTTP library
- **CoinGecko API**: Cryptocurrency data source

### Frontend
- **React 18**: UI library
- **React Router DOM**: Routing
- **CSS**: Styling

## 📊 Key Features

### Data Caching
- Data is cached for 30 seconds
- Reduces external API requests
- Improves response speed

### Auto-refresh
- Prices update every 10 seconds automatically
- Manual refresh available with Refresh button

### User Interface
- Simple and user-friendly design
- Prices displayed in separate cards
- Easy navigation between pages

## 🔧 Development

### Adding New Cryptocurrency

1. In `backend/services/coingecko.py`, add the new currency to the `ids` parameter:
```python
params = {
    "ids": "bitcoin,ethereum,shiba-inu,tether,your-new-coin",
    "vs_currencies": "usd"
}
```

2. Add the corresponding icon in `frontend/src/coinIcons.js`.

### Changing Update Interval

In `frontend/src/components/Dashboard.jsx`:
```javascript
const interval = setInterval(fetchPrices, 10000); // 10 seconds
```

## 🚧 Future Features

- [ ] Add price charts
- [ ] Implement reinforcement learning agent
- [ ] Add personal portfolio
- [ ] Price change notifications
- [ ] Support for more cryptocurrencies
- [ ] Dark/Light mode toggle

## 🤝 Contributing

1. Fork the project
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 📞 Contact

For questions or suggestions, please create an Issue.

---

**Note**: This project is under active development and may undergo further changes in the future.