class Bird:
    def intro(self):
        print("There are many types of bird.")

    def fly(self):
        print("Most of the birds can fly and some cannot.")


class Pigeon(Bird):
    def fly(self):
        print("Pigeon can fly.")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich cannot fly.")




obj_bird=Bird()
obj_bird.intro()
obj_bird.fly()

obj_p=Pigeon()
obj_p.fly()


obj_o=Ostrich()
obj_o.fly()
obj_o.intro()
