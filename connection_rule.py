

class ConnectionRule:

    def __init__(self, simulator, connector, ):
        self.S = simulator
        self.C = connector
        #self.attrs = {}

    def update(self):
        """ Update values with which connections objects will be initialized """
        pass
    def should_connect(self, i, j):
        """ Return true if elements should be connected, else false. """
        # TODO: consider using lazyarrays
        # should you pass unit objects or indices? note that they're not
        # actually units but collections of units...
        # alternately this could return a weight (or a dict) - just 0 if
        # shouldn't connect or something
        pass

    def make_connections(self, pre_pop_tags, post_pop_tags, 
                         pre_pop=None, post_pop=None):

        
        

        # should pre and post be sets of uids or sets of tags?
        # can do lots of interesting things with sets of uids using chains
        # of filter commands...
        # why not both?
        # if change this, should probably change connector too...


        # so need to filter things with tags (unless pops given)
        # then need to...append numbers to pop tags? so pop tags have to be
        # given?


        # use iterator instead?
        # should you force users to only connect things as they are made?
        # so couldn't connect pre-existing stuff...
        # this would sorta suck
        # ALSO, can't just increment and append to tags. What if an element
        # of the population was deleted? What if the user selects a non-
        # continuous subset of the population?

        # Then I guess you need the population to just adhere to the rule
        # "has tag# in tags, and objects with same # in tag# are part of the
        # same group". Then can segment easily that way.
        keep_going = True
        while keep_going:
            pass
            # set keep_going



    def get_pop(self, tag, subset=None):
        # allow ranges? so only specific sub-population selected?
        # Note: elements must have both 'tag' and 'tag*' as tags, 
        # where 'tag*' places them in a group

        # get all candidates
        population = self.S.filter(tag)
        # partition candidates
        groups = []
        while population: # continue until empty?
            # should check to verify subpop changes each step, else err?
            n = population.pop()
            # get n's tags
            ntags = self.S.G.nodes[n].tags
            # get all potential tag* matches
            matches = [t for t in ntags if tag in t[:len(tag)] and t != tag]
            # verify unique match
            if len(matches) > 1:
                raise Exception('Too many matches in get_pop')
            # if so, get all units in same group
            group = {n} | self.S.filter_units(matches[0], subset=population)
            # remove them all from population and append to groups
            population -= group
            groups.append(group)

        # TODO: I feel like this could be  much cleaner
        return groups

