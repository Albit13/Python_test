test_design_writers = [1, 3, 5]
scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]

all_testers = sorted(list(set(test_design_writers + scripters + reviewers)))
script_only_testers = sorted(list(set(scripters) - set(test_design_writers) - set(reviewers)))
working_testers = sorted(list(set(all_testers) - set(out_of_office_today)))
script_and_review_testers = sorted(list(set(scripters) & set(reviewers) & set(working_testers)))

print("All testers: ", all_testers)
print("Script only testers: ", script_only_testers)
print("Working testers: ", working_testers)
print("Script and review testers: ", script_and_review_testers)
