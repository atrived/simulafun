import numpy.random as random
from functools import reduce


def game_1(**kwargs):
    """
    reward: 6
    penalty: -1
    odds: 60/40
    """
    TRIAL_LEN = 1000

    reward = kwargs.pop("reward")
    reward_prob = kwargs.pop("reward_prob")
    penalty = kwargs.pop("penalty")
    penalty_prob = kwargs.pop("penalty_prob")

    sim_list = random.binomial(1, reward_prob, TRIAL_LEN)

    start_ = 1
    loss = []
    for i in sim_list:
        if i:
            start_ *= reward
        else:
            start_ = 1
            loss.append(start_)

    return start_ + sum(loss)

    # naive avg expectation
    # return sum([reward if x else penalty for x in sim_list])/len(sim_list)


print(f"game 1 {game_1(reward=2, reward_prob=1, penalty=-1, penalty_prob=0)}")


def game_2(**kwargs):
    """
    reward: 6
    penalty: -1
    odds: 60/40
    """
    TRIAL_LEN = 1000

    reward = kwargs.pop("reward")
    reward_prob = kwargs.pop("reward_prob")
    penalty = kwargs.pop("penalty")
    penalty_prob = kwargs.pop("penalty_prob")
    # save_ratio = kwargs.pop("save_ratio", None)

    sim_list = random.binomial(1, reward_prob, TRIAL_LEN)
    # print(sim_list)
    save_ratio = 0.2
    bank = 0
    start_ = 1
    loss = []
    for i in sim_list:

        if i:
            start_ *= reward
            # print(
            # f"winnig! put {save_ratio} in bank and {1-save_ratio} on our next play")
            bank = bank + (start_*save_ratio)
            start_ *= (1-save_ratio)
            # print("win", start_, bank)

        else:
            # print(bank)
            if start_ > bank:
                return -1  # "you iz broke"
            bank -= start_
            # print("loss", start_, bank)
            # loss.append(start_)

    return start_ + bank

    # naive avg expectation
    # return sum([reward if x else penalty for x in sim_list])/len(sim_list)


# for i in range(100)
# print(f"game 1 {game_(reward=2, reward_prob=1, penalty=-1, penalty_prob=0)}")
print(
    f"game 2 {game_2(reward=6, reward_prob=0.9, penalty=-1, penalty_prob=0.1)}")
# print("\n")

strategy = []
for i in range(10):
    game_1_reward = game_1(reward=2, reward_prob=1, penalty=-1, penalty_prob=0)
    game_2_reward = game_2(reward=6, reward_prob=0.9,
                           penalty=-1, penalty_prob=0.1)
    strategy.append(game_1_reward
                    > game_2_reward)
    # print(strategy)
print("st 1 better", strategy.count(True),
      "st 2 better", strategy.count(False))
