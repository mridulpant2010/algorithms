def find_paths(root,sum):
    all_paths = []
    find_paths_recursive(root,sum,[],all_paths)
    return all_paths


def find_paths_recursive(root,required_sum,current_path,all_paths):
    if root is None:
        return
    
    current_path.append(root.data)
    if root.left and root.right and root.data==required_sum:
        all_paths.append(current_path)
    else:
        find_paths_recursive(root.left,required_sum-root.data,current_path,all_paths)
        find_paths_recursive(root.right,required_sum-root.data,current_path,all_paths)
    del current_path[-1]

