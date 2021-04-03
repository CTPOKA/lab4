import os
import multiprocessing as m
import random

def action(name,enemy,c1,c2):
    while(True):
        if (c1.value <= 0):
            break
        x = random.randrange(5)
        print(f"Процесс {{PID={os.getpid()}, PPID={os.getppid()}}}: У команды {name} пополнение. {name}: {c1.value} (\033[32m+{x}\033[0m) ► {c1.value + x} \n",end="")
        c1.value = c1.value + x
        x = random.randrange(10)
        if (c2.value <= x):
            print(f"Процесс {{PID={os.getpid()}, PPID={os.getppid()}}}: Команда {name} наносит последний удар! {enemy}: {c2.value} (\033[31m-{c2.value}\033[0m) ► 0 \n",end="")
            c2.value = -10
            break
        print(f"Процесс {{PID={os.getpid()}, PPID={os.getppid()}}}: Команда {name} атакует. {enemy}: {c2.value} (\033[31m-{x}\033[0m) ► {c2.value - x} \n",end="")
        c2.value = c2.value - x

def battle(name1,name2,count1,count2):
    c1 = m.Value('d', count1)
    c2 = m.Value('d', count2)
    print(f"Процесс {{PID={os.getpid()}, PPID={os.getppid()}}}: Число бойцов команды {name1}: {count1}. Число бойцов команды {name2}: {count2}")
    print(f"Процесс {{PID={os.getpid()}, PPID={os.getppid()}}}: ▄▀▄▀▄▀ Битва началась! ▄▀▄▀▄▀\n")
    proc1 = m.Process(target=action, args=(name1,name2,c1,c2))
    proc2 = m.Process(target=action, args=(name2,name1,c2,c1))
    proc1.start()
    proc2.start()
    proc1.join()
    proc2.join()
    return name1 if c2.value <= 0 else name2

if __name__ == '__main__':
    winer = battle("\033[31mRED\033[0m","\033[34mBLUE\033[0m",100,100)
    print(f"\nПроцесс {{PID={os.getpid()}, PPID={os.getppid()}}}: ▄▀▄▀▄▀ Команда {winer} победила! ▄▀▄▀▄▀\n")
