
test_cases = int(input())

for i in range(test_cases):
    setter_problem,problems_req_for_contest,days = map(int, list(input().split()))
    # setter_problem = int(line_2[0])
    # problems_req_for_contest = int(line_2[1])
    # days = int(line_2[2])
    total_problems_set_by_setter = 0

    line_3= list(input().split())
    for x in line_3:
        total_problems_set_by_setter += int(x)

    if(problems_req_for_contest > total_problems_set_by_setter):
        print(0)
        continue
    days_for_setter_problems = int(total_problems_set_by_setter/problems_req_for_contest)
    print(min(days_for_setter_problems,days))



