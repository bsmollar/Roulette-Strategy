##Introduction
The purpose of this program is to test a roulette betting strategy.

##Technologies Used
VS Code, Jupyter Notebook, Python Editor

##The Strategy
The idea of the strategy is to wait until the same color has been spun twice in a row. The program will then subsequently bet on the opposite color. On the next spin, if the program wins, it goes back to waiting. If it loses, the bet is doubled and placed on the same color. There is a bet limit of $100 and an initial bet of $5. If the bet exceeds $100, it resets to $5. If you want to change this, both values can be found in the place_initial_bet() and double_bet_amount() functions.

##Results
I found that without a bet limit, or one that is relatively high to the initial bet, the player will win. When a bet limit is introduced, the player consistently loses. 
