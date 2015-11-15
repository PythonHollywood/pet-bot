"""Skeleton for Pet Class"""
import json

DEFAULT_STATE = dict(
    awake=True,
    hunger=50,
    energy=50,
    damage=50,
    mood=50,
    alertness=50)


class Pet(object):
    def __init__(self, state_file=None, initial_state=None, **kwargs):
        """Creator method for the pet.

        Args:
            state_file: filename for the json file where state is saved.
            If left empty, the state will only be stored in memory and
            thus not recoverable after the program has ended.

            initial_state (dict): dictionary containing initial values
            for the states. If empty, values from state_file will be used.
            If file does not exist or data is missing, default states will
            be added.

            **kwargs: Alternative way to specify initial states for individual
            state variables. Overrides initial_state and state_file.
        """
        self.state_file = state_file
        self.state = DEFAULT_STATE
        if self.state_file:
            try:
                with open(state_file) as f:
                    self.state.update(json.load(f))
            except IOError:
                pass
        self.update_state(initial_state, **kwargs)

    def increment_time(self):
        """Some states should be updated as time progresses. This is done
        every time this method is called."""
        self.adjust_state(hunger=1)

    def _update_state_file(self):
        """Updates the state json file with the current state.
        If self.state_file is None, the state is just stored
        in memory and nothing will happen.
        """
        if self.state_file:
            with open(self.state_file, mode='w') as f:
                json.dump(self.state, f)

    def update_state(self, new_state=None, **kwargs):
        """Update state to new_state or **kwargs.
        **kwargs override new_state (this allows overriding one value in new_state)

        Args:
            new_state: dict containing the updated state variables. Any state variable
                not specified will be left untouched.
            **kwargs: Key-value pairs specifying the new state. Overrides new_state.
        """
        if new_state is None:
            new_state = {}
        self.state.update(new_state, **kwargs)
        self._update_state_file()
        pass

    def adjust_state(self, adjustments=None, **kwargs):
        """Make a relative adjustment of the state from the current
        based on dict or keyword arguments. **kwargs override adjustments
        (this allows overriding one value in adjustments)

        Args:
            adjustments: A dict containing relative adjustments for states.

            **kwargs: Key-value pairs containing relative adjustments for states.
            Overrides adjustments. For added clarity, one can use the unity operator
            when making positive adjustments. For example:
                self.adjust_state(mood=+1)

        Raises:
            KeyError: if adjustments or kwargs contain a key that is not defined
            in self.state, KeyError will be raised.
        """
        if adjustments is None:
            adjustments = {}
        adjustments = adjustments.copy()
        adjustments.update(**kwargs)
        new_state = {}
        for key in adjustments:
            new_state[key] = self.state[key] + adjustments[key]
        self.update_state(new_state)

    def interact_with(self, action=''):
        """This method should take an arbitrary string as an argument
        and figure out which action is to be performed. That action shall
        then be run and the response returned.

        Perform an action specified in string action. If action string
        is empty or undefined, create a response based on current state.
        """
        selector = {
            'spank': self.action_spank,
            'feed': self.action_feed}
        return selector.get(action.lower(), self.action_else)()

    def action_spank(self):
        """Example action method. Prefix these with action to make them
        easy to identify."""

        # update state
        self.update_state()
        # or
        self.adjust_state()

        # create response string
        response = 'Ouch!'

        return response

    def action_feed(self):
        self.adjust_state(hunger=-1)
        return 'Yummy!'

    def action_else(self):
        return 'I don\'t know what to do with that'

    def speak(self):
        """Craft a phrase (<140 char) describing the current state of the pet"""
        return 'I\'m hungry'


if __name__ == '__main__':
    # Just some example code, don't try running at this point
    pet = Pet('state.json', mood=0)
    pet.increment_time()
    print pet.interact_with('here, have som food')
    print pet.interact_with()
