CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,  -- Ensure this line exists
    phone VARCHAR(15)             -- Add this line for the phone field
);
