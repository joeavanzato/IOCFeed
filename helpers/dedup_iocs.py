

def start(file_list):
    print("Deduplicating Feed Lists...")
    for file in file_list:
        print(f"Deduplicating: {file}")
        with open(file,'r', encoding='utf8') as f:
            new_file = "dedup_"+file
            print(f"Output: {new_file}")
            with open(new_file, 'w', encoding='utf8') as nf:
                temp_contents = {}
                for line in f:
                    if line.startswith("#"):
                        pass
                        #nf.writelines(line)
                    else:
                        data = line.split(">>>")
                        if data[0] in temp_contents:
                            temp_contents[data[0]] = temp_contents.get(data[0])+";"+data[1].strip()
                        else:
                            temp_contents[data[0]] = data[1].strip()
                for k,v in temp_contents.items():
                    nf.writelines(k+">>>"+v+"\n")
