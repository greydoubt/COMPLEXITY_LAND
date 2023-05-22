# The Wizard's Spellbook

'''In the enchanted land of Arcania, a group of wizards gather to study and master the art of magic. Each wizard possesses a unique spellbook containing a collection of spells. To unlock the secrets of powerful spells, the wizards need to combine spells from different spellbooks in a specific order.

The goal is to determine if it is possible to create a specific sequence of spells by selecting spells from the available spellbooks while adhering to certain rules.

Each wizard can only choose one spell from their spellbook at a time, and once a spell is chosen, it cannot be unselected. The order in which the wizards select spells is fixed and must be followed. Additionally, the final sequence of spells must match the desired target sequence exactly, without any additional spells.

Your task is to determine whether it is possible to create the desired sequence of spells by selecting spells in the correct order and following the rules of the wizard's gathering.

This problem falls into the complexity class of NP, as we can easily verify a proposed solution in polynomial time by checking if the selected spells are in the correct order and if the final sequence matches the target sequence.'''

def verify_wizard_spellbook(spellbooks, wizards_order, target_sequence):
    sequence = []

    # Iterate through the wizards in the specified order
    for wizard in wizards_order:
        # Check if the wizard has a spellbook
        if wizard in spellbooks:
            spellbook = spellbooks[wizard]

            # Select the next spell from the wizard's spellbook
            if spellbook:
                spell = spellbook.pop(0)
                sequence.append(spell)

        # Check if the current sequence matches the target sequence
        if sequence == target_sequence:
            return "The desired sequence of spells can be created!"

    # If the loop completes without finding a match, the sequence cannot be created
    return "The desired sequence of spells cannot be created."

# Example usage
spellbooks = {
    "Merlin": ["Fireball", "Teleport", "Invisibility"],
    "Gandalf": ["Lightning Bolt", "Healing", "Shield"],
    "Hermione": ["Levitation", "Expelliarmus", "Polyjuice Potion"]
}
wizards_order = ["Merlin", "Gandalf", "Hermione"]
target_sequence = ["Fireball", "Teleport", "Invisibility", "Lightning Bolt", "Healing", "Shield"]

result = verify_wizard_spellbook(spellbooks, wizards_order, target_sequence)
print(result)



'''the spellbooks dictionary represents the available spellbooks possessed by the wizards. Each wizard is a key, and their spellbook is a list of spells. The wizards_order list specifies the order in which the wizards select spells. The target_sequence list represents the desired sequence of spells.

The verify_wizard_spellbook() function takes these parameters as input and verifies if it is possible to create the desired sequence of spells. It iterates through the wizards in the specified order and checks if each wizard has a spellbook. If a spellbook exists, it selects the next spell and adds it to the sequence. It then checks if the current sequence matches the target sequence. If the spells are selected in the correct order and the final sequence matches the target sequence, the function returns a positive result indicating that the desired sequence of spells can be created.'''