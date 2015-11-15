"""Command Line Interface for the Pet class.
Can be used as a demonstration of the class or
as a convenient way to test new functionality.
"""

from pet import Pet


if __name__ == '__main__':
    p = Pet()
    print 'Type something to interact or type "quit" to quit.'

    while True:
        interaction = raw_input()
        if interaction.lower() == 'quit':
            break

        p.increment_time()
        print p.interact_with(interaction)
