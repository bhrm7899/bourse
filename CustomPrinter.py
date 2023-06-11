from colorama import Style


class CustomPrinter:

    @staticmethod
    def print(text, color):
        print(f"{Style.NORMAL}{color}{text}{Style.RESET_ALL}", end="")

    @staticmethod
    def println(text, color):
        print(f"{Style.NORMAL}{color}{text}{Style.RESET_ALL}")
