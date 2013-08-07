

class ConnectionRule(object):

    def __init__(self, simulator, connector):
        self.S = simulator
        self.C = connector
        #self.attrs = {}

    def update(self):
        """ Update values with which connections objects will be initialized """
        pass

    def should_connect(self, pre_group, post_group):
        """ Return True if groups should be connected, else False. """
        # TODO: consider using lazyarrays
        # TODO: after modifying connector so can add parameters to each edge
        #       should somehow have this so it can modify parameters for 
        #       each time connector connects things?
        raise NotImplementedError()

    def make_connections(self, pre_pop, pre_group_tag, 
                         post_pop, post_group_tag):
        # NOTE: as stated in get_groups, must have 'tag', 'tag*' pattern
        for pre in self.get_groups(pre_group_tag, pop=pre_pop):
            for post in self.get_groups(post_group_tag, pop=post_pop):
                if self.should_connect(pre, post):
                    self.C.make_connection(pre, post)

    def make_individual_connections(self, pre_pop, post_pop):
        # without grouping, just apply connector to every pair
        # hacky?
        for pre in pre_pop:
            for post in post_pop:
                if self.should_connect({pre}, {post}):
                    self.C.make_connection({pre}, {post})

    def get_groups(self, tag, pop=None):
        # Note: elements must have both 'tag' and 'tag*' as tags, 
        # where 'tag*' places them in a specific group

        # get all candidates
        population = pop.copy() if pop!=None else self.S.filter(tag)
        # partition candidates
        groups = []
        while population: # continue until empty?
            # should check to verify subpop changes each step, else err?
            n = population.pop()
            # get n's tags
            ntags = self.S.G.node[n]['unit'].tags
            # get all potential tag* matches
            matches = [t for t in ntags if tag in t[:len(tag)] and t != tag]
            # verify unique match
            if len(matches) > 1:
                raise Exception('Too many matches in get_groups')
            # if so, get all units in same group
            group = {n} | self.S.filter_units(matches[0], subset=population)
            # remove them all from population and append to groups
            population -= group
            groups.append(group)

        # TODO: I feel like this could be  much cleaner
        return groups

