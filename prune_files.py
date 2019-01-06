import json
import sys
import os

from shutil import copyfile

import pdb

# NOTE: Will change from project to project. This is HW2.
# EDIT_FILES = [
#     "main/java/datastructures/concrete/DoubleLinkedList.java",
#     "test/java/datastructures/TestDeleteFunctionality.java",
#     "test/java/datastructures/TestDeleteStress.java",
#     "main/java/datastructures/concrete/dictionaries/ArrayDictionary.java",
#     "main/java/calculator/ast/ExpressionManipulators.java"
# ]

# NOTE: Edit files for HW5.
# EDIT_FILES = [
#     "main/java/datastructures/concrete/ArrayHeap.java",
#     "main/java/misc/Searcher.java",
#     "test/java/datastructures/sorting/TestArrayHeapFunctionality.java",
#     "test/java/datastructures/sorting/TestSortingStress.java",
#     "test/java/datastructures/sorting/TestTopKSortFunctionality.java",
#     "main/java/search/analyzers/TfIdfAnalyzer.java",
#     "main/java/search/analyzers/PageRankAnalyzer.java"
# ]

# NOTE: Edit files for HW7.
EDIT_FILES = [
    "main/java/datastructures/concrete/ArrayDisjointSet.java",
    "main/java/misc/graphs/Graph.java",
    "main/java/mazes/generators/maze/KruskalMazeCarver.java"
]

def copy_files(submission_dir, out_dir, join_out):
    student_dirs = os.listdir(submission_dir)
    # Gotta prune out files. Only dirs.
    student_dirs = [d for d in student_dirs if os.path.isdir(os.path.join(submission_dir, d))]

    for cur_dir in student_dirs:
        full_dir = os.path.join(submission_dir, cur_dir)
        # Make the output dir.
        cur_copy_dir = os.path.join(out_dir, cur_dir)
        os.mkdir(cur_copy_dir)

        student_files = []

        for cur_edit_file in EDIT_FILES:
            cur_edit_path = os.path.join(full_dir, "src")
            cur_edit_path = os.path.join(cur_edit_path, cur_edit_file)

            # Copy this edit file over.
            edit_basename = os.path.basename(cur_edit_file)
            cur_copy_target = os.path.join(cur_copy_dir, edit_basename)
            copyfile(cur_edit_path, cur_copy_target)

            student_files.append(cur_copy_target)

        # NOTE: Moss takes the skeleton as a single file. So just join all files
        # into a single one.
        cur_join_file = cur_dir + "_join.java"
        cur_join_target = os.path.join(join_out, cur_join_file)

        # NOTE: Little hack so they all get joined in the same order. MOSS
        # shouldn't care, but hey!
        student_files.sort()
        cat_command = ["cat"] + student_files + [">"] + [cur_join_target]
        cat_command = " ".join(cat_command)
        os.system(cat_command)



if __name__ == '__main__':

    orig_repos = sys.argv[1]
    pruned_out_dir = sys.argv[2]
    joined_out_dir = sys.argv[3]

    copy_files(orig_repos, pruned_out_dir, joined_out_dir)
