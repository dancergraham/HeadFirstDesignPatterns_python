class GumballMachine:
    def __init__(self, number_gumballs) -> None:
        self.no_quarter_state = NoQuarterState(self)
        self.sold_out_state = SoldOutState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)
        self.count = number_gumballs
        if number_gumballs > 0:
            self.state = self.no_quarter_state
        else:
            self.state = self.sold_out_state

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def release_ball(self):
        print("A gumball comes rolling out the slot...")
        if self.count > 0:
            self.count -= 1

    def refill(self, count):
        self.count += count
        print(f"The gumball machine was just refilled; its new count is: {self.count}")
        self.state.refill()

    def set_state(self, state):
        self.state = state

    def __str__(self) -> str:
        result = []
        result.append("\nMighty Gumball, Inc.")
        result.append("\nJava-enabled Standing Gumball Model #2004")
        result.append(f"\nInventory: {self.count} gumball")
        if self.count != 1:
            result.append("s")

        result.append("\n")
        result.append(f"Machine is {self.state}\n")
        return "".join(result)


class State:
    def insert_quarter(self):
        raise NotImplementedError

    def eject_quarter(self):
        raise NotImplementedError

    def turn_crank(self):
        raise NotImplementedError

    def dispense(self):
        raise NotImplementedError

    def refill(self):
        raise NotImplementedError


class NoQuarterState(State):
    def __init__(self, gumball_machine: GumballMachine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You inserted a quarter")
        self.gumball_machine.set_state(self.gumball_machine.has_quarter_state)

    def eject_quarter(self):
        print("You haven't inserted a quarter")

    def turn_crank(self):
        print("You turned, but there's no quarter")

    def dispense(self):
        print("You need to pay first")

    def refill(self):
        raise NotImplementedError

    def __str__(self):
        return "waiting for quarter"


class SoldOutState(State):
    def __init__(self, gumball_machine: GumballMachine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can't insert a quarter, the machine is sold out")

    def eject_quarter(self):
        print("You can't eject, you haven't inserted a quarter yet")

    def turn_crank(self):
        print("You turned, but there are no gumballs")

    def dispense(self):
        print("No gumball dispensed")

    def refill(self):
        self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)

    def __str__(self):
        return "sold out"


class HasQuarterState(State):
    def __init__(self, gumball_machine: GumballMachine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can't insert another quarter")

    def eject_quarter(self):
        print("Quarter returned")
        self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)

    def turn_crank(self):
        print("You turned...")
        self.gumball_machine.set_state(self.gumball_machine.sold_state)

    def dispense(self):
        print("No gumball dispensed")

    def refill(self):
        raise NotImplementedError

    def __str__(self):
        return "waiting for turn of crank"


class SoldState(State):
    def __init__(self, gumball_machine: GumballMachine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("Please wait, we're already giving you a gumball")

    def eject_quarter(self):
        print("Sorry, you already turned the crank")

    def turn_crank(self):
        print("Turning twice doesn't get you another gumball!")

    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.count > 0:
            self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)
        else:
            self.gumball_machine.set_state(self.gumball_machine.sold_out_state)

    def refill(self):
        raise NotImplementedError

    def __str__(self):
        return "dispensing a gumball"


def gumball_machine_test_drive():
    gumball_machine = GumballMachine(2)
    print(gumball_machine)
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    gumball_machine.refill(5)
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)


if __name__ == "__main__":
    gumball_machine_test_drive()
