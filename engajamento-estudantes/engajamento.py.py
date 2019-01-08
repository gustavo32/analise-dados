import unicodecsv as ucsv
from datetime import datetime
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def string_to_int(field):
    return int(float(field))


def string_to_float(field):
    return float(field)


def string_to_date(field):
    if field == "":
        return None
    else:
        return datetime.strptime(field, '%Y-%m-%d')


def string_to_boolean(field):
    return field == "True"


def parse_maybe_int(field):
    if field:
        return int(field)
    else:
        return None


def read_csv(arq):
    return pd.read_csv(arq)


def exclusive_students(dt):
    exclusive = set()
    if type(dt) == dict:
        res = dt["account_key"]
        for r in res:
            exclusive.add(r)
    else:
        for d in dt:
            exclusive.add(d["account_key"])
    return exclusive


def first_week(date_join, date_engagement):
    time_delta = date_engagement - date_join
    return time_delta.days < 7 and time_delta.days >= 0


def extract_feature_first_week(engagement_by_user, field):
    feature_by_account = {}

    for key, value in engagement_by_user.items():
        feature = 0
        for v in value:
            feature += v[field]
        feature_by_account[key] = feature

    return feature_by_account


def create_list_project(dt, account_engagement):
    feature_who = defaultdict(list)
    for p in dt:
        account_key = p["account_key"]
        if account_key in account_engagement:
            feature_who[account_key].append(p)
    return feature_who


def describe_data(field):
    print("Mean: ", np.mean(field))
    print("Standard Deviation: ", np.std(field))
    print("Max: ", np.max(field))
    print("Min: ", np.min(field))


d_eng = read_csv("daily_engagement.csv")
enrolls = read_csv("enrollments.csv")
proj_sub = read_csv("project_submissions.csv")

for e in enrolls:
    e['join_date'] = string_to_date(e['join_date'])
    e['cancel_date'] = string_to_date(e['cancel_date'])
    e['days_to_cancel'] = parse_maybe_int(e['days_to_cancel'])
    e['is_udacity'] = string_to_boolean(e['is_udacity'])
    e['is_canceled'] = string_to_boolean(e['is_canceled'])

for d in d_eng:
    d['lessons_completed'] = string_to_int(d['lessons_completed'])
    d['projects_completed'] = string_to_int(d['projects_completed'])
    d['num_courses_visited'] = string_to_int(d['num_courses_visited'])
    d['total_minutes_visited'] = string_to_float(d['total_minutes_visited'])
    d['utc_date'] = string_to_date(d['utc_date'])
    d["account_key"] = d["acct"]
    d["has_visited"] = 1
    del[d["acct"]]
    if d["total_minutes_visited"] == 0.0:
        d["has_visited"] = 0

for p in proj_sub:
    p["creation_date"] = string_to_date(p["creation_date"])
    p["completion_date"] = string_to_date(p["completion_date"])

unique_engagements_students = exclusive_students(d_eng)
unique_enrollment_students = exclusive_students(enrolls)
# Teste para verficar as anomalias de enrolls e engagement
udacity_test = set()
account_udacity_test = []
new_d_eng = []
new_enrolls = []
new_proj_sub = []
for e in enrolls:
    if e["is_udacity"]:
        udacity_test.add(e["account_key"])
        account_udacity_test = e
        continue
    new_enrolls.append(e)

for d in d_eng:
    if d["account_key"] not in udacity_test:
        new_d_eng.append(d)

for p in proj_sub:
    if p["account_key"] not in udacity_test:
        new_proj_sub.append(p)

# print("New Enrolls: ", len(new_enrolls))
# print("Old Enrolls: ", len(enrolls))
# print("New Engagement: ", len(new_d_eng))
# print("Old Engagement: ", len(d_eng))
# print("New Project: ", len(new_proj_sub))
# print("Old Project: ", len(proj_sub))

paid_enrolls = {}
for e in new_enrolls:
    if e["days_to_cancel"] == None or e["days_to_cancel"] > 7:
        account_key = e["account_key"]
        enroll_date = e["join_date"]
        if account_key not in paid_enrolls or enroll_date > paid_enrolls[account_key]:
            paid_enrolls[account_key] = enroll_date

paid_engagement_in_first_week = []
account_engagement = []
for n in new_d_eng:
    n_acc_key = n["account_key"]
    if n_acc_key in paid_enrolls and first_week(paid_enrolls[n_acc_key], n["utc_date"]):
        account_engagement.append(n_acc_key)
        paid_engagement_in_first_week.append(n)

paid_submissions = []
for p in new_proj_sub:
    if p["account_key"] in paid_enrolls:
        paid_submissions.append(p)

paid_submission_in_first_week = []
for n in paid_engagement_in_first_week:
    if n["account_key"] in account_engagement:
        paid_submission_in_first_week.append(n)
# print(len(paid_engagement_in_first_week))

engagement_by_user = defaultdict(list)

for d in paid_engagement_in_first_week:
    acc = d["account_key"]
    engagement_by_user[acc].append(d)

total_minutes_by_account = extract_feature_first_week(
    engagement_by_user, "total_minutes_visited")

total_lessons_by_account = extract_feature_first_week(
    engagement_by_user, "lessons_completed")

total_days_by_account = extract_feature_first_week(
    engagement_by_user, "has_visited")

total_minutes = list(total_minutes_by_account.values())
total_lessons = list(total_lessons_by_account.values())
total_days = list(total_days_by_account.values())

# describe_data(total_days)

subway_project_lesson_keys = ['746169184', '3176718735']
pass_test = set()
for n in paid_submissions:
    if n["lesson_key"] in subway_project_lesson_keys:
        if n["assigned_rating"] == "PASSED" or n["assigned_rating"] == "DISTINCTION":
            pass_test.add(n["account_key"])


passing_engagement = []
non_passing_engagement = []
for p in paid_submission_in_first_week:
    if p["account_key"] in pass_test:
        passing_engagement.append(p)
    else:
        non_passing_engagement.append(p)

# print(len(passing_engagement))
# print(len(non_passing_engagement))

feature_by_who_pass = create_list_project(
    passing_engagement, account_engagement)

feature_by_who_dont_pass = create_list_project(
    non_passing_engagement, account_engagement)


lessons_by_who_passed = extract_feature_first_week(
    feature_by_who_pass, "lessons_completed")

describe_data(list(lessons_by_who_passed.values()))
plt.hist(list(lessons_by_who_passed.values()))
plt.show()

lessons_by_who_dont_passed = extract_feature_first_week(
    feature_by_who_dont_pass, "lessons_completed")

describe_data(list(lessons_by_who_dont_passed.values()))
plt.hist(list(lessons_by_who_dont_passed.values()))
plt.show()
# for key, value in total_minutes_by_account.items():
#     if value > 3000:
#         for d in engagement_by_user[key]:
#             print(d, "\n")

# for k in engagement_by_user[key]:
#     print(k["total_minutes_visited"], "\n")
