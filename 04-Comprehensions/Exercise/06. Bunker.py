if __name__ == "__main__":
    categories_string  = input().split(', ')
    categories = [{'category': food_category, 'foods': []} for food_category in categories_string]
    total_qty = 0
    total_qlty= 0
    N = int(input())
    for i in range(0,N):
        input_command = input().split(' - ')
        for category in categories:
            if category['category'] == input_command[0]:
                category['foods'].append(input_command[1])
                qty, qlty = input_command[2].split(";")
                total_qty += int(qty.split(":")[1])
                total_qlty += int(qlty.split(":")[1])
    print(f'Count of items: {total_qty}\nAverage quality: {total_qlty/len(categories_string):.2f}')
    print("\n".join([f"{x['category']} -> {', '.join(x['foods'])}" for x in categories]))


