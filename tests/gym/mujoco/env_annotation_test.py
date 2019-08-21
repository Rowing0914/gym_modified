import gym

ENVS = [
    # 'Reacher-v2',
    # 'Pusher-v2',
    # 'Thrower-v2',
    # 'Striker-v2',
    # 'InvertedPendulum-v2',
    # 'InvertedDoublePendulum-v2',
    # 'HalfCheetah-v2',
    # 'HalfCheetah-v3',
    # 'Hopper-v2',
    # 'Hopper-v3',
    # 'Swimmer-v2',
    # 'Swimmer-v3',
    # 'Walker2d-v2',
    # 'Walker2d-v3',
    'Ant-v2',
    # 'Ant-v3',
    # 'Humanoid-v2',
    # 'Humanoid-v3',
    # 'HumanoidStandup-v2'
]

for env_name in ENVS:
    env = gym.make(env_name)
    env.reset()
    print(env_name, env.action_space.shape[0])

    for i in range(1000):
        env.render(annotation_flg=True)
        action = env.action_space.sample()
        env.step(action)
