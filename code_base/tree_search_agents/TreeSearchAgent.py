from abc import ABC, abstractmethod
from typing import List

from Environment import Environment


class TreeSearchAgent(ABC):
    @abstractmethod
    def run(self, env: Environment) -> tuple[List[int], float, list]:

        pass

    def play(self, env: Environment, actions: List[int]) -> float:
      
      

        env.reset()
        total_score = 0

        for action in actions:
            _, score, done = env.move(action)

            total_score += score

            if done:
                break

        return total_score

    @property
    @abstractmethod
    def name(self) -> str:
        pass
