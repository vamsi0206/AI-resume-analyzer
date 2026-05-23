from Question import Question

question_prompts = [
    "what color are apples?\n(a) red\n(b) green\n(c) yellow\n(d) all of the above\n\n",
    "what color are bananas?\n(a) red\n(b) green\n(c) yellow\n(d) all of the above\n\n",
    "what color are oranges?\n(a) red\n(b) green\n(c) yellow\n(d) all of the above\n\n"

]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "d"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            print("you got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)