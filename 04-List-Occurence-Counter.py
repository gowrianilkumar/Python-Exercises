def find_duplicates(sample_list):
    from collections import Counter
    item_counts = Counter(sample_list)
    
   
    duplicates = [item for item, count in item_counts.items() if count > 1]
    
    return duplicates


sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
result = find_duplicates(sample_list)
print(result) 
