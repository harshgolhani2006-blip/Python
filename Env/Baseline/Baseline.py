from env import EmailEnv
from tasks import easy_task, medium_task, hard_task

env = EmailEnv()

print("Easy Score:", easy_task(env))
print("Medium Score:", medium_task(env))
print("Hard Score:", hard_task(env))