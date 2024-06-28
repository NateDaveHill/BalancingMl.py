import random
import gym

try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Flatten
    from tensorflow.keras.optimizers import Adam

    from rl.agents import DQNAgent
    from rl.policy import BoltzmannQPolicy
    from rl.memory import SequentialMemory

    print("All imports were successful!")

except ImportError as e:
    print(f"ImportError: {e}")



env = gym.make("CartPole-v1", render_mode="human")

states = env.observation_space.shape[0]
actions = env.action_space.n

print(states)
print(actions)

# episodes = 10
# for episode in range(1, episodes+1):
#     state = env.reset()
#     done = False
#     score = 0

#     while not done:
#         action = random.choice([0, 1])
#         _, reward, done, _ = env.step(action)
#         score += reward
#         env.render()


#     print(f"Episode {episode}, Score: {score}")

# env.close