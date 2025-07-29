def recommend_career(interests, skills, mapping_df):
    recommendations = []
    for _, row in mapping_df.iterrows():
        int_match = any(i in row['interests'].split(';') for i in interests)
        skill_match = any(s in row['skills'].split(';') for s in skills)
        if int_match and skill_match:
            recommendations.append({
                "career": row["career"],
                "step1": row["step1"],
                "step2": row["step2"],
                "step3": row["step3"]
            })
    return recommendations
