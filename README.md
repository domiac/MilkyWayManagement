# MilkyWayManagement

## Overview:
Users can create user accounts which can invest money on our platform. They can add funds created by admins into watchlists to watch their performance overtime. Admins have to create admin accounts via the ADMIN_KEY which is give to admins only (In the starting the project section). Admins can create new funds for normal users to use.


## AI in this project
I have used Claude.ai and chatgpt in creating this read.me file and with help on the templates. It was used to fix hidden inputs in the register file. It was also used in fixing / finding a bug on the watchlist page. Especially figuring out the way of having 2 different post's in one page. It was also used in watchlist routes fixing accoring to the bug fixes found in the template. I did not find any guidelines into LLM's so that's the reasoning for these fixes.

20.10.2024.
Claude.ai was used in fixing all sql queries into a more readable form.

## Description

MilkyWayManagement is a web application developed as part of a Databases and Web Development course project. It simulates an investment platform where users can invest in various funds managed by admin investors.

## Starting the project
- all these in the terminal as follows:
- git clone https://github.com/domiac/MilkyWayManagement
- cd MilkyWayManagement
- python3 -m venv .venv
- source .venv/bin/activate
- pip3 install -r requirements.txt 

Then create a .env file and copy your credentials along with ADMIN_KEY like follows
- DATABASE_URL=postgresql:/ "Whatever it might be for you"
- SECRET_KEY = "Whatever it might be for you"
- ADMIN_KEY = admin1234
- Save

Then in the terminal:
- Flask run


## Features

### User Features
- Create and manage user accounts
- View account dashboard with total investments
- Choose fund allocations for investments
- Real-time updates on account balance and fund performance
-Watchlist feature to track new and upcoming funds

### Admin Features
- Create and manage investment funds


## User Journey

1. **Account Creation/Login**
   - New users can create an account
   - Existing users can log in securely

2. **Dashboard**
   - Users see their total investment amount
   - Quick overview of current fund allocations

3. **Investment Process**
   - Users click "Invest More" button
   - Choose investment amount and select fund(s)
   - Confirm and authorize transaction
   - Instantly see updated account balance

4. **Fund Management (Admin)**
   - Admins can create new funds
   - Monitor individual user investments
   - Track overall fund performance


