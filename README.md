# MilkyWayManagement

## Current state DELETE LATER WHEN FINE TUNING:
MilkyWayManagement is in a good state. The Main functions are working well. The Database needs some tweaking for example if a user is trying to create a same named user it increments the running id without creating the user. This might create problems with overhang in larger projects. I need to finish the admin interface of adding "funds". Then last step is to add a calculator for a certain timeperiod which will simulate the gains for each user.


## AI in this project
I have used Claude.ai and chatgpt in creating this read.me file and with help on the templates. It was used to fix hidden inputs in the register file. I did not find any guidelines into LLM's so that's the reasoning for these fixes.

## Description

MilkyWayManagement is a web application developed as part of a Databases and Web Development course project. It simulates an investment platform where users can invest in various funds managed by admin investors.

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


