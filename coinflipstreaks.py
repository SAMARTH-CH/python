import random
print('samarth \n 1AY24AI097')
def flip_coin_streaks(num_flips):
    streak = 1
    last_flip = random.choice(['Heads', 'Tails'])
    print(f"Flip 1: {last_flip}")

    for i in range(2, num_flips + 1):
        current_flip = random.choice(['Heads', 'Tails'])
        print(f"Flip {i}: {current_flip}")

        if current_flip == last_flip:
            streak += 1
        else:
            print(f"--> Streak of {streak} {last_flip} ended")
            streak = 1  
        last_flip = current_flip
    print(f"Final streak: {streak} {last_flip}")
flip_coin_streaks(20)
