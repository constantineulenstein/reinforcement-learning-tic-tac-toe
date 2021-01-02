
from state import State
from player import Player
from humanPlayer import HumanPlayer


if __name__ == "__main__":
    # training
    training = str(input("Do you want to retrain the computer? Y/N?"))
    if training == 'Y' or training == 'y':
        p1 = Player("p1")
        p2 = Player("p2")

        st = State(p1, p2)
        print("training...")
        st.play(20000)
        #st.play()
        p1.savePolicy()

    # play with human
    p1 = Player("computer", exp_rate=0)
    p1.loadPolicy("policy_p1")

    p2 = HumanPlayer("Coco")

    st = State(p1, p2)
    st.play2()