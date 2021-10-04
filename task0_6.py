def maximum(*args):
    print("Maximum is ", end = '')
    if args[1] <= args[0] >= args[2]:
        print(args[0])
    elif args[0] <= args[1] >= args[2]:
        print(args[1])
    elif args[0] <= args[2] >= args[1]:
        print(args[2])
   
maximum()