import cmd

class MyCmd(cmd.Cmd):
        intro = "Welcome to my cmd, type help for more information.\n"
        prompt = "(mycmd)> "

        def do_greet(self, args):
                """Greets the user"""
                print("Hey there, How may I help you ? \n")
        def do_sum(self, args):
                """Sums two numbers"""
                try:
                        num1, num2 = map(float, args.split())
                        result = num1 + num2
                        print(f"The sum is {result}")
                except ValueError:
                        print("Invalid Integer. Usage: sum <num1> <num2>")
        def do_multiply(self, args):
                """Multiplies two numbers"""
                try:
                        num1, num2 = map(float, args.split())
                        result = num1 * num2
                        print(f"The product is {result}")
                except ValueError:
                        print("Invalid input. Usage multiply <num1> <num2>")
        def do_exit(self, args):
                """Exits mycmd"""
                return True

if __name__ == "__main__":
        MyCmd().cmdloop()
