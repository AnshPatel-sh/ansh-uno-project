We've encountered a logical error where, if a player plays an incorrect card, the turn incorrectly shifts back to the previous player. We're working on fixing this issue.
A possible solution could be:
Check if the played card is valid before changing turns.
If the card is invalid, return it to the player's hand.
Keep the turn with the current player instead of moving to the previous one.
Prompt the current player to play a valid card or draw from the deck.
We'll update the code soon to implement this fix.
