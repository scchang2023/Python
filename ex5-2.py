# 用下列的格式印出每一個問題以及它的答案：
# Q:問題
# A:答案
questions=[
    "We don't server strings around here. Are you a string",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]
answers=[
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]
print(type(questions))
q_a = ((0, 1),(1, 2),(2, 0))
print(type(q_a))
for q, a in q_a:
    print("Q:", q, questions[q])
    print("A:", a, answers[a])
    print()