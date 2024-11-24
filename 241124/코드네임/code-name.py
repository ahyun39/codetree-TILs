class Agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

agents = []

for _ in range(5):
    name, score = map(str, input().split())
    agents.append(Agent(name, score))

sort_agents = [[agent.codename, agent.score] for agent in agents]
sort_agents.sort(key=lambda x:x[1])
print(*sort_agents[0])