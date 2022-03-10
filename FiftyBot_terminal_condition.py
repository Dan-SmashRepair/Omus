import numpy as np

from rlgym.utils.terminal_conditions import TerminalCondition
from rlgym.utils.gamestates import GameState, PlayerData


class FiftyBotTerminalCondition(TerminalCondition):
    def __init__(self: int):
        super().__init__()

    def reset(self, initial_state: GameState):
        pass

    def is_terminal(self, current_state: GameState) -> bool:
        return np.linalg.norm(current_state.ball.position - np.array([0, 0, 97])) > 1200 and any(p.ball_touched for p in current_state.players)