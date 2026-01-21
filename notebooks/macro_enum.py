from enum import Enum

class SpaceControl(Enum):
    NONE = "none"
    # Does not meaningfully influence positioning or spatial pressure

    MOBILITY = "mobility"
    # Allows the caster to reposition quickly
    # Used to engage, disengage, rotate, or dodge without affecting enemy position

    DISPLACEMENT = "displacement"
    # Forces enemies to move against their will
    # Breaks formations, pushes targets into danger, or removes them from safe zones

    ZONE = "zone"
    # Creates an area enemies are pressured to avoid
    # Controls movement by threat rather than force

    TERRAIN = "terrain"
    # Alters the map layout
    # Creates or removes paths, walls, or obstacles that reshape fights

    ANCHOR = "anchor"
    # Restricts movement relative to a point or target
    # Prevents repositioning and limits escape options

    ISOLATION = "isolation"
    # Separates targets from allies, routes, or objectives
    # Cuts off interaction paths to enable focused punishment


class TempoControl(Enum):
    NONE = "none"
    # Does not meaningfully change the flow or timing of combat

    BURST = "burst"
    # Compresses damage or impact into a very short time window
    # Aims to overwhelm reactions or instantly swing fights

    POKE = "poke"
    # Applies repeated, low-commit pressure over time
    # Gradually erodes health or resources before full engagement

    DELAY = "delay"
    # Slows down actions, objectives, or fight resolution
    # Buys time or disrupts enemy timing

    INTERRUPT = "interrupt"
    # Breaks or cancels ongoing actions
    # Denies execution of planned plays or combos

    RESET = "reset"
    # Reverses prior progress or restores a neutral state
    # Forces fights or situations to be replayed on new terms


class InformationControl(str, Enum):
    NONE = "none"
    # Does not meaningfully affect what either team knows

    TRUE_STEALTH = "true_stealth"
    # Completely removes the caster from enemy awareness
    # No visual, no minimap, no reliable cues

    CONCEALMENT = "concealment"
    # Hides strategic information while leaving partial cues
    # Enemies may sense presence but lack certainty

    REVEAL = "reveal"
    # Actively exposes enemy positions or states
    # Removes fog-of-war advantages

    PRESENCE_CHECK = "presence_check"
    # Confirms existence without full vision
    # Used to probe areas or deny ambushes

    EXPLICIT_DISCLOSURE = "explicit_disclosure"
    # Publicly broadcasts information to both teams
    # Shapes expectations and forces reactions through certainty


class AgencyControl(Enum):
    NONE = "none"
    # Does not meaningfully restrict or alter player control

    FORCED_ACTION = "forced_action"
    # Pushes the target into specific movement or behavior
    # Player input exists but outcome is guided

    HARD_CC = "hard_cc"
    # Fully removes control from the target
    # Guarantees interruption and vulnerability

    SOFT_CC = "soft_cc"
    # Partially limits available actions
    # Weakens response options without full shutdown

    AGENCY_DENIAL_ZONE = "denial"
    # Creates areas where specific actions are forbidden
    # Controls behavior through environmental rules

    SELF_AGENCY_LOCK = "self_lock"
    # Caster voluntarily locks their own actions
    # Trades flexibility for guaranteed effect

    AGENCY_OVERRIDE = "override"
    # Temporarily breaks standard action rules
    # Enables effects that ignore normal constraints


class ResourceControl(str, Enum):
    NONE = "none"
    # Does not meaningfully affect resource states

    RESTORE = "restore"
    # Returns previously lost resources
    # Sustains presence and prolongs fights

    DRAIN = "drain"
    # Removes resources from enemies for advantage
    # Weakens opponents while empowering the user or team

    DENIAL = "denial"
    # Prevents access to resources or objectives
    # Wins by exclusion rather than gain

    RESET = "reset"
    # Reverts resources to an earlier or baseline state
    # Erases accumulated progress

    ACCELERATION = "acceleration"
    # Increases the rate at which resources are gained or reused
    # Enables faster scaling or repeated pressure

    TRANSFER = "transfer"
    # Moves resources between entities
    # Redistributes power without creating or destroying it

    ERASE = "erase"
    # Removes existing resources or constructs outright
    # Nullifies setups, shields, or persistent threats
