def easy_task(env):
    score = 0
    total = 3

    state = env.reset()

    for _ in range(total):
        email = state["email"]

        if "Server" in email:
            action = "urgent"
        elif "Discount" in email:
            action = "spam"
        else:
            action = "normal"

        state, reward, done, _ = env.step(action)
        if reward > 0:
            score += 1

    return score / total


def medium_task(env):
    score = 0
    total = 3

    state = env.reset()

    for _ in range(total):
        email = state["email"]

        if "down" in email:
            action = "urgent"
        elif "offer" in email:
            action = "spam"
        else:
            action = "normal"

        state, reward, done, _ = env.step(action)
        if reward > 0:
            score += 1

    return score / total


def hard_task(env):
    score = 0
    total = 3

    state = env.reset()

    for _ in range(total):
        email = state["email"]

        # harder logic
        action = random.choice(["urgent", "normal", "spam"])

        state, reward, done, _ = env.step(action)
        if reward > 0:
            score += 1

    return score / total