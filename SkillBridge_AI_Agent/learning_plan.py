def generate_learning_plan(skill_gaps):
    roadmap = {}
    for i, skill in enumerate(skill_gaps):
        roadmap[f"Week {i+1}"] = f"Learn {skill} fundamentals and build mini projects. Estimated Time: 6-8 hours."
    return roadmap