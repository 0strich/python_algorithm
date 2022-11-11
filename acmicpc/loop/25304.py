def calculate(value):
    return value[0] * value[1]

def receipt(total, receipt_list):
    calculate_value = sum([calculate(value) for value in receipt_list])
    return 'Yes' if total == calculate_value else 'No'
    
if __name__ == "__main__":
    total = int(input())
    receipt_list = []
  
    for _ in range(int(input())):
        money, num = map(int, input().split())
        receipt_list.append((money, num))
        
    print(receipt(total, receipt_list))