# Author: matt0 (matt@planet.com)
# Description: Tests the functionality of stack_finder.py

import unittest

import stack_finder


class StackFinderTest(unittest.TestCase):
    def test_find_stacks(self):
        default_scene = {
            "geometry": {
                "coordinates": [[
                    [
                        35.369952624579206,
                        31.216789643457062
                    ],
                    [
                        35.420750988391234,
                        31.175389359348845
                    ],
                    [
                        35.477637108131596,
                        31.226907952923735
                    ],
                    [
                        35.42695322789718,
                        31.268358180524043
                    ],
                    [
                        35.369952624579206,
                        31.216789643457062
                    ]
                ]]
            }
        }

        northern_scene = {
            "geometry": {
                "coordinates": [[
                    [
                        128.19634502233615,
                        -1.04336292997073
                    ],
                    [
                        128.23352242360906,
                        -1.0897399380061228
                    ],
                    [
                        128.28783572166822,
                        -1.0455725768717137
                    ],
                    [
                        128.25071101409458,
                        -0.999258432155743
                    ],
                    [
                        128.19634502233615,
                        -1.04336292997073
                    ]
                ]]
            }
        }

        # Basically just 2 northern scenes and 4 default scenes.
        # I'd expect the clustering algo to separate this into two stacks,
        # one of just default scenes and one of just northern scenes
        scenes = [
            default_scene.copy(),
            northern_scene.copy(),
            default_scene.copy(),
            northern_scene.copy(),
            default_scene.copy(),
            default_scene.copy()]

        stacks, stack_centers = stack_finder.find_stacks(scenes)

        # There should just be two stacks, the default scenes in one stack
        # and the northern scenes in another stack
        self.assertEqual(len(stacks), 2)

        # We passed in 4 default scenes
        self.assertEqual(len(stacks[0]), 4)

        # We passed in 2 northern scenes
        self.assertEqual(len(stacks[1]), 2)


if __name__ == '__main__':
    unittest.main()
