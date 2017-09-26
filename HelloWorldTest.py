import unittest
import HelloWorld

class HelloWorldTest(unittest.TestCase):

    def test_greeting(self):
        greet = HelloWorld.Howdy()
        greeting = greet.greeting("Foo")

        self.assertEqual(greeting, "Hello, Foo turdz")

    def test_vars(self):
        greet2 = HelloWorld.Howdy()
        greet2.turd = "fartz"
        greeting2 = greet2.greeting("Foo")
        greet = HelloWorld.Howdy()
        greeting = greet.greeting("Foo")

        self.assertEqual(greeting, "Hello, Foo turdz")
        self.assertEqual(greeting2, "Hello, Foo fartz")

    def test_bye(self):
        greet = HelloWorld.Howdy()
        greeting = greet.bye("Bar")

        self.assertEqual(greeting, "Adios, Baro")

    def test_is_a_shit(self):
        greet = HelloWorld.Howdy()

        self.assertTrue(greet.is_a_shit())

if __name__ == '__main__':
    unittest.main()

