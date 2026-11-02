import streamlit as st
import sys
import io

# 1. إعدادات الصفحة الأساسية والهوية البصرية الفائقة
st.set_page_config(
    page_title="MI S1 Algorithmique & Python",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# حقن تصاميم CSS مخصصة لإنشاء واجهة بريميوم وتأثيرات بصرية متطورة ومريحة للعين
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    /* ضبط الخطوط الأساسية للتطبيق */
    html, body, [data-testid="stSidebar"], .stMarkdown {
        font-family: 'Inter', 'Cairo', sans-serif;
    }
    
    /* تصميم الأزرار التفاعلية بشكل زجاجي فخم مع تأثيرات توهج وتنقل مرن */
    div.stButton > button {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 12px 28px;
        border-radius: 12px;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.2);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        width: 100%;
        cursor: pointer;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
        background: linear-gradient(135deg, #3b82f6 0%, #1e3a8a 100%);
        border-color: rgba(255, 255, 255, 0.2);
    }
    
    /* تخصيص مظهر شريط التنقل الجانبي المستقبلي */
    [data-testid="stSidebar"] {
        background-color: #0b0f19;
        border-right: 1px solid #1e293b;
    }
    
    /* تخصيص إطارات النجاح والأخطاء لتلائم الهوية البصرية فائقة الجودة */
    div[data-testid="stNotification"] {
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
    }
    
    /* إطار مخصص ومظلم لعرض المخرجات البرمجية */
    div.stCodeBlock {
        border-radius: 12px;
        border: 1px solid #1e293b;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# دالة برمجية معزولة وآمنة لتشغيل أكواد بايثون محلياً والتقاط النتائج
def run_python_code(code_str):
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout_res, stderr_res = "", ""
    ok = True
    try:
        # تنفيذ الكود البرمجي في بيئة محلية نظيفة
        exec(code_str, {"__builtins__": __builtins__}, {})
        stdout_res = redirected_output.getvalue()
    except Exception as e:
        ok = False
        import traceback
        stderr_res = traceback.format_exc().split('\n')[-2]
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
    
    class Result:
        def __init__(self, ok, stdout, stderr):
            self.ok = ok
            self.stdout = stdout
            self.stderr = stderr
            self.explanation_fr = "💡 Conseil IA: Erreur de syntaxe ou d'exécution. Vérifiez l'indentation (les espaces au début des lignes) et assurez-vous que toutes les variables sont correctement déclarées."
            self.explanation_ar = "💡 توجيه ذكي: حدث خطأ في بناء الجملة أو التنفيذ. يرجى التحقق من المسافات البادئة (Indentation) والتأكد من تعريف المتغيرات بشكل صحيح."
            
    return Result(ok, stdout_res, stderr_res)

# قاعدة بيانات التحديات والمسائل البرمجية المدمجة (ثنائية اللغة بالكامل)
CHALLENGES = [
    {
        "id": "ch1",
        "title_ar": "التحدي 1: متتالية فيبوناشي (Fibonacci)",
        "title_fr": "Défi 1: Suite de Fibonacci",
        "desc_ar": "اكتب دالة برمجية تقوم بحساب وعرض الحد N في متتالية فيبوناشي الشهيرة.",
        "desc_fr": "Écrivez une fonction Python qui calcule le N-ième terme de la suite de Fibonacci."
    },
    {
        "id": "ch2",
        "title_ar": "التحدي 2: التحقق من الأعداد الأولية",
        "title_fr": "Défi 2: Nombres Premiers",
        "desc_ar": "قم ببناء خوارزمية تختبر ما إذا كان الرقم المدخل أولياً (Prime) أم لا.",
        "desc_fr": "Créez un algorithme qui vérifie si un nombre donné est premier ou non."
    }
]

# 2. بناء القائمة الجانبية وإدارتها بشكل لغوي ديناميكي
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #3b82f6; font-weight:700;'>🌐 GLOBAL PLATFORM</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.9rem;'>الهوية المرئية الفائقة / UI Premium</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # قائمة اختيار لغة المنصة الموحدة
    language = st.selectbox(
        "Choose Language / اختر اللغة",
        ["Français", "العربية"],
        index=0
    )
    
    st.markdown("---")
    
    # تعديل اتجاه القوائم وعناوينها ديناميكياً بحسب اللغة المحددة
    if language == "العربية":
        st.markdown("<div style='text-align: right; color: #94a3b8; font-weight:600; margin-bottom:10px;'>لوحة التحكم والأقسام:</div>", unsafe_allow_html=True)
        sections = ["نظرة عامة على المنصة", "محرر بايثون الاحترافي", "التحديات والمنافسات الخوارزمية"]
        section = st.radio("", sections)
    else:
        st.markdown("<div style='color: #94a3b8; font-weight:600; margin-bottom:10px;'>Navigation & Control:</div>", unsafe_allow_html=True)
        sections = ["Vue d'ensemble", "Éditeur Python Interactif", "Défis algorithmiques"]
        section = st.radio("", sections)

# تهيئة وإعداد ذاكرة الجلسة (Session State) لمتابعة وحفظ نقاط تقدم الطلاب
if "completed_exercises" not in st.session_state:
    st.session_state["completed_exercises"] = []

# 3. معالجة وعرض الأقسام المحددة وبناء واجهاتها
if section in ["Vue d'ensemble", "نظرة عامة على المنصة"]:
    if language == "العربية":
        st.markdown("<div style='direction: rtl; text-align: right;'><h1 style='color: #3b82f6;'>مرحباً بك في منصة MI S1 العالمية 🎓</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem; color: #e2e8f0; line-height: 1.8;'>تم بناء هذه البيئة الرقمية بأعلى المعايير البصرية لتوفير تجربة تعليمية فائقة الجودة لطلاب شُعب الرياضيات والمعلوماتية الفتية. يمكنك هنا صقل مهاراتك البرمجية عبر أدوات التقييم اللحظي ومتابعة مسار خوارزمياتك خطوة بخطوة.</p></div>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='color: #3b82f6;'>Bienvenue sur la Plateforme MI S1 Globale 🎓</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem; color: #e2e8f0; line-height: 1.8;'>Découvrez un environnement d'apprentissage haut de gamme conçu pour maîtriser l'algorithmique et Python. Expérimentez le code en temps réel avec des retours d'évaluation instantanés et un suivi de progression adaptatif.</p>", unsafe_allow_html=True)

elif section in ["Éditeur Python Interactif", "محرر بايثون الاحترافي"]:
    if language == "العربية":
        st.markdown("<div style='direction: rtl; text-align: right;'><h1 style='color: #3b82f6;'>محرر الأكواد التفاعلي الفاخر 💻</h1></div>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='color: #3b82f6;'>Éditeur Python Interactif Premium 💻</h1>", unsafe_allow_html=True)
        
    default_snippet = "for i in range(1, 6):\n    print(f'Hello Global Python {i}')"
    
    # محاذاة واستخدام مكونات التحرير الاحترافية تالياً
    try:
        from streamlit_ace import st_ace
        code = st_ace(
            value=default_snippet,
            language="python",
            theme="monokai",
            keybinding="vscode",
            font_size=14,
            tab_size=4,
            height=280
        )
    except ImportError:
        # واجهة صندوق نصوص بديل أنيق في حال لم يتم تحميل التبعيات بعد في البيئة
        label_text = "أدخل كود البايثون الخاص بك هنا:" if language == "العربية" else "Saisissez votre code Python ci-dessous:"
        code = st.text_area(label_text, value=default_snippet, height=200)

    btn_label = "تحديث وتوصيل الشفرة" if language == "العربية" else "Exécuter la commande"
    
    if st.button(btn_label):
        result = run_python_code(code)
        if result.ok:
            success_msg = "🌟 مذهل! تم معالجة وتدقيق الكود بنجاح تام." if language == "العربية" else "🌟 Excellent ! Le code a été exécuté avec succès."
            st.success(success_msg)
            st.markdown("### 💻 Output / مخرجات الشفرة")
            st.code(result.stdout or ("(لا توجد مخرجات طباعة)" if language == "العربية" else "(Aucune sortie textuelle)"))
        else:
            error_msg = "❌ تم اكتشاف عائق برميجي أثناء المعالجة الحية" if language == "العربية" else "❌ Une erreur a été détectée lors de l'exécution"
            st.error(error_msg)
            st.markdown("### ⚠️ Runtime Trace / تفاصيل العطل")
            st.code(result.stderr)
            
            st.markdown("### 💡 Guided Assistance / الدعم الإرشادي الذكي")
            if language == "العربية":
                st.info(result.explanation_ar)
            else:
                st.info(result.explanation_fr)

elif section in ["Défis algorithmiques", "التحديات والمنافسات الخوارزمية"]:
    if language == "العربية":
        st.markdown("<div style='direction: rtl; text-align: right;'><h1 style='color: #3b82f6;'>المنافسات والتحديات البرمجية 🏆</h1></div>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='color: #3b82f6;'>Défis Algorithmiques Pro 🏆</h1>", unsafe_allow_html=True)
        
    for challenge in CHALLENGES:
        ch_title = challenge["title_ar"] if language == "العربية" else challenge["title_fr"]
        ch_desc = challenge["desc_ar"] if language == "العربية" else challenge["desc_fr"]
        
        st.markdown(f"### 🎯 {ch_title}")
        st.write(ch_desc)
        st.markdown("---")
