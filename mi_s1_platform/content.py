"""Educational content for the MI S1 platform."""

COURSES = [
    {
        "id": "intro_algo",
        "title_fr": "Introduction à l'algorithmique",
        "title_ar": "مقدمة في الخوارزميات",
        "definition_fr": "Un algorithme est une suite finie d'instructions permettant de résoudre un problème.",
        "definition_ar": "الخوارزمية هي سلسلة من التعليمات المنتهية لحل مشكلة معينة.",
        "example_fr": "Calculer la somme des N premiers entiers.",
        "example_ar": "حساب مجموع أول N من الأعداد الصحيحة.",
        "notation": "Lire N → somme = 0 → pour i de 1 à N: somme += i → afficher somme",
        "flowchart": "Début -> Lire N -> i=1,somme=0 -> [i<=N?] -> somme=somme+i -> i=i+1 -> retour test -> Afficher somme -> Fin",
    },
    {
        "id": "conditions",
        "title_fr": "Structures conditionnelles",
        "title_ar": "البُنى الشرطية",
        "definition_fr": "Permettent de choisir un traitement selon une condition vraie ou fausse.",
        "definition_ar": "تسمح باختيار مسار التنفيذ حسب صحة الشرط.",
        "example_fr": "Déterminer si un nombre est pair ou impair.",
        "example_ar": "تحديد ما إذا كان العدد زوجيًا أو فرديًا.",
        "notation": "Si n % 2 == 0 alors afficher 'pair' sinon afficher 'impair'",
        "flowchart": "Début -> Lire n -> [n%2==0?] -> Oui: afficher pair / Non: afficher impair -> Fin",
    },
]

PYTHON_TOPICS = [
    {
        "name_fr": "Variables et types",
        "name_ar": "المتغيرات والأنواع",
        "content_fr": "int, float, str, bool + affectation avec =",
        "content_ar": "الأنواع الأساسية في بايثون وكيفية الإسناد.",
        "python_example": "age = 18\nmoyenne = 14.5\nnom = 'Amina'\nest_admis = True",
    },
    {
        "name_fr": "Boucles et fonctions",
        "name_ar": "الحلقات والدوال",
        "content_fr": "for, while et définition de fonctions avec def.",
        "content_ar": "استخدام for و while وتعريف الدوال.",
        "python_example": "def somme_n(n):\n    total = 0\n    for i in range(1, n + 1):\n        total += i\n    return total",
    },
]

EXERCISES = [
    {
        "id": "sum_n",
        "level": "Débutant",
        "topic": "Boucles",
        "statement_fr": "Écrire une fonction somme_n(n) qui retourne la somme de 1 à n.",
        "statement_ar": "اكتب دالة somme_n(n) التي تُرجع مجموع الأعداد من 1 إلى n.",
        "function_name": "somme_n",
        "tests": [("somme_n(1)", 1), ("somme_n(5)", 15), ("somme_n(10)", 55)],
        "correction_steps_fr": [
            "Initialiser une variable total à 0.",
            "Parcourir les entiers de 1 à n.",
            "Ajouter chaque entier à total.",
            "Retourner total.",
        ],
    },
    {
        "id": "count_vowels",
        "level": "Intermédiaire",
        "topic": "Chaînes",
        "statement_fr": "Écrire une fonction compte_voyelles(texte) qui compte les voyelles.",
        "statement_ar": "اكتب دالة compte_voyelles(texte) لحساب عدد الحروف الصوتية.",
        "function_name": "compte_voyelles",
        "tests": [("compte_voyelles('algo')", 2), ("compte_voyelles('MI S1')", 1)],
        "correction_steps_fr": [
            "Définir l'ensemble des voyelles.",
            "Parcourir chaque caractère de la chaîne.",
            "Incrémenter un compteur si le caractère est une voyelle.",
            "Retourner le compteur.",
        ],
    },
]

CHALLENGES = [
    {
        "id": "fibonacci",
        "title_fr": "Défi Fibonacci",
        "title_ar": "تحدي فيبوناتشي",
        "description_fr": "Créer fib(n) qui retourne le n-ième terme de Fibonacci (fib(0)=0, fib(1)=1).",
        "description_ar": "أنشئ الدالة fib(n) التي تُرجع الحد n من متتالية فيبوناتشي.",
        "function_name": "fib",
        "tests": [("fib(0)", 0), ("fib(1)", 1), ("fib(7)", 13)],
        "difficulty": "Progressif",
    }
]

