import gym
env = gym.make('CartPole-v0')
for i_episode in range(20):
    reward = env.reset()
    for t in range(100):
        #env.render()
        print(reward)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
