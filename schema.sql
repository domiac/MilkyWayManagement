CREATE TABLE users(id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT, admin BOOLEAN);


CREATE TABLE fund(id SERIAL PRIMARY KEY, intrest INT, fund_name TEXT, user_id INTEGER REFERENCES users, create_date DATE);


CREATE TABLE transaction(id SERIAL PRIMARY KEY, amount INT,fund_id INTEGER REFERENCES fund , user_id INTEGER REFERENCES users, sent_date DATE);


CREATE TABLE watchlist(id SERIAL PRIMARY KEY,fund_id INTEGER REFERENCES fund , user_id INTEGER REFERENCES users);

