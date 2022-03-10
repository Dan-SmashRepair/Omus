import numpy as np

from rlgym.utils import RewardFunction
from rlgym.utils.gamestates import GameState, PlayerData


class FiftyBotReward(RewardFunction):
    def __init__(self):
        super().__init__()

    def reset(self, initial_state: GameState):
        pass

    def get_reward(self, player: PlayerData, current_state: GameState, previous_action: np.ndarray) -> float:
        for player2 in current_state.players:
            if player2.team_num != player.team_num:
                if player2.ball_touched and np.linalg.norm(current_state.ball.position - np.array([0, 0, 97])) > 1200:
                    return -100
        if player.ball_touched and np.linalg.norm(current_state.ball.position - np.array([0, 0, 97])) > 1200:
            return 100
        return 0