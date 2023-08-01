# This file is for strategy

from util.objects import *
from util.routines import *
from util.tools import *

class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        
        if self.kickoff_flag:
            self.set_intent(kickoff())
            self.set_intent(atba())
            return
        
        available_boosts = [boost for boost in self.boosts if boost.large]
        closest_boost = None
        closest_distance = 10000
        for boost in available_boosts:
            distance = (self.me.location - boost.location).magnitude()
            if closest_boost is None or distance < closest_distance:
                closest_boost = boost
                closest_distance = distance 
                return
                
        if self.me.boost < 90:
            available_large_boosts = [boost for boost in self.boosts if boost.large and boost.active]
            if len(available_large_boosts) is True:
                self.set_intent(goto(available_large_boosts[0].location))
            return
        
        if self.intent is not None:
            return
        d1 = abs(self.ball.location.y - self.foe_goal.location.y)
        d2 = abs(self.me.location.y - self.foe_goal.location.y)
        if d1 > d2:
            self.set_intent(goto(self.friend_goal.location))
            self.set_intent(short_shot(self.ball.location))
            return
        
        if d1 < d2:
            self.set_intent(short_shot(self.ball.location))
            return
            
        if self.set_intent is None:
            self.set_intent(short_shot(self.ball.location))
            self.set_intent(recovery(self.ball.location))
            return