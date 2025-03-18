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


class Leaderboard:
    """A leaderboard of speedrunning record times.

    Each entry has a time in seconds and a runner name.
    Runners may submit multiple runs.
    The leaderboard is ranked fastest run first.
    Ties receive the same rank as each other, so for example if runners submit
    the times 10, 20, 20, and 30, they will have the ranks 1, 2, 2, and 4.
    """

    def __init__(self, runs=[]):
        self.runs = runs

    def get_runs(self): #using insertion sort
        for i in range(1, len(self.runs)):
            #if time is less or equal the do comparison to decide if the element need to be insert first
            while i >= 1 and self.runs[i][0] <= self.runs[i-1][0]:
                #switch if time is smaller
                if self.runs[i][0] < self.runs[i-1][0]:
                    self.runs[i], self.runs[i-1] = self.runs[i-1], self.runs[i]
                #switch if time is equal but name come first
                elif self.runs[i][1] < self.runs[i-1][1]:
                    self.runs[i], self.runs[i-1] = self.runs[i-1], self.runs[i]
                i -= 1 #keep switching unit find no smaller element or i reached 1
        return self.runs
    
    def submit_run(self, time, name):
        self.runs.append((time, name))
        """Adds the given run to the leaderboard

        Args:
            time: The run time in seconds.
            name: The runner's name.
        """

    def get_rank_time(self, rank):
        rank_count = 1 #starting at rank 1
        i = 1
        #sort the list before assigning rank
        self.get_runs()
        rank_value = self.runs[i-1][0] #assign the first value to a varible

        while rank_count < rank and i < len(self.runs):
            rank_value = self.runs[i][0] #assign the next value
            if rank_value != self.runs[i-1][0]: #if the time larger than time before it then move up a rank
                rank_count += 1
            i += 1
        return rank_value

    def get_possible_rank(self, time): #Note: use binary search for the next version
        #sort the list before matching time with ranks
        self.get_runs()
        last_rank_time = self.runs[-1][0]
        posible_rank = 1

        if time <= last_rank_time: #if the arg time is smaller than the time ranked last then start comparing
            while self.get_rank_time(posible_rank) < time:
                posible_rank += 1
            return posible_rank
        else: #if its greater then add 1 to the last ranked
            return self.get_possible_rank(last_rank_time) + 1

    def count_time(self, time):

        self.get_runs()
        count = 1

        index = binary_search(time, self.runs)

        if index != -1:
            upper_count = index
            lower_count = index
            while upper_count < len(self.runs) - 1 and self.runs[upper_count][0] == self.runs[upper_count + 1][0]:
                count += 1
                upper_count += 1
            while lower_count > 0 and self.runs[lower_count][0] == self.runs[lower_count - 1][0]:
                count += 1
                lower_count -= 1
            return count
        else:
            return 0


list = Leaderboard([(10, 'Alex'), (30, 'Bob'), (30, 'Mike'), (30, 'Jess')])
list.submit_run(16, 'Josh')
list.submit_run(16, 'aohnny')  
print(list.get_runs())
print(list.count_time(30))
