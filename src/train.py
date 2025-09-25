class _Car:
    __slots__ = ("id", "prev", "next")

    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None


class Train:
    def __init__(self):
        self.head = None
        self.tail = None

    def attach_front(self, car_id):
        car = _Car(car_id)
        if not self.head:
            self.head = self.tail = car
        else:
            car.next = self.head
            self.head.prev = car
            self.head = car

    def attach_back(self, car_id):
        car = _Car(car_id)
        if not self.tail:
            self.head = self.tail = car
        else:
            self.tail.next = car
            car.prev = self.tail
            self.tail = car

    def detach_front(self):
        if not self.head:
            return None
        removed_id = self.head.id
        next_car = self.head.next
        if next_car:
            next_car.prev = None
        else:
            self.tail = None
        self.head = next_car
        return removed_id

    def detach_back(self):
        if not self.tail:
            return None
        removed_id = self.tail.id
        prev_car = self.tail.prev
        if prev_car:
            prev_car.next = None
        else:
            self.head = None
        self.tail = prev_car
        return removed_id

    def detach(self, car_id):
        car = self.head
        while car:
            if car.id == car_id:
                prev_car = car.prev
                next_car = car.next
                if prev_car:
                    prev_car.next = next_car
                else:
                    self.head = next_car
                if next_car:
                    next_car.prev = prev_car
                else:
                    self.tail = prev_car
                return True  # changed to True
            car = car.next
        return False  # not found

    def to_list(self):
        result = []
        car = self.head
        while car:
            result.append(car.id)
            car = car.next
        return result
