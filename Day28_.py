#https://leetcode.com/problems/students-and-examinations/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
def students_and_examinations(
    students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame
) -> pd.DataFrame:
    return (
        students.merge(subjects, how="cross")
        .merge(
            examinations[["student_id", "subject_name"]].value_counts().reset_index(),
            how="left",
        )
        .fillna(0)
        .sort_values(by=["student_id", "subject_name"])
        .rename(columns={"count": "attended_exams"})
        if not examinations.empty
        else pd.DataFrame(
            columns=["student_id", "student_name", "subject_name", "attended_exams"]
        )
    )
