#!/usr/bin/env python3

import numpy as np

from aido_schemas import EpisodeStart, protocol_agent_duckiebot1, PWMCommands, Duckiebot1Commands, LEDSCommands, RGB, wrap_direct, Context


class RandomAgent:

    def init(self, context: Context):
        self.n = 0
        context.info('init()')

    def on_received_seed(self, data: int):
        np.random.seed(data)

    def on_received_episode_start(self, context: Context, data: EpisodeStart):
        context.info(f'Starting episode "{data.episode_name}".')

    def on_received_observations(self, context: Context):
        pass

    def on_received_get_commands(self, context: Context):
        if self.n == 0:
            pwm_left = 0.0
            pwm_right = 0.0
        else:
            pwm_left = np.random.uniform(0.5, 1.0)
            pwm_right = np.random.uniform(0.5, 1.0)
        self.n += 1

        # pwm_left = 1.0
        # pwm_right = 1.0
        grey = RGB(0.0, 0.0, 0.0)
        led_commands = LEDSCommands(grey, grey, grey, grey, grey)
        pwm_commands = PWMCommands(motor_left=pwm_left, motor_right=pwm_right)
        commands = Duckiebot1Commands(pwm_commands, led_commands)
        context.write('commands', commands)

    def finish(self, context: Context):
        context.info('finish()')


def main():
    node = RandomAgent()
    protocol = protocol_agent_duckiebot1
    wrap_direct(node=node, protocol=protocol)


if __name__ == '__main__':
    main()
