import unittest


class CarTests(unittest.TestCase):
    make = 'make'
    model = 'model'
    fuel_consumption = 10
    fuel_capacity = 100

    def test_car_make_setter__when_None__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.make = None

        self.assertEqual('Make cannot be null or empty!', str(context.exception))

    def test_car_make_setter__when_empty__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.make = ""

        self.assertEqual('Make cannot be null or empty!', str(context.exception))

    def test_car_make_setter__when_correct__expect_to_make(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.make = "yeet"

        self.assertEqual("yeet", car.make)

    def test_car_model_setter__when_None__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.model = None

        self.assertEqual('Model cannot be null or empty!', str(context.exception))

    def test_car_model_setter__when_empty__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.model = ""

        self.assertEqual('Model cannot be null or empty!', str(context.exception))

    def test_car_model_setter__when_correct__expect_to_change_model(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.model = "yeet"

        self.assertEqual("yeet", car.model)

    def test_car_fuel_consumption__when_value_is_zero__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        value = 0
        with self.assertRaises(Exception) as context:
            car.fuel_consumption = value

        self.assertEqual('Fuel consumption cannot be zero or negative!', str(context.exception))

    def test_car_fuel_consumption__when_value_is_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        value = -6
        with self.assertRaises(Exception) as context:
            car.fuel_consumption = value

        self.assertEqual('Fuel consumption cannot be zero or negative!', str(context.exception))

    def test_car_fuel_consumption__when_value_is_correct__expect_to_change_fuel_consumption(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        value = 8
        car.fuel_consumption = value

        self.assertEqual(value, car.fuel_consumption)

    def test_car_fuel_capacity__when_value_is_zero__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        value = 0
        with self.assertRaises(Exception) as context:
            car.fuel_capacity = value

        self.assertEqual('Fuel capacity cannot be zero or negative!', str(context.exception))

    def test_car_fuel_capacity__when_value_is_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        value = -6
        with self.assertRaises(Exception) as context:
            car.fuel_capacity = value

        self.assertEqual('Fuel capacity cannot be zero or negative!', str(context.exception))

    def test_car_fuel_capacity__when_value_is_correct__expect_to_change_fuel_consumption(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        value = 8
        car.fuel_capacity = value

        self.assertEqual(value, car.fuel_capacity)

    def test_car_fuel_amount__when_value_is_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        value = -6
        with self.assertRaises(Exception) as context:
            car.fuel_amount = value

        self.assertEqual('Fuel amount cannot be negative!', str(context.exception))

    def test_car_fuel_amount__when_value_is_correct__expect_to_change_fuel_consumption(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        value = 8
        car.fuel_amount = value

        self.assertEqual(value, car.fuel_amount)

    def test_car_refuel__when_provided_fuel_is_negative_or_0__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.refuel(0)

    def test_car_refuel__when_provided_fuel_is_negative_or_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.refuel(-1)

    def test_car_refuel__when_provided_fuel_is_correct__expect_to_increase_fuel_amount_by_provided_fuel(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        fuel = 50
        car.refuel(fuel)
        self.assertEqual(fuel, car.fuel_amount)

    def test_car_refuel__when_provided_fuel_is_more_than_capacity__expect_to_increase_fuel_amount_to_fuel_capacity(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.refuel(self.fuel_capacity * 2)
        self.assertEqual(car.fuel_capacity, car.fuel_amount)

    def test_car_drive__when_value_is_less_than_fuel_amount__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        distance_test = 30
        car.fuel_amount = 2
        with self.assertRaises(Exception) as context:
            car.drive(distance_test)

        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))

    def test_car_drive__when_value_is_correct__expect_to_drive(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        distance_test = 10
        car.fuel_amount = 50
        left_fuel = 49
        car.drive(distance_test)

        self.assertEqual(float(left_fuel), car.fuel_amount)

if __name__ == '__main__':
    unittest.main()
