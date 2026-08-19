class Head:
    def __init__(self):
        self.brain = "thinking"


class Hand:
    def __init__(self):
        self.fingers = 5


class Arm:
    def __init__(self, hand):
        self.hand = hand


class Feet:
    def __init__(self):
        self.toes = 5


class Leg:
    def __init__(self, foot):
        self.foot = foot


class Torso:
    def __init__(self, head, left_arm, right_arm, left_leg, right_leg):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg


class Human:
    def __init__(self):


        self.head = Head()

        left_hand = Hand()
        right_hand = Hand()

        self.left_arm = Arm(left_hand)
        self.right_arm = Arm(right_hand)

        left_foot = Feet()
        right_foot = Feet()

        self.left_leg = Leg(left_foot)
        self.right_leg = Leg(right_foot)

        self.torso = Torso(
            self.head,
            self.left_arm,
            self.right_arm,
            self.left_leg,
            self.right_leg
        )


if __name__ == "__main__":

    person = Human()

    print("Brain:", person.head.brain)
    print("Left hand fingers:", person.left_arm.hand.fingers)
    print("Right foot toes:", person.right_leg.foot.toes)