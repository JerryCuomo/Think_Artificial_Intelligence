# Text Adventure Game Decision-Making Script
# This script simulates decision-making processes in a text adventure game.
# It evaluates various conditions such as player actions and character familiarity,
# then determines the character's response based on these factors.
# The script embodies basic principles of AI decision-making in a game setting.

def char_interaction(enter_room, knows_player, rep, has_item, action, apologizes):
    """
    Simulates character interaction based on player's actions and game context.

    Parameters:
    enter_room (bool): True if the player enters the room, False otherwise.
    knows_player (bool): True if the character knows the player, False otherwise.
    rep (str): Player's reputation, values like 'good', 'bad', or others.
    has_item (bool): True if the player has a quest item, False otherwise.
    action (str): Player's action, values like 'kind', 'aggressive', or others.
    apologizes (bool): True if the player apologizes, False otherwise.

    Returns:
    str: Description of the character's response.
    """

    # Decision process when player enters the room
    if enter_room:
        # Character's response if they know the player
        if knows_player:
            # Positive reputation leads to different interactions
            if rep == 'good':
                if has_item:
                    return 'helps_player'
                else:
                    return 'disappointment_offers_guidance'
            # Negative reputation triggers another set of responses
            elif rep == 'bad':
                response = 'refuses_help_reminds_past'
                if apologizes:
                    response += ' gives_second_chance'
                else:
                    response += ' remains_wary'
                return response
            # Neutral response for unknown or mixed reputation
            else:
                return 'neutral_acts_current_actions'
        else:
            # First impressions based on the player's action
            if action == 'kind':
                return 'becomes_friendly'
            elif action == 'aggressive':
                return 'becomes_hostile_or_fearful'
            else:
                return 'is_cautious'
    else:
        # Routine behavior when player doesn't trigger an interaction
        return 'continues_routine'

# Testing the function with specified parameters
response = char_interaction(
    enter_room=True,
    knows_player=False,
    rep='good',
    has_item=False,
    action='kind',
    apologizes=True
)
print(response) # Output the character's response based on the inputs
