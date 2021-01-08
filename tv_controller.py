# Create a simple prototype of a TV controller in Python. It’ll use the following commands:

# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",
# if the channel N or 'name' exists in the list, or "No" - in the other case.
# The default channel turned on before all commands is №1.

channels = ['BBC', 'Discovery', 'TV1000']

class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.i = 0

    def first_channel(self):
        first_ch = self.channels[0]
        print(f'First channel from the list {first_ch}')
        return first_ch

    def last_channel(self):
        self.i = len(channels)-1
        last_ch = self.channels[self.i]
        print(f'Last channel from the list {last_ch}')
        return last_ch

    def turn_channel(self, n):
        try:
            turned_ch = self.channels[n-1]
            print(f'Okay, here you are {turned_ch}')
        except IndexError:
            print('Sorry! The channel out of the list')
        return self.current_channel()

    def next_channel(self):
        if self.i < len(self.channels)-1:
            self.i += 1
            next_ch = self.channels[self.i]
            print(f'Next channel is {next_ch}')
        else:
            print(f'Next channel is {self.channels[0]}')
        return next_ch

    def previous_channel(self):
        if self.i == 0:
            previous_ch = self.channels[len(channels)-1]
            print(f'Channel {previous_ch}')
        else:
            self.i -= 1
            previous_ch = self.channels[self.i]
            print(f'Previous channel is {previous_ch}')
        return previous_ch

    def current_channel(self):
        current_ch = self.channels[self.i]
        print(f'Current channel is {current_ch}')
        return current_ch

    def is_exist(self, name):
        if type(name) is int:
            if 0 < name-1 < 3:
                return True
            else:
                return False
        else:
            if name in self.channels:
                return True
            else:
                return False

controller = TVController(channels)
print(controller.i)
controller.next_channel()
controller.turn_channel(4)
print(controller.is_exist('BBC'))

# controller = TVController(channels)
# print(controller.first_channel() == 'BBC')
# controller.last_channel() == "TV1000"
# controller.turn_channel(1) == "BBC"
# controller.next_channel() == "Discovery"
# controller.previous_channel() == "BBC"
# controller.current_channel() == "BBC"
# controller.is_exist(4) == "No"
# controller.is_exist("BBC") == "Yes"