from cowsay import cowsay, list_cows, make_bubble, cowthink
import shlex
import cmd

class CowCmd(cmd.Cmd):
    prompt = "twocows> "

    def do_list_cows(self, args):
        """Вывод списка доступных коров."""

        print(list_cows())
    

    def do_make_bubble(self, args):
        """Оборачивает текст животного в виде пузырика."""

        print(make_bubble(args))

    def _print_side_by_side(self, text1, text2):
        """Вывод двух животных."""
        cow1_split = text1.split('\n')
        cow2_split = text2.split('\n')
        
        max_lenght_1 = max([len(i) for i in cow1_split])

        max_weight_1 = len(cow1_split)
        max_weight_2 = len(cow2_split)

        if max_weight_1 > max_weight_2:
            cow2_split = [" "] * (max_weight_1 - max_weight_2) + cow2_split
        else:
            cow1_split = [" "] * (max_weight_2 - max_weight_1) + cow1_split

        for i in range(max(max_weight_1, max_weight_2)):
            len_line = len(cow1_split[i])
            print(cow1_split[i] + ' ' * (max_lenght_1 - len_line), cow2_split[i])
    
    def do_cowsay(self, args):
        """Разбор параметров у животных."""

        args = shlex.split(args)
        message_1 = args[0]
        cow_1 = 'default'
        eyes_1 = 'oo'
        i = 1

        while args[i] != "reply":
            if i == 1:
                cow_1 = args[i]
            elif i == 2:
                eyes_1 = args[i][5:]
            i += 1
        i += 1

        j = i

        message_2 = args[i]
        cow_2 = 'default'
        eyes_2 = 'oo'

        while j < len(args):
            if j == i + 1:
                cow_2 = args[j]
            elif j == i + 2:
                eyes_2 = args[j][5:]
            j += 1

        CowCmd._print_side_by_side(self, cowsay(message_1, cow=cow_1, eyes=eyes_1), cowsay(message_2, cow=cow_2, eyes=eyes_2))

    def do_cowthink(sel, args):
        """Думающая корова"""
        args = shlex.split(args)
        message = args[0]
        print(cowthink(message))

    def do_EOF(self, arg):
        """конец"""
        return -1
    
if __name__ == '__main__':
    CowCmd().cmdloop()
