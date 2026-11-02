"""Streamlit app for MI S1 Algorithmics learning."""

from __future__ import annotations

from pathlib import Path

import streamlit as st

from mi_s1_platform.content import CHALLENGES, COURSES, EXERCISES, PYTHON_TOPICS
from mi_s1_platform.execution import evaluate_function_submission, run_python_code
from mi_s1_platform.progress import completion_rate, load_progress, save_progress


st.set_page_config(page_title="Plateforme MI S1 - Algorithmique", layout="wide")

language = st.sidebar.selectbox("Langue / اللغة", ["Français", "العربية"], index=0)
theme = st.sidebar.selectbox("Mode", ["Clair", "Sombre"], index=0)

if theme == "Sombre":
    st.markdown(
        """
        <style>
        .stApp { background-color: #0f172a; color: #e2e8f0; }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.title("Plateforme éducative Algorithmique - MI S1")
st.caption("Apprentissage interactif de l'algorithmique et de Python (Français + explications عربية).")

progress_file = Path("data/student_progress.json")
progress = load_progress(progress_file)

section = st.sidebar.radio(
    "Sections",
    [
        "Cours",
        "Apprendre Python",
        "Exercices",
        "Éditeur Python",
        "Défis algorithmiques",
        "Tableau de bord",
    ],
)


if section == "Cours":
    st.header("Cours d'algorithmique")
    for lesson in COURSES:
        title = lesson["title_fr"] if language == "Français" else lesson["title_ar"]
        with st.expander(title):
            st.write("**Définition:**", lesson["definition_fr"])
            st.write("**Français:**", lesson["example_fr"])
            st.write("**العربية:**", lesson["definition_ar"], "-", lesson["example_ar"])
            st.code(lesson["notation"], language="text")
            st.write("**Flowchart (texte):**", lesson["flowchart"])
            if st.button(f"Marquer comme terminé: {lesson['id']}", key=f"lesson_{lesson['id']}"):
                if lesson["id"] not in progress["lessons"]:
                    progress["lessons"].append(lesson["id"])
                    save_progress(progress_file, progress)
                    st.success("Leçon enregistrée.")

elif section == "Apprendre Python":
    st.header("Python pour l'algorithmique")
    for topic in PYTHON_TOPICS:
        st.subheader(topic["name_fr"] if language == "Français" else topic["name_ar"])
        st.write(topic["content_fr"])
        st.write("**العربية:**", topic["content_ar"])
        st.code(topic["python_example"], language="python")

elif section == "Exercices":
    st.header("Exercices par niveau")
    level = st.selectbox("Niveau", sorted({exercise["level"] for exercise in EXERCISES}))
    for exercise in [item for item in EXERCISES if item["level"] == level]:
        st.subheader(f"{exercise['topic']} - {exercise['id']}")
        st.write(exercise["statement_fr"])
        st.write("**العربية:**", exercise["statement_ar"])
        user_code = st.text_area(f"Réponse Python ({exercise['id']})", height=180, key=f"code_{exercise['id']}")
        if st.button(f"Corriger {exercise['id']}", key=f"check_{exercise['id']}"):
            ok, message = evaluate_function_submission(user_code, exercise["tests"])
            st.info(message)
            st.write("**Correction détaillée:**")
            for index, step in enumerate(exercise["correction_steps_fr"], start=1):
                st.write(f"{index}. {step}")
            if ok and exercise["id"] not in progress["exercises"]:
                progress["exercises"].append(exercise["id"])
                save_progress(progress_file, progress)

elif section == "Éditeur Python":
    st.header("Éditeur Python interactif")
    default_snippet = "for i in range(1, 6):\n    print(i)"
    code = st.text_area("Écrire votre code Python", value=default_snippet, height=220)
    if st.button("Exécuter"):
        result = run_python_code(code)
        if result.ok:
            st.success("Exécution réussie")
            st.code(result.stdout or "(aucune sortie)")
        else:
            st.error("Erreur détectée")
            st.code(result.stderr)
            st.warning(result.explanation_fr)

elif section == "Défis algorithmiques":
    st.header("Défis progressifs")
    for challenge in CHALLENGES:
        st.subheader(challenge["title_fr"] if language == "Français" else challenge["title_ar"])
        st.write(challenge["description_fr"])
        st.write("**العربية:**", challenge["description_ar"])
        st.caption(f"Difficulté: {challenge['difficulty']}")
        challenge_code = st.text_area(f"Solution ({challenge['id']})", height=180, key=f"challenge_{challenge['id']}")
        if st.button(f"Valider {challenge['id']}", key=f"validate_{challenge['id']}"):
            ok, message = evaluate_function_submission(challenge_code, challenge["tests"])
            if ok:
                st.success(message)
                if challenge["id"] not in progress["challenges"]:
                    progress["challenges"].append(challenge["id"])
                    save_progress(progress_file, progress)
            else:
                st.error(message)

else:
    st.header("Tableau de bord étudiant")
    goals = st.text_area("Objectifs personnels", value=progress.get("goals", ""))
    if st.button("Enregistrer mes objectifs"):
        progress["goals"] = goals
        save_progress(progress_file, progress)
        st.success("Objectifs enregistrés.")

    st.metric("Leçons terminées", len(progress["lessons"]))
    st.metric("Exercices validés", len(progress["exercises"]))
    st.metric("Défis validés", len(progress["challenges"]))
    st.metric(
        "Progression globale (%)",
        f"{completion_rate(progress, len(COURSES), len(EXERCISES), len(CHALLENGES)):.1f}",
    )

