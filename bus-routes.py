# -*- coding: utf-8 -*-
from collections import defaultdict


class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0

        stop_bus_map = defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                stop_bus_map.get(stop).add(bus)

        bfs = [(S, 0)]
        # The set seen record all stops visted and we won't check a stop for twice
        seen = set([S])
        for stop, bus in bfs:
            if stop == T:
                return bus
            for route_i in stop_bus_map[stop]:
                for next_stop in routes[route_i]:
                    if next_stop not in seen:
                        bfs.append((next_stop, bus + 1))
                        seen.add(next_stop)
                routes[route_i] = []
        return -1
