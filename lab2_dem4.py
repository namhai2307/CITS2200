# Name: Nam Tran
# Student Number: 24149594

def binary_search(element, list):
    n = len(list)
    start_position = 0
    end_position = n - 1
    
    while start_position <= end_position:
        middle_point = start_position + ((end_position - start_position) // 2)
        if element == list[middle_point][0]:
            return middle_point

        elif element > list[middle_point][0]:
            start_position = middle_point + 1

        else:
            end_position = middle_point - 1
    return -1

def merge(left, right):
    i = 0
    j = 0
    sorted_list = []
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            sorted_list.append(left[i])
            i += 1
        elif left[i][0] > right[j][0]:
            sorted_list.append(right[j])
            j += 1
        else:
            if left[i][1] <= right[j][1]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
            
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

def merge_sort(list):
    n = len(list)
    mid = n//2
    left_side = []
    right_side = []
    if n <= 1: #list with one element is already sorted
        return list
    
    left_side = list[:mid]
    right_side = list[mid:]
    
    return merge(merge_sort(left_side), merge_sort(right_side))
    

class Leaderboard:

    def __init__(self, runs=[]):
        self.runs = runs

    def get_runs(self): #using merge sort algorithm
        self.runs = merge_sort(self.runs)
        return self.runs
    
    def submit_run(self, time, name):
        self.runs.append((time, name))

    def get_rank_time(self, rank):
        #sort the list before assigning rank
        self.get_runs()
        list = self.runs

        if rank > self.get_possible_rank(self.runs[-1][0]):
            return self.runs[-1][0]

        n = len(list)
        start_position = 0
        end_position = n - 1

        #binary search for the time equivalant to the argument rank
        while start_position <= end_position:
            middle_point = start_position + ((end_position - start_position) // 2)
            if rank == self.get_possible_rank(list[middle_point][0]):
                return list[middle_point][0]

            elif rank > self.get_possible_rank(list[middle_point][0]):
                start_position = middle_point + 1

            else:
                end_position = middle_point - 1

        #if did not find any equivalent, return the time to get the higher rank closest to the argument rank
        return self.runs[start_position - 1][0]
        
    def get_possible_rank(self, time):
        #sort the array before matching time with ranks
        self.get_runs()
        last_rank_time = self.runs[-1][0] #slowest time stored for comparison
        first_rank_time = self.runs[0][0]

        #if the argument time greater than the slowest time in the array then return rank of the slowest + 1(no need to search)
        if time > last_rank_time:
            return self.get_possible_rank(last_rank_time) + 1
        #if the argument time smaller/equal than the top 1 time then return 1(no need to search)
        elif time <= first_rank_time:
            return 1
        
        n = len(self.runs)
        start_position = 0
        end_position = n - 1
            
        while start_position <= end_position:
            middle_point = start_position + ((end_position - start_position) // 2)
            if time == self.runs[middle_point][0]:
                while self.runs[middle_point][0] == self.runs[middle_point - 1][0] and middle_point > 1:
                    middle_point -= 1
                return middle_point + 1

            elif time > self.runs[middle_point][0]:
                start_position = middle_point + 1

            else:
                end_position = middle_point - 1
        return self.get_possible_rank(self.runs[start_position][0])

    def count_time(self, time):

        self.get_runs()
        count = 1
        #search for the argument time
        index = binary_search(time, self.runs)

        if index != -1: #if found, linear search left and right side for equal time
            upper_count = index
            lower_count = index
            while upper_count < len(self.runs) - 1 and self.runs[upper_count][0] == self.runs[upper_count + 1][0]:
                count += 1
                upper_count += 1 #count for right side
            while lower_count > 0 and self.runs[lower_count][0] == self.runs[lower_count - 1][0]:
                count += 1
                lower_count -= 1 #count for the left side
            return count
        else: # return 0 time if binary search not found
            return 0
