import argparse

parser = argparse.ArgumentParser()

# 입력받고자 하는 인자의 조건을 설정
# - or -- 가 없이 그냥 쓰면 python arhparse_test.py 1 2
# parser.add_argument('X',type=int,
#                     help='What is the first number?')
#
# parser.add_argument('Y',type=int,
#                     help='What is the second number?')


# python argparse_test.py --first-number 1 --second-number 2
# python argparse_test.py -f 1 -s 2

parser.add_argument('-f','--first-number',type=int,
                    help='What is the first number?')

parser.add_argument('-s','--second-number',type=int,
                    help='What is the second number?')

# 인자들을 파싱하여 args에 저장한다. 각 인자는 add_argument의 type에 지정된 형식으로 지정된다.

# vars : __dict__ attribute를 가짐
args = vars(parser.parse_args())
print(args)

X = args['first_number']
Y = args['second_number']

print("%d + %d = %d"  % (X, Y, X+Y))
