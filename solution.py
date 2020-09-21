#!/usr/bin/env python3

import io

import numpy as np
from PIL import Image

from aido_schemas import (Context, Duckiebot1Commands, Duckiebot1Observations, EpisodeStart, JPGImage,
                          LEDSCommands, protocol_agent_duckiebot1, PWMCommands, RGB, wrap_direct)


class RandomAgent:
    n: int

    def init(self, context: Context):
        self.n = 0
        context.info('init()')

    def on_received_seed(self, data: int):
        np.random.seed(data)

    def on_received_episode_start(self, context: Context, data: EpisodeStart):
        context.info(f'Starting episode "{data.episode_name}".')

    def on_received_observations(self, context: Context, data: Duckiebot1Observations):
        camera: JPGImage = data.camera
        _rgb = jpg2rgb(camera.jpg_data)

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


def jpg2rgb(image_data: bytes) -> np.ndarray:
    """ Reads JPG bytes as RGB"""

    im = Image.open(io.BytesIO(image_data))
    im = im.convert('RGB')
    data = np.array(im)
    assert data.ndim == 3
    assert data.dtype == np.uint8
    return data


def main():
    node = RandomAgent()
    protocol = protocol_agent_duckiebot1
    wrap_direct(node=node, protocol=protocol)


if __name__ == '__main__':
    main()
