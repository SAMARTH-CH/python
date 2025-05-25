import random
print('samarth\n1AY24AI097')
class ZombieDiceBot:
    def __init__(self, name):
        self.name = name
        self.brains = 0
        self.shotguns = 0

    def should_continue(self):
        """Basic logic: keep going until 2 shotguns."""
        return self.shotguns < 2

    def take_turn(self, dice_cup):
        self.brains = 0
        self.shotguns = 0
        footsteps = []

        print(f"\n{self.name}'s turn begins.")

        while self.should_continue():
           
            dice_to_roll = footsteps
            while len(dice_to_roll) < 3:
                if not dice_cup:
                    print("Dice cup is empty!")
                    break
                dice_to_roll.append(dice_cup.pop())

            print(f"Rolling dice: {dice_to_roll}")
            new_footsteps = []

            for die in dice_to_roll:
                face = random.choice(['brain', 'shotgun', 'footsteps'])
                print(f"  Die shows: {face}")
                if face == 'brain':
                    self.brains += 1
                elif face == 'shotgun':
                    self.shotguns += 1
                else:
                    new_footsteps.append(die)

            footsteps = new_footsteps

            print(f"  Score so far: {self.brains} brains, {self.shotguns} shotguns")

            if self.shotguns >= 3:
                print(f"  {self.name} got shot 3 times and loses all brains!")
                self.brains = 0
                break

        print(f"{self.name}'s turn ends with {self.brains} brains.\n")
        return self.brains


def make_dice_cup():
    """Returns a randomized dice cup."""
  
    return random.sample(
        ['green']*6 + ['yellow']*4 + ['red']*3, 13
    )


if __name__ == "__main__":
    bot1 = ZombieDiceBot("Bot-A")
    bot2 = ZombieDiceBot("Bot-B")

    for round_num in range(1, 4):
        print(f"--- Round {round_num} ---")
        dice_cup = make_dice_cup()
        bot1.take_turn(dice_cup.copy())
        dice_cup = make_dice_cup()
        bot2.take_turn(dice_cup.copy())
