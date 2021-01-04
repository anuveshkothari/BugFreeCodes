
test_cases = int(input())
for test in range(test_cases):
    john_packs, jack_packs = map(int, list(input().split()))

    john_pack_list = list(input().split())
    jack_pack_list = list(input().split())
    john_pack_list = [int(x) for x in john_pack_list]
    jack_pack_list = [int(x) for x in jack_pack_list]
    john_pack_list.sort()
    jack_pack_list.sort()
    # print(jack_pack_list)
    john_total_votes = jack_total_votes =0

    for i in john_pack_list:
        john_total_votes += int(i)
    for i in jack_pack_list:
        jack_total_votes += int(i)

    # print(str(john_pack_list) + " : " + str(jack_pack_list) + " : " + str(john_total_votes) + " : " + str(jack_total_votes))

    num_of_iteration = min (john_packs, jack_packs)
    i = 0
    while i < num_of_iteration and john_total_votes <= jack_total_votes:
        john_total_votes += int(jack_pack_list[jack_packs-i-1]) - int(john_pack_list[i])
        jack_total_votes += int(john_pack_list[i]) - int(jack_pack_list[jack_packs-i-1])
        i+=1
        # print("john_total_votes:  " + str(john_total_votes) + ", jack_total_votes: " + str(jack_total_votes))
    if (john_total_votes > jack_total_votes):
        print(i)
    else:
        print("-1")