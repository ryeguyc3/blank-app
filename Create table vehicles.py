CREATE TABLE IF NOT EXISTS vehicles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vin_last6 TEXT NOT NULL,              -- last 6 digits of VIN
    key_code TEXT NOT NULL,               -- two-digit key number, store as text so 01, 02 etc. are preserved
    year INTEGER,
    make TEXT,
    model TEXT,
    trim TEXT,
    color TEXT,
    mileage INTEGER,
    price REAL NOT NULL CHECK(price >= 0),
    stock_status TEXT NOT NULL DEFAULT 'available',  -- available, sold, hold, etc.
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
