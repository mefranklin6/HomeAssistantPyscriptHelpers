"""Module to handle light actions in Home Assistant Pyscript"""

# Place any light objects you don't want affected here
# Example include lights that are already part of a deconz group
ignore_lights = [
]

# Include keywords for switch objects that are not tied to light switches or switched outlets
ignore_switches_keywords = [
    "adaptive_lighting",
    "camera",
    "cablemodem",
    "roborock",
    "nodered",
    "unifi",
]

ADAPTIVE_LIGHTING_SLEEP_KEYWORD = "adaptive_lighting_sleep_mode"


class LightHelper:
    def __init__(self):
        self.all_lights = state.names(domain="light")
        self.all_switches = state.names(domain="switch")
        self.ignore_lights = ignore_lights
        self.ignore_switches_keywords = ignore_switches_keywords
        self.adaptive_lighting_sleep_keyword = ADAPTIVE_LIGHTING_SLEEP_KEYWORD

    def all_lights_off(self):
        for light_ in self.all_lights:
            if light_ in self.ignore_lights:
                continue
            light.turn_off(entity_id=light_)

        for switch_ in self.all_switches:
            ignore = False
            for keyword in self.ignore_switches_keywords:
                if keyword in switch_:
                    ignore = True
                    break
            if ignore:
                continue
            switch.turn_off(entity_id=switch_)

    def adaptive_sleep_mode(self, desired_state):
        adaptive_lighting_switches = [
            ad_sw
            for ad_sw in self.all_switches
            if self.adaptive_lighting_sleep_keyword in ad_sw
        ]
        for ad_sw in adaptive_lighting_switches:
            (
                switch.turn_on(entity_id=ad_sw)
                if desired_state == "on"
                else switch.turn_off(entity_id=ad_sw)
            )
