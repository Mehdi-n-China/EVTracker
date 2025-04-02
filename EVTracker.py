
"""
This program is designed to help you track card counts, make perfect strategy decisions, and beat the house in

blackjack by providing real-time guidance and optimal betting strategies. It automatically keeps a running count

of cards using the Zen Count system, adjusts the true count based on the number of decks remaining, and presents

the most accurate information possible to help you make informed decisions. By integrating exact card theory and

perfect deviations, the program ensures that you play each hand optimally, effectively beating the house edge and

maximizing your chances of winning. It also identifies profitable betting opportunities by suggesting when to

increase or decrease your bets based on favorable or unfavorable counts, giving you the ability to capitalize on

situations where the odds are in your favor. A special thanks goes to the Wizard of Odds for providing their API,

which serves as a reliable source for accurate calculations, strategy charts, and other essential data. Their

expertise ensures that the program is grounded in trusted mathematical principles, giving you a competitive edge

at the blackjack table. With this program, you'll be well-equipped to approach blackjack with confidence, reduce

the house edge, and increase your chances of walking away a winner.

Good luck, and remember: with the right strategy, the house doesn't always have to win!
"""

from Functions import window_open

always_on_top = True

window_open(always_on_top)
