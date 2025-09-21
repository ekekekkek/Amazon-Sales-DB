# Amazon Sales Database API

A FastAPI-based REST API for managing Amazon product sales data from Kaggle. This project provides endpoints to query products, reviews, and users with a PostgreSQL database backend.

## Dataset Overview

This project uses the Amazon Sales DB dataset from Kaggle, which may include unrealistic values.

### Data Schema

| Field | Description |
|-------|-------------|
| `product_id` | Unique identifier for the product |
| `product_name` | Name of the product |
| `category` | Product category classification |
| `discounted_price` | Current discounted price |
| `actual_price` | Original price before discount |
| `discount_percentage` | Percentage discount applied |
| `rating` | Product rating (1-5 stars) |
| `rating_count` | Number of ratings received |
| `about_product` | Detailed product description |
| `user_id` | Unique identifier for the reviewer |
| `user_name` | Name of the reviewer |
| `review_id` | Unique identifier for the review |
| `review_title` | Short review summary |
| `review_content` | Full review text |
| `img_link` | URL to product image |
| `product_link` | Official product page URL |

## Project Structure

```
amazon-sql-api/
├── README.md                # This file
├── .env.example             # Environment variables template
├── db/                      # Database configuration
│   ├── docker-compose.yml   # PostgreSQL container setup
│   └── init/                # Database initialization scripts
│       ├── 01_schema.sql    # Database schema creation
│       └── 02_indexes.sql   # Database indexes for performance
├── backend/                 # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   └── app/                 # Main application code
│       ├── __init__.py
│       ├── main.py          # FastAPI application entry point
│       ├── db.py            # Database connection and session management
│       ├── models.py        # SQLAlchemy ORM models
│       ├── schemas.py       # Pydantic models for API serialization
│       └── routers/         # API route handlers
│           ├── products.py   # Product-related endpoints
│           ├── reviews.py   # Review-related endpoints
│           └── users.py     # User-related endpoints
├── scripts/                 # Utility scripts
│   └── load_csv.py          # CSV data import script
└── data/                    # Data files
    └── amazon.csv           # Raw CSV data (place your file here)
```

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Python 3.8+
- pip

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd amazon-sql-api
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Start the database**
   ```bash
   cd db
   docker-compose up -d
   ```

4. **Install Python dependencies**
   ```bash
   cd ../backend
   pip install -r requirements.txt
   ```

5. **Load the data**
   ```bash
   python scripts/load_csv.py
   ```

6. **Start the API server**
   ```bash
   python app/main.py
   ```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- **Interactive API docs**: `http://localhost:8000/docs`
- **ReDoc documentation**: `http://localhost:8000/redoc`

## Configuration

Key environment variables (see `.env.example`):
- `DATABASE_URL`: PostgreSQL connection string
- `API_HOST`: API server host (default: localhost)
- `API_PORT`: API server port (default: 8000)

## 📝 License

This project uses data from Kaggle's Amazon Sales DB dataset. Please check the original dataset license for usage terms.