class Solution:
    def average(self, salary: List[int]) -> float:

        minimum = min(salary)
        maximum = max(salary)
        total_salary = 0
        length = 0
        
        for i in salary:
            
            if i != minimum and i != maximum:
                total_salary += i
                length += 1
            
        return (total_salary / length)

        