# This file is for strategy

from util.objects import *
from util.routines import *
from util.tools import *

class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        # if self.kickoff_flag:
        #     self.set_intent(kickoff())
        #     return
        available_boosts = [boost for boost in self.boosts if boost.large]
        closest_boost = None
        closest_distance = 10000
        for boost in available_boosts:
            distance = (self.me.location - boost.location).magnitude()
            if closest_boost is None or distance < closest_distance:
                closest_boost = boost
                closest_distance = distance 
                return
        self.set_intent(goto_boost)

        # if self.intent is not None:
        #     return
        # d1 = abs(self.ball.location.y - self.foe_goal.location.y)
        # d2 = abs(self.me.location.y - self.foe_goal.location.y)
        # if d1 > d2:
        #     self.set_intent(goto(self.friend_goal.location))
        #     self.set_intent(short_shot(self.ball.location))
        #     return
        
        # if self.me.boost < 90:
        #     available_large_boosts = [boost for boost in self.boosts if boost.large and boost.active]
        #     if len(available_large_boosts) is True:
        #         self.set_intent(goto(available_large_boosts[0].location))
        #     return
        
        # if self.set_intent is None:
        #     targets = {
        #         'at_opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
        #         'away_from_our_net': (self.friend_goal.right_post, self.friend_goal.left_post)
        #     }
        #     hits = find_hits(self, targets)
        #     if len(hits['to_opponents_goal']) > 0:
        #         self.set_intent(hits['to_opponents_goal'][0])
        #         return
        #     if len(hits['away_from_our_net']) > 0:
        #         self.set_intent(hits['away_from_our_net'][0])
        #         return
        













        # if self.me.boost < 50:
        #     available_boosts = [boost for boost in self.boosts if boost.large]
        #     closest_boost = None
        #     closest_distance = 5000
        #     for boost in available_boosts:
        #         distance = (self.me.location - boost.location).magnitude()
        #         if closest_boost is None or distance < closest_distance:
        #             closest_boost = boost
        #             closest_distance = distance 
        #             return
        #     if closest_boost is not None:
        #         self.set_intent(goto(closest_boost.location))
        #         return

        #     if len(available_boosts) > 0:
        #         self.set_intent(goto(available_boosts[0].location))
        #         print('going for boost', available_boosts[0].index)
        #         return
            
        # if self.me.boost > 50:
        #     self.set_intent(short_shot(self.foe_goal.location))
        #     return

         
        # target_boost = self.get_closest_large_boost()
        # if target_boost < 85:
        #     self.set_intent(goto(target_boost.location))
        #     return
        
        # if self.intent is None:
        #     d1 = abs(self.ball.location.y - self.foe_goal.location.y)
        #     d2 = abs(self.me.location.y - self.foe_goal.location.y)
        #     In_Front_Ball = d1 > d2
        #     Targets = {}
        #     find_hits(self, Targets)
        #     if In_Front_Ball:
        #         self.set_intent(goto(self.friend_goal.location))
        #         return
        #     self.set_intent(short_shot(self.foe_goal.location))
        #     targets = {
        #         'to_opponents_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
        #         'away_from_our_net': (self.friend_goal.right_post, self.friend_goal.right_post)
        #     }
        #     hits = find_hits(self, targets)
        #     if len(hits['to_opponents_goal']) > 0:
        #         self.set_intent(hits['to_opponents_goal'][0])
        #         return
        #     if len(hits['away_from_our_net']) > 0:
        #         self.set_intent(hits['away_from_our_net'][0])
        #         return
        
        # # if self.time % 2 == 0:
        #         print(hits)
        #     self.set_intent(atba())
       
       
       
        #boost class
        
        # if self.me.boost > 50:
        #     self.set_intent(short_shot(self.for_goal.location))

        # available_boosts = [boost for boost in self.boosts if boost.large and boost.active ]
        
        # closest_boost = None
        # closest_distance = 1000
        # for boost in available_boosts:
        #     distance = (self.me.location - boost.location).magnitude()
        #     if closest_boost is None or distance < closest_distance:
        #         closest_boost = boost
        #         closest_distance = distance 
        # if closest_boost is not None:
        #     self.set_intent(goto(closest_boost.location))
        #     return

        # if len(available_boosts) > 0:
        #     self.set_intent(goto(available_boosts[0].location))
        #     print('going for boost', available_boosts[0].index)
        #     return 