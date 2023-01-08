#

def decimalToBinary(n):
    return "{0:b}".format(int(n))

def binToPowerOfTwo(number):

    binNum = decimalToBinary(number)

    bin_str = str(binNum)
    bin_len = len(bin_str)
    print(f"### Binform: {bin_str}")
    return_list=[]

    for index,ele in enumerate(bin_str):

        if int(ele):
            tmp = pow(2,(bin_len-index-1))
            return_list.append(tmp)
    print(f"#### Powers of to for given number: {return_list}")

 


    return return_list



def simplyMod(base,exp,N,pow_list,pow_dict):

    power_string = "*".join([f"{base}^{pow}" for pow in pow_list])
    
    power_sum = "+".join([str(ele) for ele in pow_list])
    power_super_script = f"{base}^({power_sum})"

    # print(f"### Power Super Script: {power_super_script}")

    # print(f"### Power List: ({power_string}) mod ({N})")

    power_string_with_mod = "*".join([f"({base}^{pow} mod {N})" for pow in pow_list])

    # print(f"### Power List with Mod: ({power_string_with_mod}) mod ({N})")

    first_list = [pow_dict[ele] for ele in pow_list]

    mod_list = "*".join([str(ele) for ele in first_list])


    # print(f"### First Mod: ({mod_list}) mod {N}")


    # while True:

    tmp_list = first_list

    while len(tmp_list)>1:
        tmp_return_list = []

        tmp_str_list = "*".join([f"({str(ele)})" for ele in tmp_list])
        # print(f"### List with Mod: ({tmp_str_list}) mod {N}")
        print(f"({tmp_str_list}) mod {N}")

        tmp_str_list = "*".join([f"({str(ele)} mod {N})" for ele in tmp_list])
        # print(f"### List with each Mod: ({tmp_str_list}) mod {N}")
        print(f"({tmp_str_list}) mod {N}")

        

        for index,ele in enumerate(tmp_list):

            tmp_list[index] = (tmp_list[index]%N)
        tmp_str_list = "*".join([str(ele) for ele in tmp_list])
        # print(f"### List with Mod after: ({tmp_str_list}) mod {N}")
        print(f"({tmp_str_list}) mod {N}")



        list_len = 0

        while list_len+1<=len(tmp_list)-1:

            first_ele = tmp_list[list_len]
            second_ele = tmp_list[list_len+1]

            mul_ele = first_ele*second_ele

            tmp_return_list.append(mul_ele)

            list_len+=2
        # print(f"#### List len: {list_len} and tmp_list len: {len(tmp_list)}")

        if (len(tmp_list)-list_len)==1:
            tmp_return_list.append(tmp_list[-1])
            # print(f"### END {tmp_return_list}")
            # break
        

        # print(f"#### Iterate List: {tmp_return_list}")

        tmp_list = tmp_return_list

    final = (tmp_list[0])%N

    print(f"###### Final Mod: {final}")



def modexp(base,exp,N):

    pow_in2_list = binToPowerOfTwo(exp)


    high_pow = pow_in2_list[0]

    mod_index = {}

    index = 1
    remainder=0

    while index <= high_pow:

        if index ==1:
            remainder = base
            mod_index[1]=base
            print(f"{base}^{index} mod {N} = {base}")
            index*=2
            continue

        tmp = pow(base,index,N)

        mod_index[index] = tmp

        print(f"{base}^{index} mod {N} = ({remainder}*{remainder}) mod {N} = {tmp}")
        remainder=tmp

        index*=2

    # print(f"#### final mod table: {mod_index}")

    simplyMod(base,exp,N,pow_in2_list,mod_index)
    

modexp(698056,584939,988027)

# modexp(550230,584939,988027)