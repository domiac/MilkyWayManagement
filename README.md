# MilkyWayManagement

## Current state DELETE LATER WHEN FINE TUNING:
MilkyWayManagement is in a good state. The Main functions are working well. The Database needs some tweaking for example if a user is trying to create a same named user it increments the running id without creating the user. This might create problems with overhang in larger projects. Need to fix the admin feature registration feature. And finish the fund simulation. Then the program is finished. To create an admin user when registering use create .env where ADMIN_KEY = admin1234


## AI in this project
I have used Claude.ai and chatgpt in creating this read.me file and with help on the templates. It was used to fix hidden inputs in the register file. It was also used in fixing / finding a bug on the watchlist page. Especially figuring out the way of having 2 different post's in one page. It was also used in watchlist routes fixing accoring to the bug fixes found in the template. I did not find any guidelines into LLM's so that's the reasoning for these fixes.

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
- View account dashboard with total investments and interest earnings
- Set up monthly investment plans
- Choose fund allocations for investments
- Real-time updates on account balance and fund performance

### Admin Features
- Create and manage investment funds
- View user investments in each fund
- Monitor overall fund performance
- Access detailed reports on total investments and interest earned

## User Journey

1. **Account Creation/Login**
   - New users can create an account
   - Existing users can log in securely

2. **Dashboard**
   - Users see their total investment amount and interest earned
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


