from math import floor
import pkmbasestats

"""
Functions to calculate a pokemons's CP and HP based on their individual and base stats.
"""

def calculateCP(mon_id, level, atk_iv, def_iv, stam_iv):
    stats = pkmbasestats.get_pkm_base_stats(mon_id)
    return floor((stats[0] + atk_iv) * (stats[1] + def_iv)**0.5 * (stats[2] + stam_iv)**0.5 * CPScalar(level) / 10)

def calculateHP(mon_id, level, stam_iv):
    stats = pkmbasestats.get_pkm_base_stats(mon_id)
    return floor((stats[2] + stam_iv) * CPScalar(level)**0.5)

# utility function to generate the CP Scalar used in CP and HP calculations
def CPScalar(level):
    if 41 > level >= 30.5:
        scalar = (0.00891892 * (level - 30)) + 0.53538485
    elif 30.5 > level >= 20.5:
        scalar = (0.01784981 * (level - 20)) + 0.35688675
    elif 20.5 > level >= 10.5:
        scalar = (0.01783805 * (level - 10)) + 0.17850625
    else:
        scalar = (0.01885225 * level) - 0.01001625
    return scalar
