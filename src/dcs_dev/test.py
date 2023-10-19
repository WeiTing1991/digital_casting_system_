import json
import os

from hal.interface import MixerStructOutput


HERE = os.path.dirname(__file__)
path = "_config"
SRC_DIR = os.path.join(HERE, path)


# Opening JSON file
f = open(SRC_DIR + "/beckhoff_controller.json")

# returns JSON object as
# a dictionary
config = json.load(f)

# Iterating through the json
# list

# Closing file
f.close()

mixer = MixerStructOutput()
print(mixer)



# print(mixer._to_list())


# mixer_params_output = mixer.output_params
# print(mixer_params_output)

# mixer_output = config["inline_mixer"]["Output"]


# for i in mixer_output:
#     for k, v in mixer_output[0].items():
#         mixer_params_output[i].update({k:v})

# print(mixer_params_output)
