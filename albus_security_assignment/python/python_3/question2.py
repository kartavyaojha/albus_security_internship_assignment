def search_pattern(file_name, pattern):
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
            matching_lines = [line.strip() for line in lines if pattern in line]
            return matching_lines
    except Exception as e:
        print(str(e))
        return []
    


file_path=input("enter the name of the file:")
pattern=input("enter the string pattern to be searched:")
matches=search_pattern(file_path,pattern)
print("Matches:")
for match in matches:
    print(match)