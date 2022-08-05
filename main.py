from game_data import data
import art
import random

def random_choise_from_data(data):

    random_sample = random.sample(data, 2)
    choise_1 = random_sample[0]
    choise_2 = random_sample[1]
    print(art.logo)
    print(f"campare A: {choise_1['name']}, a {choise_1['description']}, from {choise_1['country']}")
    print(art.vs)
    print(f"campare A: {choise_2['name']}, a {choise_2['description']}, from {choise_2['country']}")
    followers_a = choise_1['follower_count']
    followers_b = choise_2['follower_count'] 
    return (followers_a, followers_b)
#     print(random_sample)
#     return random_sample

def compare(two_samples,score):
    print(f"score is {score}")
    print(two_samples[0], two_samples[1])
    if two_samples[0] > two_samples[1]:
        higher = "A"
    elif two_samples[0] < two_samples[1]:
        higher = "B"
    else: 
        random_choise_from_data(data)
    choise = input("Type 'A' or 'B'")
    if choise == higher:
        score =1
        print(f" You win, your score is {score}")
        return (False, score)
    else:
        print("You lose, start again")
        return True
score= 0   
end_game = False
while end_game != True:
    two_samples = random_choise_from_data(data)
    end_game = compare(two_samples,score) 
    score += end_game[1]
    print(end_game)