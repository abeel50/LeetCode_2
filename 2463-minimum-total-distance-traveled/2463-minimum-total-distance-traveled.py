import functools
import math

class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        # Sort robots and factories to simplify distance calculation
        robot.sort()
        factory.sort()

        @functools.lru_cache(None)
        def dp(robot_idx: int, factory_idx: int, fixed_count: int) -> int:
            """
            Returns the minimum distance to fix robots from index `robot_idx` onwards
            using factories from index `factory_idx` onwards. `fixed_count` indicates
            the number of robots already fixed by the current factory.
            """
            # Base case: all robots are fixed
            if robot_idx == len(robot):
                return 0
            # Base case: no more factories available to use
            if factory_idx == len(factory):
                return math.inf
            
            # Option 1: Skip the current factory
            skip_current_factory = dp(robot_idx, factory_idx + 1, 0)
            
            # Option 2: Use the current factory if it can still fix more robots
            factory_position, factory_limit = factory[factory_idx]
            use_current_factory = (
                dp(robot_idx + 1, factory_idx, fixed_count + 1) + abs(robot[robot_idx] - factory_position)
                if fixed_count < factory_limit else math.inf
            )
            
            # Return the minimum distance of both options
            return min(skip_current_factory, use_current_factory)

        # Start the recursion from the first robot and first factory with no fixed robots
        return dp(0, 0, 0)
