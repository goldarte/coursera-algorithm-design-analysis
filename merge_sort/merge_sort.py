def merge_step(left_half, right_half):
    n_left = len(left_half)
    n_right = len(right_half)
    if n_left > 1:
        left_half = merge_step(left_half[0:int(n_left/2)], left_half[int(n_left/2):n_left])
    if n_right > 1:
        right_half = merge_step(right_half[0:int(n_right/2)], right_half[int(n_right/2):n_right])
    output = []
    n = n_left + n_right
    i = j = 0
    for k in range(n):
        if i >= n_left:
            output.append(right_half[j])
            j+=1
        elif j >= n_right:
            output.append(left_half[i])
            i+=1
        elif left_half[i] <= right_half[j]:
            output.append(left_half[i])
            i+=1
        else:
            output.append(right_half[j])
            j+=1
    return output

def merge_sort(input_array):
    n = len(input_array)
    return merge_step(input_array[0:int(n/2)], input_array[int(n/2):n])
        

print (merge_sort([4,2,6,8,3,5,1,2,5]))

